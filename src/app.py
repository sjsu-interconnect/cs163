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

@app.route('/historical-weather', methods=['GET'])
def get_historical_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not lat or not lon or not start_date or not end_date:
        return jsonify({"error": "Please provide latitude, longitude, start_date, and end_date parameters."}), 400

    historical_data = WeatherService.get_historical_weather(lat, lon, start_date, end_date)
    return jsonify(historical_data)

if __name__ == '__main__':
    app.run(debug=True)
