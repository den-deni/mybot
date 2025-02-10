import requests
from config.setting import Config


code_to_smile = {
            "Clear": "Ясно ☀️",
            "Clouds": "Хмарно ☁️",
            "Rain": "Дощ 🌧",
            "Drizzle": "Дощик 🌦",
            "Thunderstorm": "Гроза ⛈",
            "Snow": "Сніг ❄️",
            "Mist": "Туман 😶‍🌫️"
        }


def get_default_weather(city='Kiev'):
    key = Config.WEATHER_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang={'ua'}&appid={key}&units=metric"
    response = requests.get(url)
    data = response.json()
    main = data['weather'][0]['main']
    if main in code_to_smile:
        wd = code_to_smile[main]
    name_country = data['sys']['country']
    name_city = data['name']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    temp = data['main']['temp']
    feels = data['main']['feels_like']

    weather_text = f"Місто {name_city}\n"
    weather_text += f"Країна {name_country}\n"
    weather_text += f"{main} {wd}\n"
    weather_text += f"Температура повітря {temp}°C\n"
    weather_text += f"Відчувається як {feels}°C\n"
    weather_text += f"Швидкість вітру {wind}м/с\n"
    weather_text += f"Вологість повітря {humidity}%"
    return weather_text

def custom_weather(city):
    try:
        key = Config.WEATHER_KEY
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang={'ua'}&appid={key}&units=metric"
        response = requests.get(url)
        data = response.json()
        main = data['weather'][0]['main']
        if main in code_to_smile:
            wd = code_to_smile[main]
        name_country = data['sys']['country']
        name_city = data['name']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        temp = data['main']['temp']
        feels = data['main']['feels_like']

        weather_text = f"Місто {name_city}\n"
        weather_text += f"Країна {name_country}\n"
        weather_text += f"{main} {wd}\n"
        weather_text += f"Температура повітря {temp}°C\n"
        weather_text += f"Відчувається як {feels}°C\n"
        weather_text += f"Вологість повітря {humidity}%"
        return weather_text
    except KeyError:
        return f"Невірна назва міста"
