
# Prints the weather for a location from command line

# pip install requests

import requests

import time

import json

# Weather API URL and API key

api_url = "https://api.weatherapi.com/v1/current.json"

# Weather API key

api_key = "dd519b0eb51b2d09fb2e49bc0d7b6b5a" 

# Function to fetch weather data for a city

def get_weather(city):
    params = {
        "key": api_key,
        "q": city
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch weather data for {city}")
        return None

# Function to display weather data

def display_weather(data):
    if data:
        print("\nWeather Information:")
        print(f"Location: {data['location']['name']}, {data['location']['country']}")
        print(f"Temperature: {data['current']['temp_c']}°C")
        print(f"Condition: {data['current']['condition']['text']}")
    else:
        print("No weather data available.")

# Main function

if __name__  == "__main__":
    while True:
        city_name = input("Enter a city name (or 'exit' to quit): ")

        if city_name.lower() == "exit":
            break

        weather_data = get_weather(city_name)

        if weather_data:
            display_weather(weather_data)

        # Sleep for a random time between 15-30 seconds
        
        refresh_interval = 15 + 15 * (time.time() % 2)
        print(f"Refreshing in {refresh_interval} seconds...")
        time.sleep(refresh_interval)