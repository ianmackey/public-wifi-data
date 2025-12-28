# Public WiFi Data

A collection of WiFi speed test data from hotels, airlines, and other public locations.

## About

This repository contains real-world WiFi performance data including download/upload speeds, latency, and jitter measurements from various locations. The data is useful for travelers, researchers, and anyone interested in public WiFi performance.

I know this isn't the most elegant solution, but I wanted to get this project going and hopefully as it grows, I'll continue to make improvements.

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

## Contributing

I'll be adding support for contributions soon - likely through simple form submission.

## License

This data is provided as-is for public use.

