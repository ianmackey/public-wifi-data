# Contributing WiFi Speed Test Data

Thank you for contributing to the public WiFi data collection! Your submissions help create a valuable resource for travelers and researchers.

## How to Submit

1. Click the "Edit this file" (pencil icon) on `wifi-data.json`
2. Add your entry following the existing format
3. Fill out the PR template completely
4. **Attach a screenshot** of your speed test results (required for verification)
5. Submit the pull request

## Data Format

Please follow this JSON structure:

```json
{
  "Date Measured": "YYYY-MM-DD",
  "Name": "Location Name",
  "Category": "Hotel" or "Airline",
  "Download (Mbps)": 0.0,
  "Upload (Mbps)": 0.0,
  "Latency (ms)": 0.0,
  "Jitter (ms)": 0.0
}
```

For airline entries, also include:
- `"Airline"`: Airline name
- `"Aircraft Type"`: Aircraft model
- `"Route"`: Origin-Destination (e.g., "LAX-JFK")
- `"Provider"`: WiFi provider name

## Required Screenshot

Please include a screenshot from your speed test tool (Speedtest.net, Fast.com, etc.) showing:
- Download speed
- Upload speed
- Latency/Jitter
- Date/time of test

This helps verify the accuracy of submissions and ensures data quality.

## Guidelines

- Use a reliable speed test service (Speedtest.net, Fast.com, Google Speed Test, etc.)
- Test during normal usage conditions
- Include the exact location name as it appears
- Use the date format YYYY-MM-DD
- If latency/jitter data is unavailable, use `null` in the JSON

Thank you for your contribution!

