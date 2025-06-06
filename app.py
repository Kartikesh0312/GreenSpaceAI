import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load API key
load_dotenv()
api_key = os.getenv("OPENWEATHERMAP_API_KEY")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/fetch_data", methods=["POST"])
def fetch_data():
    city = request.form.get("city")
    if not city:
        return jsonify({"error": "No city provided. Please enter a city name."}), 400
    city = city.strip()

    # Geocode city to get latitude and longitude using OpenWeatherMap API
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    geocode_response = requests.get(geocode_url).json()

    if not geocode_response or "lat" not in geocode_response[0]:
        return jsonify({"error": "City not found. Please check the name and try again."}), 400

    lat = geocode_response[0]["lat"]
    lon = geocode_response[0]["lon"]

    # Fetch weather data
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    weather_response = requests.get(weather_url)
    data = weather_response.json()

    if weather_response.status_code == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
    else:
        return jsonify({"error": f"Error fetching weather data: {data.get('message', 'Unknown error')}"}), 400

    # Mock NDVI (temporary until GEE access)
    mock_ndvi = 0.65
    # Recommendation based on heat waves (temp > 30°C suggests need for more plantation)
    recommendation = "This area needs more plantation due to high heat waves." if temp > 30 else "Suitable for current planting conditions."

    return jsonify({
        "temperature": temp,
        "humidity": humidity,
        "ndvi": mock_ndvi,
        "recommendation": recommendation,
        "city": city
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=False) 