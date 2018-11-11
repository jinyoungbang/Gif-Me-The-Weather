from urllib.request import urlopen
import json


def random_gif():
    api_key = "dc6zaTOxFJmzC"
    finalURL = "https://api.giphy.com/v1/gifs/random?api_key=" + api_key

    data = json.loads(urlopen(finalURL).read().decode('utf-8'))

    dataArray = [data["data"]["image_url"], data["data"]["url"]]

    return dataArray
