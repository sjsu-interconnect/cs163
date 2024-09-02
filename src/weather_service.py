# weather_service.py

import requests
from config import Config
from datetime import datetime, timedelta

class WeatherService:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    HISTORICAL_URL = "https://history.openweathermap.org/data/2.5/history/city?"

    @staticmethod
    def get_current_weather(city_name=None, lat=None, lon=None):
        if city_name:
            complete_url = f"{WeatherService.BASE_URL}q={city_name}&appid={Config.OPENWEATHER_API_KEY}&units=metric"
        elif lat and lon:
            complete_url = f"{WeatherService.BASE_URL}lat={lat}&lon={lon}&appid={Config.OPENWEATHER_API_KEY}&units=metric"
        else:
            return {"error": "You must provide either a city_name or both lat and lon coordinates."}

        response = requests.get(complete_url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Unable to fetch data. Please check the parameters and try again."}

    @staticmethod
    def get_historical_weather(lat, lon, start_date, end_date):
        # Convert start_date and end_date from string to datetime objects
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        # Convert the datetime objects to UNIX timestamps
        start_timestamp = int(start_date.timestamp())
        end_timestamp = int(end_date.timestamp())

        # Build the API request URL
        complete_url = (
            f"{WeatherService.HISTORICAL_URL}lat={lat}&lon={lon}&type=hour"
            f"&start={start_timestamp}&end={end_timestamp}&appid={Config.OPENWEATHER_API_KEY}"
        )

        # Debug: Print the complete URL
        print(f"API Request URL: {complete_url}")

        # Make the API request
        response = requests.get(complete_url)

        # Debug: Print response status and content
        print(f"Response Status: {response.status_code}")
        print(f"Response Content: {response.text}")

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API request failed with status code {response.status_code}: {response.text}"}