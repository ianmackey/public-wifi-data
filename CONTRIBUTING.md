# Contributing WiFi Speed Test Data

Thank you for contributing to the public WiFi data collection! Your submissions help create a valuable resource for travelers and researchers.

## How to Submit

### Option 1: GitHub Pull Request (Preferred)
1. Click the "Edit this file" (pencil icon) on `wifi-data.json`
2. Add your entry following the existing format
3. Fill out the PR template completely
4. **Attach a screenshot** of your speed test results (required for verification)
5. Submit the pull request

### Option 2: GitHub Issue
1. Open a new [GitHub Issue](https://github.com/ianmackey/public-wifi-data/issues/new)
2. Include all required information from the data format section below
3. **Attach a screenshot** of your speed test results (required for verification)
4. We'll add your entry to the dataset

## Data Format

Please follow this JSON structure:

**Basic structure (all entries):**
```json
{
  "Date Measured": "YYYY-MM-DD",
  "Name": "Location Name",
  "Category": "Hotel", "Airline", "Airline Lounge", "Restaurant", etc.,
  "Download (Mbps)": 0.0,
  "Upload (Mbps)": 0.0,
  "Latency (ms)": 0.0,
  "Jitter (ms)": 0.0
}
```

**For hotel entries, also include:**
- `"Address"`: Physical address of the hotel

**For airline entries, also include:**
- `"Airline"`: Airline name
- `"Aircraft Type"`: Aircraft model
- `"Route"`: Origin-Destination (e.g., "LAX-JFK")
- `"Provider"`: WiFi provider name

**For airline lounge entries, also include:**
- `"Address"`: Physical address including airport and terminal
- `"Airline"`: Airline name
- Note: Include airport and terminal in the Name field (e.g., "Alaska Airlines Lounge - SFO Terminal 1")

**For restaurant entries, also include:**
- `"Address"`: Physical address of the restaurant
- `"Brand"`: Restaurant brand name

## Required Screenshot

Please include a screenshot from your speed test tool ([Speedtest.net](https://www.speedtest.net/), [Fast.com](https://fast.com/), [Cloudflare Speed Test](https://speed.cloudflare.com/), etc.) showing:
- Download speed
- Upload speed
- Latency/Jitter
- Date/time of test

This helps verify the accuracy of submissions and ensures data quality.

## Guidelines

- Use a reliable speed test service:
  - [Speedtest.net](https://www.speedtest.net/)
  - [Fast.com](https://fast.com/)
  - [Google Speed Test](https://www.google.com/search?q=speed+test)
  - [Cloudflare Speed Test](https://speed.cloudflare.com/)
- Please disable VPN when running speed tests. If you can't or don't feel comfortable disabling your VPN, please note VPN usage in your submission
- Test during normal usage conditions
- Include the exact location name as it appears
- Use the date format YYYY-MM-DD
- If latency/jitter data is unavailable, use `null` in the JSON

Thank you for your contribution!

