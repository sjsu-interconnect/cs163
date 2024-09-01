# app.py

from flask import Flask, request, jsonify
from weather_service import WeatherService

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Weather API!"

@app.route('/current-weather', methods=['GET'])
def get_current_weather():
    city_name = request.args.get('city_name')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if not city_name and (not lat or not lon):
        return jsonify({"error": "You must provide either a city_name or both lat and lon coordinates."}), 400

    weather_data = WeatherService.get_current_weather(city_name=city_name, lat=lat, lon=lon)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
