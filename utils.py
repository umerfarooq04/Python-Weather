
def format_weather(data, metric=True):
    main = data['main']
    weather_desc = data['weather'][0]['description']
    wind = data.get('wind', {})
    visibility = data.get('visibility', 0)

    icon = get_weather_icon(weather_desc)
    temp_unit = "°C" if metric else "°F"
    speed_unit = "m/s" if metric else "mph"

    return (
        f"{icon} Weather: {weather_desc.capitalize()}\n"
        f"Temperature: {main['temp']}{temp_unit}\n"
        f"Humidity: {main['humidity']}%\n"
        f"Wind Speed: {wind.get('speed', 0)} {speed_unit}\n"
        f"Visibility: {visibility} m"
    )

def save_to_history(city, result):
    with open("history.txt", "a") as file:
        file.write(f"{city} - {result}\n")
