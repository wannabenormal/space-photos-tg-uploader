# Space Telegram

This script collecting photos from NASA APOD & EPIC, SpaceX launches and upload them to Telegram channel via bot.

### How to install

1. You need to create `.env` file
2. Get [api-key](https://api.nasa.gov/#signUp) for NASA
3. Create bot in [Telegram](https://core.telegram.org/bots) and get api-key
4. Create a channel in Telegram and set your bot as administrator
5. Add information in `.env`:
```
NASA_API_KEY="YOUR NASA API-KEY"
TG_API_KEY="YOUR BOT API-KEY"
TG_CHANNEL_ID="@your_channel_id"
UPLOAD_INTERVAL=SCRIPT RUNNING INTERVAL IN SECONDS
```
By default UPLOAD_INTERVAL is setted to 1 day.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

6. Run the script with `python` or `python3`:
```
python main.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).