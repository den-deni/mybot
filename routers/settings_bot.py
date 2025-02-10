from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hblockquote, hbold

from state.bot_state import BotState
from database.model import Database


settings_router = Router()
db = Database()


@settings_router.message(Command('settings'))
async def get_settings(message: Message):
    await message.answer(text=f"{hblockquote('Налаштування що можна змінити?')}"
                         f"{hbold('Змінити поточне місто для погоди /city')}\n"
                         f"{hbold('Додати свою монету в курс /coins')}\n"
                        )


@settings_router.message(Command('city'))
async def set_city(message: Message):
    city = message.text.split()
    if len(city) > 1:
        city = ' '.join(city[1:])
        await db.update_user(message.from_user.id, city=city)
        await message.answer(text=f"Місто змінено на {city}")
    else:
        await message.reply(text="Команда /city повинна використовуватися з аргументом. Наприклад: /city London")


@settings_router.message(Command('coins'))
async def set_coins(message: Message):
    coins = message.text.split()
    if len(coins) > 1:
        coins = ' '.join(coins[1:]).upper()
        await db.update_user(message.from_user.id, coins=coins)
        await message.answer(text=f"Монета змінено на {coins}")
    else:
        await message.reply(text="Команда /coins повинна використовуватися з аргументом. Наприклад: /coins BTC")