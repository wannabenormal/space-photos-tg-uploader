import os
from urllib.parse import urlparse, unquote
import requests


def get_extension_from_url(url):
    parsed_url = urlparse(unquote(url))
    file_name = os.path.split(parsed_url.path)[1]

    return os.path.splitext(file_name)[1]


def download_image(url, path_to_save, params={}):
    response = requests.get(url, params=params)
    response.raise_for_status()

    image = response.content
    with open(path_to_save, "wb") as file:
        file.write(image)
