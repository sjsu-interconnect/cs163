# weather_service.py

import requests
from config import Config

class WeatherService:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

    @staticmethod
    def get_current_weather(city_name):
        complete_url = f"{WeatherService.BASE_URL}q={city_name}&appid={Config.OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(complete_url)
        return response.json()

    @staticmethod
    def get_weather_by_coordinates(lat, lon):
        complete_url = f"{WeatherService.BASE_URL}lat={lat}&lon={lon}&appid={Config.OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(complete_url)
        return response.json()
