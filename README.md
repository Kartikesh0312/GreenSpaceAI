## How It Works
- Fetches climate data via OpenWeatherMap API based on city name input.
- Uses mock NDVI data due to delayed GEE access.
- Recommends planting needs based on heat waves (temp > 30°C suggests more plantation).
- Features a web interface for user-friendly interaction.

## Setup (Local)
1. Clone: `git clone https://github.com/Kartikesh0312/GreenSpaceAI.git`
2. Install: `pip install -r requirements.txt`
3. Add API key to `.env` (e.g., `OPENWEATHERMAP_API_KEY=your_key`).
4. Run: `python app.py`
5. Open `http://127.0.0.1:5000/`.

## Deployed Version
- Access online at: https://greenspaceai.onrender.com
- No setup required—just enter a city name!

## Notes
- GEE access delayed; used mock satellite data, ready for real data post-approval.