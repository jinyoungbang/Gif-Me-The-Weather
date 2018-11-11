# Below is the Flask stuff
from flask import Flask, render_template, request, redirect, url_for
import requests
import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import pyowm

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index1.html')
    # print('here')
    # return redirect(url_for('result'))



@app.route('/result', methods=['GET', 'POST'])
def home():


    if request.method == 'POST':
        user_input = request.form['location']
        owm = pyowm.OWM('e921cfa3d8fa4cf0b3d90a123dfb9424')
        # user_input = request.form.get('location')
        observation = owm.weather_at_place(user_input)
        w = observation.get_weather()
        temp = w.get_temperature('fahrenheit')
        hum = w.get_humidity()
        wind = w.get_wind()['speed']
        final = temp['temp']

        if final > 77:
            str_var = "hot weather burning fire summer"
        elif final > 68:
            str_var = "beach pool sunny weather surfing"
        elif final > 54:
            str_var = "autumn fall weather spring "
        elif final > 14:
            str_var = "cold winter snow skiing christmas"
        else:
            str_var = "freezing hypothermia snowstorm iceage shivering"

        api_instance = giphy_client.DefaultApi()
        api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
        tag = str_var # str | Filters results by specified tag. (optional)
        rating = 'g' # str | Filters results by specified rating. (optional)
        fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

        api_response = api_instance.gifs_random_get(api_key, tag=tag, rating=rating, fmt=fmt)
        gif = api_response.data.image_original_url

        return render_template('result1.html', final = final, gif = gif)


if __name__ == '__main__':
    app.run()
