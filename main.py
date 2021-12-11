import os
import time
from dotenv import load_dotenv
import telegram

from fetch_nasa import fetch_nasa_apod, fetch_nasa_epic
from fetch_spacex import fetch_spacex_launch


def main():
    load_dotenv()
    tg_api_key = os.getenv("TG_API_KEY")
    tg_channel_id = os.getenv("TG_CHANNEL_ID")
    nasa_api_key = os.getenv("NASA_API_KEY")
    upload_interval = int(os.getenv("UPLOAD_INTERVAL")) or 86400

    bot = telegram.Bot(token=tg_api_key)

    while True:
        fetch_spacex_launch("5eb87ce4ffd86e000604b337")
        fetch_nasa_apod(nasa_api_key)
        fetch_nasa_epic(nasa_api_key)

        for filename in os.listdir("images"):
            if not os.path.isdir(os.path.join("images", filename)):
                continue
            
            images_folder = os.path.join("images", filename)

            for image_name in os.listdir(images_folder):
                image_path = os.path.join(images_folder, image_name)
                
                with open(image_path, "rb") as image:
                    bot.send_photo(chat_id=tg_channel_id, photo=image, timeout=600)
                
                time.sleep(upload_interval)


if __name__ == "__main__":
    main()
