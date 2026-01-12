# Public WiFi Data

A collection of WiFi speed test data from hotels, airlines, and other public locations, visualized on an interactive map.

## About

This repository contains real-world WiFi performance data including download/upload speeds, latency, and jitter measurements from various locations. The data is useful for travelers, researchers, and anyone interested in public WiFi performance.

**View the interactive map**: The data is visualized on an interactive map at `index.html` which can be viewed directly on GitHub Pages or by opening the file locally.

## Features

The interactive map includes:

- **Interactive Map Visualization**: Color-coded markers based on download speed (green = fast, red = slow)
- **Marker Clustering**: Automatically clusters markers when zoomed out for better performance
- **Category Filtering**: Filter by location type (Hotels, Restaurants, Airline Lounges, etc.)
- **Statistics Display**: Real-time statistics showing total locations, average speeds, and fastest/slowest connections
- **Speed Legend**: Visual guide showing the color-to-speed mapping
- **Location Search**: Search for cities or zip codes to quickly navigate the map
- **Enhanced Popups**: Detailed information including category, provider, and speed metrics
- **Mobile Optimized**: Fully responsive design optimized for mobile devices
- **Airline Data Table**: Separate table view for airline WiFi data (routes, aircraft types, providers)
- **Free & Open Source**: Uses Leaflet with OpenStreetMap tiles - no API key required

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

- **Filter Dropdown**: Select a category to filter locations (All, Hotel, Restaurant, Airline Lounge, etc.)
- **Search Box**: Enter a city name or zip code to fly to that location on the map
- **Statistics Display**: View summary statistics for the currently filtered data (displayed as plain text)
- **Speed Legend**: Reference guide showing what each marker color represents

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

## Contributing

I'll be adding support for contributions soon - likely through simple form submission.

## License

This data is provided as-is for public use.

