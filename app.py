from weather import get_weather_by_coordinates
from utils import weather_code_to_emoji

def main():
    print("🌦 Welcome to the Weather App (Coordinate-Based) 🌍")
    lat = input("Enter latitude: ").strip()
    lon = input("Enter longitude: ").strip()

    weather = get_weather_by_coordinates(lat, lon)
    if weather:
        emoji = weather_code_to_emoji(weather['weathercode'])
        print(f"{emoji} Current temperature: {weather['temperature']}°C")
        print(f"💨 Wind speed: {weather['windspeed']} km/h")
        print(f"Weather code: {weather['weathercode']}")
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    main()
