## How It Works
- Fetches climate data via OpenWeatherMap API.
- Uses mock NDVI data due to delayed GEE access.
- Recommends planting zones based on climate and NDVI.

## Setup
1. Clone: `git clone https://github.com/Kartikesh0312/GreenSpaceAI.git`
2. Install: `pip install -r requirements.txt`
3. Add API key to `.env`.
4. Run: `python src/data_fetch.py`