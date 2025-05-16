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

def weather_code_to_emoji(code):
    mapping = {
        0: "☀️",    # Clear sky
        1: "🌤️",   # Mainly clear
        2: "⛅",    # Partly cloudy
        3: "☁️",    # Overcast
        45: "🌫️",   # Fog
        48: "🌫️",   # Depositing rime fog
        51: "🌦️",   # Drizzle: Light
        53: "🌧️",   # Drizzle: Moderate
        55: "🌧️",   # Drizzle: Dense
        61: "🌧️",   # Rain: Slight
        63: "🌧️",   # Rain: Moderate
        65: "🌧️",   # Rain: Heavy
        71: "🌨️",   # Snow fall: Slight
        73: "🌨️",   # Snow fall: Moderate
        75: "🌨️",   # Snow fall: Heavy
        80: "🌧️",   # Rain showers: Slight
        81: "🌧️",   # Rain showers: Moderate
        82: "🌧️",   # Rain showers: Violent
        95: "⛈️",   # Thunderstorm: Slight or moderate
        99: "⛈️",   # Thunderstorm with hail
    }
    return mapping.get(code, "❓")  # Default unknown emoji
