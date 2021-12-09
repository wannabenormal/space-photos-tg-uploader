import os
from urllib.parse import urlparse, unquote
import requests


def get_extension_from_url(url):
    parsed_url = urlparse(unquote(url))
    file_name = os.path.split(parsed_url.path)[1]

    return os.path.splitext(file_name)[1]


def save_image(image, path_to_save):
    os.makedirs(os.path.dirname(path_to_save), exist_ok=True)

    with open(path_to_save, "wb") as file:
        file.write(image)


def download_image(url):
    response = requests.get(url)
    response.raise_for_status()

    return response.content
