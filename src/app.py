# app.py

from flask import Flask, jsonify, request
from weather_service import WeatherService

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Weather API!"

@app.route('/weather/<city_name>', methods=['GET'])
def get_weather_by_city(city_name):
    weather_data = WeatherService.get_current_weather(city_name)
    return jsonify(weather_data)

@app.route('/weather', methods=['GET'])
def get_weather_by_coordinates():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if not lat or not lon:
        return jsonify({"error": "Please provide latitude and longitude parameters"}), 400

    weather_data = WeatherService.get_weather_by_coordinates(lat, lon)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
