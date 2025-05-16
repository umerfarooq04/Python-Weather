import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable or use a default (you should set your API key in .env file)
API_KEY = os.getenv('OPENWEATHER_API_KEY', 'your_api_key_here')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
