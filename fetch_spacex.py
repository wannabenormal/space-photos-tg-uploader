import requests
from utils import download_image, get_extension_from_url


def fetch_spacex_launch(id="latest"):
    url = f"https://api.spacexdata.com/v4/launches/{id}"

    response = requests.get(url)
    response.raise_for_status()

    images = response.json()["links"]["flickr"]["original"]

    for image_index, image in enumerate(images):
        image_extension = get_extension_from_url(image)
        download_image(
            image,
            f"images/spacex/spacex_{image_index + 1}{image_extension}"
        )