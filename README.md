## How It Works
- Fetches climate data via OpenWeatherMap API.
- Uses mock NDVI data due to delayed GEE access.
- Recommends planting zones based on climate and NDVI.
- Features a web interface to input locations and view results.

## Setup
1. Clone: `git clone https://github.com/Kartikesh0312/GreenSpaceAI.git`
2. Install: `pip install -r requirements.txt`
3. Add API key to `.env` (e.g., `OPENWEATHERMAP_API_KEY=your_key`).
4. Run the Flask app: `python app.py`
5. Open `http://127.0.0.1:5000/` in your browser.

## Notes
- GEE access delayed; used mock satellite data, ready for real data post-approval.