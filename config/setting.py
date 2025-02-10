from os import getenv

from dotenv import load_dotenv
load_dotenv()


class Config:
    BOT_TOKEN = getenv('TOKEN')
    ADMIN = getenv('ADMIN_ID')
    CHANEL_ID = getenv('CHANEL_ID')
    WEATHER_KEY = getenv('WEATHER_KEY')
    URL_APP = getenv('URL_APP')