import os
import requests
import datetime
from utils import download_image, get_extension_from_url


def fetch_nasa_apod(api_key, count=15):
    os.makedirs(os.path.dirname("images/nasa_apod/"), exist_ok=True)

    params = {
      "api_key": api_key,
      "count": count,
      "thumbs": True,
    }
    response = requests.get(
        "https://api.nasa.gov/planetary/apod",
        params=params
    )
    response.raise_for_status()

    images_data = response.json()

    for image_index, image_data in enumerate(images_data, 1):
        url = image_data["url"]


        if image_data["media_type"] == "video":
            url = image_data["thumbnail_url"]

        image_extension = get_extension_from_url(url)

        download_image(
            url,
            path_to_save=f"images/nasa_apod/nasa_{image_index}{image_extension}"
        )


def fetch_nasa_epic(api_key, max_count=5):
    os.makedirs(os.path.dirname("images/nasa_epic/"), exist_ok=True)

    params = {
      "api_key": api_key,
    }
    response = requests.get(
        "https://api.nasa.gov/EPIC/api/natural",
        params=params
    )
    response.raise_for_status()

    images_data = response.json()[:max_count]

    for image_index, image_data in enumerate(images_data, 1):
        image_date = datetime.datetime.fromisoformat(image_data["date"])
        image_id = image_data["identifier"]
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date.strftime('%Y/%m/%d')}/png/epic_1b_{image_id}.png"

        image_url_params = {
          "api_key": api_key
        }

        download_image(
            image_url,
            f"images/nasa_epic/epic_{image_index}.png",
            params=image_url_params
        )
