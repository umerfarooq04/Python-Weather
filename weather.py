# util.py
import requests

def get_weather_by_coordinates(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('current_weather', None)
    else:
        print(f"[HTTP ERROR] {response.status_code} - {response.reason}")
        return None
