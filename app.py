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
    # Get latitude and longitude from the form
    lat = request.form.get("latitude")
    lon = request.form.get("longitude")
    
    try:
        lat = float(lat)
        lon = float(lon)
    except ValueError:
        return jsonify({"error": "Invalid latitude or longitude. Please enter numeric values."}), 400

    # Fetch weather data
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
    else:
        return jsonify({"error": f"Error fetching weather data: {data.get('message', 'Unknown error')}"}), 400

    # Mock satellite data (NDVI)
    mock_ndvi = 0.65
    recommendation = "Suitable for tree planting (good vegetation)." if mock_ndvi > 0.5 else "May need preparation for planting."

    return jsonify({
        "temperature": temp,
        "humidity": humidity,
        "ndvi": mock_ndvi,
        "recommendation": recommendation
    })

if __name__ == "__main__":
    app.run(debug=True)