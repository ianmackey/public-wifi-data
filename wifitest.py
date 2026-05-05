#!/usr/bin/env python3
"""
CLI tool for collecting public WiFi speed test data.

Runs a speed test, collects location info, and commits the result
directly to the ianmackey/public-wifi-data repo via the GitHub API.

Usage:
    export GITHUB_TOKEN=ghp_...
    python wifitest.py
"""

import base64
import json
import os
import sys
from datetime import date

try:
    import requests
except ImportError:
    print("Missing dependency: requests")
    print("Install with: pip install requests")
    sys.exit(1)

REPO = "ianmackey/public-wifi-data"
FILE_PATH = "wifi-data.json"
GITHUB_API = "https://api.github.com"
NOMINATIM_URL = "https://nominatim.openstreetmap.org"
IP_API_URL = "http://ip-api.com/json"

CATEGORIES = ["Hotel", "Airport", "Restaurant", "Airline", "Airline Lounge"]


# ─────────────────────────────────────────────────────────────
# Speed Test
# ─────────────────────────────────────────────────────────────

def run_speedtest():
    """Run a speed test using speedtest-cli."""
    print("\nRunning speed test...")
    try:
        import speedtest as st
    except ImportError:
        print("Missing dependency: speedtest-cli")
        print("Install with: pip install speedtest-cli")
        sys.exit(1)

    s = st.Speedtest()
    s.get_best_server()

    print("  Testing download...")
    s.download()
    print("  Testing upload...")
    s.upload()

    results = s.results.dict()
    download_mbps = round(results["download"] / 1_000_000, 2)
    upload_mbps = round(results["upload"] / 1_000_000, 2)
    latency_ms = round(results["ping"], 2)

    print(f"  Download: {download_mbps} Mbps")
    print(f"  Upload:   {upload_mbps} Mbps")
    print(f"  Latency:  {latency_ms} ms")

    return {
        "download_mbps": download_mbps,
        "upload_mbps": upload_mbps,
        "latency_ms": latency_ms,
    }


# ─────────────────────────────────────────────────────────────
# Location Services
# ─────────────────────────────────────────────────────────────

