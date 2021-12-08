import os
from urllib.parse import urlparse, urlsplit, unquote
import datetime
import requests
from dotenv import load_dotenv
import telegram


def download_image(url, path_to_save):
    response = requests.get(url)
    response.raise_for_status()

    os.makedirs(os.path.dirname(path_to_save), exist_ok=True)

    with open(path_to_save, "wb") as file:
        file.write(response.content)


def fetch_spacex_lauch(id="latest"):
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


def fetch_nasa_apod(api_key, count=15):
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

    for image_id, image_data in enumerate(images_data):
        url = image_data["url"]

        if image_data["media_type"] == "video":
            url = image_data["thumbnail_url"]

        image_extension = get_extension_from_url(url)

        download_image(
            url,
            f"images/nasa_apod/nasa_{image_id + 1}{image_extension}"
        )


def fetch_nasa_epic(api_key, max_count=5):
    params = {
      "api_key": api_key,
    }
    response = requests.get(
        "https://api.nasa.gov/EPIC/api/natural",
        params=params
    )
    response.raise_for_status()

    images_data = response.json()[:max_count]

    for image_number, image_data in enumerate(images_data):
        image_date = datetime.datetime.fromisoformat(image_data["date"])
        image_id = image_data["identifier"]
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date.strftime('%Y/%m/%d')}/png/epic_1b_{image_id}.png?api_key={api_key}"

        download_image(
            image_url,
            f"images/nasa_epic/epic_{image_number + 1}.png"
        )


def get_extension_from_url(url):
    parsed_url = urlparse(unquote(url))
    file_name = os.path.split(parsed_url.path)[1]

    return os.path.splitext(file_name)[1]


def main():
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    tg_api_key = os.getenv("TG_API_KEY")

    fetch_spacex_lauch("5eb87ce4ffd86e000604b337")
    fetch_nasa_apod(nasa_api_key)
    fetch_nasa_epic(nasa_api_key)

    bot = telegram.Bot(token=tg_api_key)
    bot.send_message(chat_id="@test_space_photos", text="Ping")



if __name__ == "__main__":
    main()
