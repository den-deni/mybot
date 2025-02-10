from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from utils.weather import get_default_weather, custom_weather
from utils.crypto_data import default_price, custom_price
from database.model import Database
from utils.currency import get_currency


data_router = Router()
db = Database()


@data_router.message(Command("today"))
async def get_weather(message: Message):
    user_id = message.from_user.id
    status = await db.check_status(user_id)
    if status == 'default':
        currency = get_currency()
        weather = get_default_weather()
        crypto_price = default_price()
        await message.answer(f"☀️Погода:\n{weather}\n\n🟠BTC-USDT: {crypto_price}\n\n"
                             f"🟢USD:{currency.get('usdbuy')}\n"
                             f"🔵EUR:{currency.get('eurbuy')}\n"
                             )
    else:
        data = await db.get_data(user_id)
        city = data.get("city")
        coins = data.get("coins") + "-USDT"
        weather = custom_weather(city)
        def_crypto = default_price()
        coins_cus = custom_price(coins)
        currency = get_currency()
        await message.answer(f"☀️Погода\n{weather}\n\n🟠BTC-USDT: {def_crypto}\n🟡{coins}: {coins_cus}\n\n"
                             f"🟢USD:{currency.get('usdbuy')}\n"
                             f"🔵EUR:{currency.get('eurbuy')}\n"
                             )
