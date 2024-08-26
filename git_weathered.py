"""Module providing the current weather of any location and various export options"""

import datetime  # Get datetime
import json  # Handle json files
import argparse  # Commands
import requests  # Get http requests
import pandas  # To export
import pyfiglet  # Ascii titles
from simple_chalk import chalk  # Colors
import config as conf
import api_codes as ac

time_now = datetime.datetime.now()  # Get the time now

# Configure the parser and its respective commands
parser = argparse.ArgumentParser(
    description="Check the weather for a certain country/city and export the data"
)
parser.add_argument(
    "-c",
    "--country",
    default="Asuncion",
    help="The country/city to ckeck the weather for",
)
parser.add_argument(
    "-l",
    "--language",
    default="en",
    help=f"The language of the data. Languages: {ac.LANGUAGE_CODES}",
)
parser.add_argument(
    "-e",
    "--export",
    help="type of file of the export",
)
args = parser.parse_args()  # Stores the input argument

# Construct the API URL with query parameters
url = f"{conf.BASE_URL}?q={args.country}&appid={conf.API_KEY}&units=metric&lang={args.language}"

# Make API request and save the response
response = requests.get(url)

# In case of errors
if response.status_code == 404:
    print(
        chalk.red(
            f"Error: Location '{args.country}' not found. Please check the spelling or try a different location."
        )
    )
    exit()
elif response.status_code != 200:
    print(
        chalk.red(
            f"Error: Unable to retrieve weather information. Error code: {response.status_code}"
        )
    )
    exit()

# Parsing the JSON response and extract the weather information
data = response.json()

# Get the info from the response
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]

# Construct the ouput to the CLI
weather_icon = ac.WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += "Current weather:  "
output += f"{weather_icon} {description}\n\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels like: {feels_like}°C\n\n"
output += f"Humidity: {humidity}\n\n"
output += f"Wind speed: {wind_speed}\n"

# Export options
if args.export == "txt" or args.export == "text":
    export = open(f"report_{time_now}.txt", "a", encoding="utf-8")
    export.write(output)
    export.close()

if args.export == "json":
    with open(f"report_{time_now}.json", "w", encoding="utf-8") as export:
        json.dump(data, export, ensure_ascii=False, indent=4)


if args.export == "csv":
    # Convert the weather data into a pandas DataFrame
    weather_data = {
        "City": [city],
        "Country": [country],
        "Temperature (°C)": [temperature],
        "Feels Like (°C)": [feels_like],
        "Description": [description],
        "Humidity": [humidity],
        "Wind Speed": [wind_speed],
    }

    df = pandas.DataFrame(weather_data)

    # Export the DataFrame to a CSV file
    df.to_csv(f"{time_now}.csv", encoding="utf-8", index=False)

# Print output
print(chalk.cyan(output))
