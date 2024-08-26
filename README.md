# Weather CLI Application

## Overview

This project is a Python-based command-line interface (CLI) application that provides current weather information for any specified location. It also includes options to export the weather data in various formats (JSON, CSV, TXT).

## Features

- **Command-Line Interface**: Easily check the current weather for any city or country directly from the terminal.
- **API Integration**: Fetches weather data from an API using the specified location and language.
- **Multiple Export Options**: Export the weather data in JSON, CSV, or TXT format.
- **Error Handling**: Handles errors for invalid API requests or when the location is not found.
- **Colorful Output**: Outputs weather information with icons and colorful text.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Install Dependencies**: 
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **API Key**: Obtain an API key from the weather API provider and add it to your `config.py` file:
   ```python
   # config.py
   API_KEY = "your_api_key_here"
   BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
   ```

## Usage

1. **Basic Usage**:
   ```bash
   python weather_cli.py -c "City/Country"
   ```
   - Replace `"City, Country"` with the desired location.

2. **Language Option**:
   ```bash
   python weather_cli.py -c "City/Country" -l "en"
   ```
   - Replace `"en"` with the desired language code.

3. **Export Options**:
   - To export the weather data in TXT format:
     ```bash
     python weather_cli.py -c "City/Country" -e txt
     ```
   - To export the weather data in JSON format:
     ```bash
     python weather_cli.py -c "City/Country" -e json
     ```
   - To export the weather data in CSV format:
     ```bash
     python weather_cli.py -c "City/Country" -e csv
     ```

## Example

To get the weather in New York, in Spanish, and export it as a JSON file:

```bash
python weather_cli.py -c "New York" -l "es" -e json
```

## Error Handling

- If the location is not found:
  ```plaintext
  Error: Location 'City/Country' not found. Please check the spelling or try a different location.
  ```
- If the API request fails:
  ```plaintext
  Error: Unable to retrieve weather information. Error code: [HTTP Status Code]
  ```
# Enjoy this little project <3
