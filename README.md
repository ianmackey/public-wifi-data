# Public WiFi Data

A collection of WiFi speed test data from hotels, airlines, and other public locations.

## About

This repository contains real-world WiFi performance data including download/upload speeds, latency, and jitter measurements from various locations. The data is useful for travelers, researchers, and anyone interested in public WiFi performance.

## Data Format

The data is stored in JSON format with the following structure:

- **Date Measured**: Date of the speed test (YYYY-MM-DD)
- **Name**: Location name
- **Category**: Type of location (Hotel, Airline, etc.)
- **Download (Mbps)**: Download speed in megabits per second
- **Upload (Mbps)**: Upload speed in megabits per second
- **Latency (ms)**: Network latency in milliseconds
- **Jitter (ms)**: Network jitter in milliseconds

For airline entries, additional fields include:
- **Airline**: Airline name
- **Aircraft Type**: Aircraft model
- **Route**: Flight route (e.g., "LAX-JFK")
- **Provider**: WiFi provider name

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to submit your WiFi speed test data.

Quick steps:
1. Click "Edit this file" on `wifi-data.json`
2. Add your entry following the existing format
3. Include a screenshot of your speed test results
4. Submit a pull request

## License

This data is provided as-is for public use.

