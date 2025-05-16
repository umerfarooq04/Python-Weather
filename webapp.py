from flask import Flask, render_template, request
from utils import get_weather_by_coordinates, weather_code_to_emoji

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    emoji = ''
    if request.method == 'POST':
        lat = request.form.get('latitude')
        lon = request.form.get('longitude')
        weather = get_weather_by_coordinates(lat, lon)
        if weather:
            emoji = weather_code_to_emoji(weather['weathercode'])
    return render_template('index.html', weather=weather, emoji=emoji)

if __name__ == '__main__':
    app.run(debug=True)
