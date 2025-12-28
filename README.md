# Public WiFi Data

A collection of WiFi speed test data from hotels, airlines, and other public locations.

## About

This repository contains real-world WiFi performance data including download/upload speeds, latency, and jitter measurements from various locations. The data is useful for travelers, researchers, and anyone interested in public WiFi performance.

I know this isn't the most elegant solution, but I wanted to get this project going and hopefully as it grows, I'll continue to make improvements.

## Data Format

The data is stored in JSON format with the following structure:

- **Date Measured**: Date of the speed test (YYYY-MM-DD)
- **Name**: Location name
- **Address**: Physical address of the location (for Hotels, Restaurants, and Airline Lounges)
- **Category**: Type of location (Hotel, Airline, Airline Lounge, Restaurant, etc.)
- **Download (Mbps)**: Download speed in megabits per second
- **Upload (Mbps)**: Upload speed in megabits per second
- **Latency (ms)**: Network latency in milliseconds
- **Jitter (ms)**: Network jitter in milliseconds

For airline entries, additional fields include:
- **Airline**: Airline name
- **Aircraft Type**: Aircraft model
- **Route**: Flight route (e.g., "LAX-JFK")
- **Provider**: WiFi provider name

For airline lounge entries, additional fields include:
- **Airline**: Airline name
- **Address**: Physical address including airport and terminal
- Note: Airport and terminal should be included in the Name field (e.g., "Alaska Airlines Lounge - SFO Terminal 1")

For restaurant entries, additional fields include:
- **Brand**: Restaurant brand name
- **Address**: Physical address of the location

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to submit your WiFi speed test data.

You can submit data through:
- **GitHub Pull Request** (preferred) - Edit `wifi-data.json` directly
- **GitHub Issue** - Open an issue with your data and screenshot

All submissions require a screenshot of your speed test results for verification.

## License

This data is provided as-is for public use.

