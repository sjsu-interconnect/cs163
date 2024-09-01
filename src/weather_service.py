# weather_service.py

import requests
from config import Config

class WeatherService:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

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
