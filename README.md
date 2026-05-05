# Public WiFi Data

A collection of WiFi speed test data from hotels, airlines, and other public locations, visualized on an interactive map.

## About

This repository contains real-world WiFi performance data including download/upload speeds, latency, and jitter measurements from various locations. The data is useful for travelers, researchers, and anyone interested in public WiFi performance.

**View the interactive map**: The data is visualized on an interactive map at `index.html` which can be viewed directly on GitHub Pages or by opening the file locally.

## Features

The interactive map includes:

- **Interactive Map Visualization**: Color-coded markers based on download speed (green = fast, red = slow)
- **Marker Clustering**: Automatically clusters markers when zoomed out for better performance
- **Statistics Display**: Real-time statistics showing total locations, average speeds, and fastest/slowest connections
- **Speed Legend**: Visual guide showing the color-to-speed mapping (collapsible to save space)
- **Location Search**: Search for cities or zip codes to quickly navigate the map
- **Enhanced Popups**: Detailed information including category, provider, and speed metrics
- **Mobile Optimized**: Fully responsive design optimized for mobile devices
- **Free & Open Source**: Uses Leaflet with OpenStreetMap tiles - no API key required

**Note**: Airline data (in-flight WiFi measurements) is currently not displayed on the map as these entries don't have geographic coordinates. Only location-based data (hotels, restaurants, airline lounges, airports, etc.) with coordinates are shown.

## Viewing the Map

You can view the interactive map on my website at [https://ianmackey.com/internet-speeds/](https://ianmackey.com/internet-speeds/).

Alternatively, you can open `index.html` locally in a web browser.

The map uses Leaflet with OpenStreetMap tiles - no API key or authentication required.

## Data Format

The data is stored in JSON format with the following structure:

- **Date Measured**: Date of the speed test (YYYY-MM-DD)
- **Name**: Location name
- **Category**: Type of location (Hotel, Airline, Airline Lounge, Restaurant, etc.)
- **Latitude**: Geographic latitude coordinate (decimal degrees) - not included for Airline entries
- **Longitude**: Geographic longitude coordinate (decimal degrees) - not included for Airline entries
- **Download (Mbps)**: Download speed in megabits per second
- **Upload (Mbps)**: Upload speed in megabits per second
- **Latency (ms)**: Network latency in milliseconds
- **Jitter (ms)**: Network jitter in milliseconds

For airline entries, additional fields include:
- **Airline**: Airline name
- **Aircraft Type**: Aircraft model
- **Route**: Flight route (e.g., "LAX-JFK")
- **Provider**: WiFi provider name

For hotel entries, additional fields include:
- **Website**: Official website URL
- **Latitude**: Geographic latitude coordinate (decimal degrees)
- **Longitude**: Geographic longitude coordinate (decimal degrees)

For airline lounge entries, additional fields include:
- **Airline**: Airline name
- **Website**: Official website URL
- **Latitude**: Geographic latitude coordinate (decimal degrees)
- **Longitude**: Geographic longitude coordinate (decimal degrees)
- Note: Airport and terminal should be included in the Name field (e.g., "Alaska Airlines Lounge - SFO Terminal 1")

For restaurant entries, additional fields include:
- **Brand**: Restaurant brand name
- **Website**: Official website URL
- **Latitude**: Geographic latitude coordinate (decimal degrees)
- **Longitude**: Geographic longitude coordinate (decimal degrees)

## Using the Map

### Controls

- **Search Box**: Enter a city name or zip code to fly to that location on the map
- **Statistics Display**: View summary statistics for all location-based data (displayed as plain text)
- **Speed Legend**: Reference guide showing what each marker color represents (click to expand/collapse)

### Map Interactions

- **Click Markers**: Click any marker to see detailed information in a popup
- **Click Clusters**: Click clustered markers to zoom in and see individual locations
- **Zoom & Pan**: Use mouse/touch gestures to navigate the map
- **Navigation Controls**: Use the zoom buttons in the top-right corner

### Color Coding

Markers are color-coded by download speed:
- 🟢 **Green** (≥100 Mbps): Excellent
- 🟡 **Lime** (50-99 Mbps): Good
- 🟡 **Yellow** (25-49 Mbps): Fair
- 🟠 **Orange** (10-24 Mbps): Slow
- 🔴 **Red** (<10 Mbps): Very Slow

## Adding Speed Test Data (CLI)

A Python CLI tool is included for quickly running a speed test and pushing results to this repo.

### Prerequisites

- Python 3.8+
- A speed test tool (either one):
  - **Ookla Speedtest CLI** (recommended — includes jitter): https://www.speedtest.net/apps/cli
  - **Python speedtest-cli** (fallback — no jitter): `pip install speedtest-cli`
- A [GitHub personal access token](https://github.com/settings/tokens) with `public_repo` scope

### Setup

```bash
pip install -r requirements.txt
export GITHUB_TOKEN=ghp_your_token_here
```

### Usage

```bash
python speedtest.py
```

The tool will:
1. Run a speed test (download, upload, latency, jitter)
2. Detect your approximate location via IP
3. Prompt you to verify/correct the location
4. Ask for category and category-specific details
5. Show a preview of the entry
6. Push directly to `wifi-data.json` via the GitHub API

### Example Session

```
==================================================
  Public WiFi Speed Test
==================================================

Running speed test...
  Download: 91.5 Mbps
  Upload:   90.5 Mbps
  Latency:  19.0 ms
  Jitter:   5.0 ms
  (via Ookla Speedtest CLI)

Category:
  1) Hotel
  2) Airport
  3) Restaurant
  4) Airline
  5) Airline Lounge
Select [1-5]: 1

── Location ──
  Detected: San Francisco, California, United States (37.7749, -122.4194)

  1) Accept detected location
  2) Search by place name
  3) Enter coordinates manually
Select [1-3]: 1
Location name: Hilton San Francisco Union Square

── Hotel Details ──
Website URL: https://www.hilton.com/...

── Preview ──
{
  "Date Measured": "2026-05-05",
  "Name": "Hilton San Francisco Union Square",
  "Category": "Hotel",
  "Website": "https://www.hilton.com/...",
  "Latitude": 37.7749,
  "Longitude": -122.4194,
  "Download (Mbps)": 91.5,
  "Upload (Mbps)": 90.5,
  "Latency (ms)": 19.0,
  "Jitter (ms)": 5.0
}

Push this entry to GitHub? [Y/n]: y

Pushing to GitHub...
Done! Entry added to wifi-data.json
```

## Contributing

I'll be adding support for contributions soon - likely through simple form submission.

## License

This data is provided as-is for public use.

