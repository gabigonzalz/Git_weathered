import argparse # Commands
import pyfiglet # Ascii titles
from simple_chalk import chalk # Colors
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

