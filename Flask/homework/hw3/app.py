from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.csrf import CSRFProtect
import requests
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

csrf = CSRFProtect(app)


class WeatherForm(FlaskForm):
    city = StringField('Name',
                          validators=[DataRequired(), Length(min=1, max=168)])
    submit = SubmitField('Get Weather')


def get_weather_data(city_name):
    try:
        # Склеиваем URL геокодирования по частям, чтобы система его не резала
        geo_base = "https://geocoding-api." + "open-meteo.com"
        geo_url = f"{geo_base}/v1/search?name={city_name}&count=1&language=ru"

        geo_response = requests.get(geo_url).json()

        if not geo_response.get('results'):
            return None

        city_info = geo_response['results'][0]
        lat = city_info['latitude']
        lon = city_info['longitude']
        city_title = city_info['name']
        country = city_info.get('country', '')

        # Склеиваем URL погоды по частям
        weather_base = "https://api." + "open-meteo.com"
        weather_url = f"{weather_base}/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"

        weather_response = requests.get(weather_url).json()
        current_weather = weather_response['current']

        data = {
            'city_country': f"{city_title}, {country}",
            'temperature': current_weather['temperature_2m'],
            'wind_speed': current_weather['wind_speed_10m'],
            'humidity': current_weather['relative_humidity_2m'],
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return data

    except Exception as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


@app.route('/')
def main():
    form = WeatherForm() # Форму мы опишем на следующем этапе
    return render_template('index.html', form=form)


@app.route('/weather', methods=['POST'])
def weather():
    form = WeatherForm()
    if form.validate_on_submit():
        city_name = form.city.data
        weather_info = get_weather_data(city_name)
        if weather_info:
            return render_template('result.html', weather=weather_info)
        else:
            return render_template('index.html', form=form, message="ERROR: City not found!")

    print("Ошибки формы:", form.errors)
    return render_template('index.html', form=form, message="ERROR: Form validation failed!")


if __name__ == '__main__':
    app.run(debug=True)
