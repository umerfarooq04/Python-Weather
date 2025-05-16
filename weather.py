import requests
from config import API_KEY, BASE_URL

def get_weather(city, metric=True):
    units = 'metric' if metric else 'imperial'
    params = {'q': city, 'appid': API_KEY, 'units': units}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    return None