def get_ip_location():
    """Get approximate location from IP address."""
    try:
        resp = requests.get(IP_API_URL, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if data.get("status") == "success":
            return {
                "city": data.get("city", ""),
                "region": data.get("regionName", ""),
                "country": data.get("country", ""),
                "lat": data.get("lat"),
                "lon": data.get("lon"),
            }
    except Exception:
        pass
    return None


def geocode_place(query):
    """Geocode a place name using Nominatim (OpenStreetMap). Returns (lat, lon) or None."""
    try:
        resp = requests.get(
            f"{NOMINATIM_URL}/search",
            params={"q": query, "format": "json", "limit": 1},
            headers={"User-Agent": "public-wifi-speedtest/1.0"},
            timeout=10,
        )
        resp.raise_for_status()
        results = resp.json()
        if results:
            return float(results[0]["lat"]), float(results[0]["lon"])
    except Exception:
        pass
    return None


def reverse_geocode(lat, lon):
    """Reverse geocode coordinates to a display name."""
    try:
        resp = requests.get(
            f"{NOMINATIM_URL}/reverse",
            params={"lat": lat, "lon": lon, "format": "json"},
            headers={"User-Agent": "public-wifi-speedtest/1.0"},
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        return data.get("display_name", f"{lat}, {lon}")
    except Exception:
        return f"{lat}, {lon}"


# ─────────────────────────────────────────────────────────────
# Interactive Prompts
# ─────────────────────────────────────────────────────────────

def prompt_input(prompt_text, default=None, required=True):
    """Prompt for input with optional default."""
    suffix = f" [{default}]" if default else ""
    while True:
        value = input(f"{prompt_text}{suffix}: ").strip()
        if not value and default is not None:
            return default
        if value or not required:
            return value
        print("  This field is required.")


def prompt_category():
    """Prompt user to select a category."""
    print("\nCategory:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}) {cat}")

    while True:
        choice = input("Select [1-5]: ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(CATEGORIES):
                return CATEGORIES[idx]
        except ValueError:
            pass
        print("  Invalid choice.")


def prompt_location(ip_loc):
    """Prompt user to verify or correct their location."""
    print("\n── Location ──")

    if ip_loc:
        city = ip_loc.get("city", "")
        region = ip_loc.get("region", "")
        country = ip_loc.get("country", "")
        lat = ip_loc.get("lat")
        lon = ip_loc.get("lon")
        loc_str = ", ".join(filter(None, [city, region, country]))
        print(f"  Detected: {loc_str} ({lat}, {lon})")
        print()
        print("  1) Accept detected location")
        print("  2) Search by place name")
        print("  3) Enter coordinates manually")

        while True:
            choice = input("Select [1-3]: ").strip()
            if choice == "1":
                name = prompt_input("Location name (e.g. 'Ritz Carlton Atlanta')")
                return {"name": name, "latitude": lat, "longitude": lon}
            elif choice == "2":
                break
            elif choice == "3":
                name = prompt_input("Location name")
                lat = float(prompt_input("Latitude"))
                lon = float(prompt_input("Longitude"))
                addr = reverse_geocode(lat, lon)
                print(f"  Resolved to: {addr}")
                return {"name": name, "latitude": lat, "longitude": lon}
            else:
                print("  Invalid choice.")
    else:
        print("  Could not detect location from IP.")

    query = prompt_input("Search for a place")
    coords = geocode_place(query)
    if coords:
        lat, lon = coords
        addr = reverse_geocode(lat, lon)
        print(f"  Found: {addr}")
        confirm = input("  Use this location? [Y/n]: ").strip().lower()
        if confirm in ("", "y", "yes"):
            name = prompt_input("Location name (e.g. 'Hilton LAX')")
            return {"name": name, "latitude": round(lat, 6), "longitude": round(lon, 6)}

    print("  Falling back to manual entry.")
    name = prompt_input("Location name")
    lat = float(prompt_input("Latitude"))
    lon = float(prompt_input("Longitude"))
    return {"name": name, "latitude": lat, "longitude": lon}


def prompt_category_fields(category):
    """Prompt for category-specific fields."""
    fields = {}
    print(f"\n── {category} Details ──")

    if category == "Hotel":
        fields["Website"] = prompt_input("Website URL", required=False)

    elif category == "Airport":
        fields["Website"] = prompt_input("Website URL", required=False)

    elif category == "Restaurant":
        fields["Brand"] = prompt_input("Brand name (e.g. 'Starbucks')", required=False)
        fields["Website"] = prompt_input("Website URL", required=False)

    elif category == "Airline":
        fields["Airline"] = prompt_input("Airline name")
        fields["Tail Number"] = prompt_input("Tail number (e.g. 'N178JB')", required=False)
        fields["Aircraft Type"] = prompt_input("Aircraft type (e.g. 'A321')", required=False)
        fields["Route"] = prompt_input("Route (e.g. 'LAX-JFK')", required=False)
        fields["Provider"] = prompt_input("WiFi provider (e.g. 'Viasat')", required=False)

    elif category == "Airline Lounge":
        fields["Airline"] = prompt_input("Airline name")
        fields["Website"] = prompt_input("Website URL", required=False)

    return {k: v for k, v in fields.items() if v}


# ─────────────────────────────────────────────────────────────
# GitHub API Persistence
# ─────────────────────────────────────────────────────────────

def get_github_token():
    """Get GitHub token from environment or prompt."""
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token

    print("\nGITHUB_TOKEN not set.")
    print("Create a token at: https://github.com/settings/tokens")
    print("Required scope: repo (or public_repo for public repos)")
    token = input("Paste your GitHub token: ").strip()
    if not token:
        print("Token required to push data.")
        sys.exit(1)
    return token


def fetch_current_data(token):
    """Fetch the current wifi-data.json from the repo. Returns (data_list, file_sha)."""
    url = f"{GITHUB_API}/repos/{REPO}/contents/{FILE_PATH}"
    resp = requests.get(url, headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }, timeout=30)
    resp.raise_for_status()
    content = resp.json()
    data = json.loads(base64.b64decode(content["content"]).decode("utf-8"))
    return data, content["sha"]


def push_new_entry(token, entry, current_data, sha):
    """Append entry to current data and push via GitHub API."""
    current_data.append(entry)
    updated_json = json.dumps(current_data, indent=2) + "\n"
    encoded = base64.b64encode(updated_json.encode("utf-8")).decode("utf-8")

    commit_msg = f"Add {entry.get('Category', 'entry')}: {entry.get('Name', 'Unknown')} - {entry.get('Date Measured', '')}"

    url = f"{GITHUB_API}/repos/{REPO}/contents/{FILE_PATH}"
    resp = requests.put(url, headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }, json={
        "message": commit_msg,
        "content": encoded,
        "sha": sha,
    }, timeout=30)
    resp.raise_for_status()
    return resp.json()


# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("  Public WiFi Speed Test")
    print("=" * 50)

    token = get_github_token()

    speed = run_speedtest()

    ip_loc = get_ip_location()

    category = prompt_category()

    is_airline = category == "Airline"

    if is_airline:
        location = {"name": None, "latitude": None, "longitude": None}
    else:
        location = prompt_location(ip_loc)

    cat_fields = prompt_category_fields(category)

    today = date.today().isoformat()

    entry = {"Date Measured": today}

    if is_airline:
        name_parts = []
        if cat_fields.get("Airline"):
            name_parts.append(cat_fields["Airline"])
        if cat_fields.get("Route"):
            name_parts.append(cat_fields["Route"])
        entry["Name"] = " ".join(name_parts) if name_parts else prompt_input("Entry name")
    else:
        entry["Name"] = location["name"]

    entry["Category"] = category

    entry.update(cat_fields)

    if not is_airline:
        entry["Latitude"] = location["latitude"]
        entry["Longitude"] = location["longitude"]

    entry["Download (Mbps)"] = speed["download_mbps"]
    entry["Upload (Mbps)"] = speed["upload_mbps"]
    entry["Latency (ms)"] = speed["latency_ms"]
    entry["Jitter (ms)"] = None

    print("\n── Preview ──")
    print(json.dumps(entry, indent=2))

    confirm = input("\nPush this entry to GitHub? [Y/n]: ").strip().lower()
    if confirm not in ("", "y", "yes"):
        print("Cancelled.")
        sys.exit(0)

    print("\nPushing to GitHub...")
    current_data, sha = fetch_current_data(token)
    push_new_entry(token, entry, current_data, sha)

    print("Done! Entry added to wifi-data.json")
    print("View map: https://ianmackey.github.io/public-wifi-data/")


if __name__ == "__main__":
    main()
