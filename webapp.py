from flask import Flask, render_template, request
from utils import get_weather_by_coordinates, weather_code_to_emoji

app = Flask(__name__)

def format_weather_card(weather):
    emoji = weather_code_to_emoji(weather['weathercode'])
    return (
        f"{emoji} Current temperature: {weather['temperature']}°C\n"
        f"💨 Wind speed: {weather['windspeed']} km/h\n"
        f"Weather code: {weather['weathercode']}"
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_text = None
    if request.method == 'POST':
        lat = request.form.get('latitude')
        lon = request.form.get('longitude')
        weather = get_weather_by_coordinates(lat, lon)
        if weather:
            weather_text = format_weather_card(weather)
    return render_template('index.html', weather_text=weather_text)

if __name__ == '__main__':
    app.run(debug=True)
