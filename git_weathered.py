import argparse  # Commands
import pyfiglet  # Ascii titles
from simple_chalk import chalk  # Colors
import requests

"""
This module provides functions to compile weather data from anywhere
in the form of a CLI program.
"""

print("This is my weather data compiler")

# API key for OpenWeatherMap API
API_KEY = "0ac74061ff0627cde608d666a3d35636"

# Base URL for OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Map the icons to the weather codes
WEATHER_ICONS = {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}

# Cnfigure the parser and its respective commands
parser = argparse.ArgumentParser(description="Check the weather for a certain country/city")
parser.add_argument("country", help="The country/city to ckeck the weather for")
args = parser.parse_args()  # Stores the input argument

# Construct the API URL with query parameters
url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

# Make API request and parse the response
response = requests.get(url)

if response.status_code != 200:
    print(chalk.red(f"""Error: Unable to retrieve weather information
                    Error code: {response.status_code}"""))
    exit()

# Parsing the JSON response and extract the weather information
data = response.json()

# Get the info
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

# Construct the ouput to the CLI
weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += "Current weather"
output += f"{weather_icon} {description}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels like: {feels_like}°C\n"

# Print output
print(chalk.blue(output))
print(data)
