# app.py
from weather import get_weather_by_coordinates

def main():
    print("🌦 Welcome to the Weather App (Coordinate-Based) 🌍")
    lat = input("Enter latitude: ").strip()
    lon = input("Enter longitude: ").strip()

    weather = get_weather_by_coordinates(lat, lon)
    if weather:
        print(f"Current temperature: {weather['temperature']}°C")
        print(f"Wind speed: {weather['windspeed']} km/h")
        print(f"Weather code: {weather['weathercode']}")
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    main()
