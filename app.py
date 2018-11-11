# Below is the Flask stuff
from flask import Flask, render_template, request
import requests
import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import pyowm

app = Flask(__name__)

@app.route('/')
def home():
    api_instance = giphy_client.DefaultApi()
    api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
    tag = 'weather' # str | Filters results by specified tag. (optional)
    rating = 'g' # str | Filters results by specified rating. (optional)
    fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

    api_response = api_instance.gifs_random_get(api_key, tag=tag, rating=rating, fmt=fmt)
    gif = api_response.data.image_original_url

    # zipcode = '02215'
    # r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=1aa2295d44b63f9eefbc87f9ea449c32')
    # json_object = r.json()
    # temp_k = float(json_object['main']['temp'])
    # temp_f = (temp_k - 273.15) * 1.8 + 32

    owm = pyowm.OWM('e921cfa3d8fa4cf0b3d90a123dfb9424')
    user_input = input("Please enter a city name followed by the country name (ex. London, GB): ")
    observation = owm.weather_at_place(user_input)
    print(observation)
    w = observation.get_weather()
    temp = w.get_temperature('fahrenheit')
    hum = w.get_humidity()
    wind = w.get_wind()['speed']
    final = (temp['temp'], hum, wind)
    print(final)
    return str(final)



if __name__ == '__main__':
    app.run(debug=True)
