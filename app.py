from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Weather API Service is up and running!"
if __name__ == "__main__":
    app.run(debug=True)

import requests

API_KEY = "your_openweathermap_api_key"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Please provide a city"}), 400

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Could not retrieve weather data"}), response.status_code
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500
@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Please provide a city"}), 400

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return jsonify(weather_info)
    else:
        return jsonify({"error": "Could not retrieve weather data"}), response.status_code
