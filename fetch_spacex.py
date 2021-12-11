import os
import requests
from utils import download_image, get_extension_from_url


def fetch_spacex_launch(launch_id="latest"):
    os.makedirs(os.path.dirname("images/spacex/"), exist_ok=True)

    url = f"https://api.spacexdata.com/v4/launches/{launch_id}"

    response = requests.get(url)
    response.raise_for_status()

    images = response.json()["links"]["flickr"]["original"]

    for image_index, image_url in enumerate(images, 1):
        image_extension = get_extension_from_url(image_url)

        download_image(
            image_url,
            f"images/spacex/spacex_{image_index}{image_extension}"
        )
