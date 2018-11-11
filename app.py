# Below is the Flask stuff
from flask import Flask, render_template
import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint

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
    return gif


if __name__ == '__main__':
    app.run(debug=True)
