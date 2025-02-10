import secrets

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold, hblockquote, hpre, hitalic, hcode

from cryptography.fernet import Fernet


from database.model import Database

app_router = Router()
db = Database()

@app_router.message(Command("encoder"))
async def get_app(message: Message):
    user_id = message.from_user.id
    user_data = await db.get_data(tg_id=user_id)

    # Если данные уже есть, просто отправляем приветственное сообщение
    if user_data and user_data.get('chipr_key') and user_data.get('token'):
        await message.answer()
    else:
        # Если данных нет, создаем новые ключи
        chipr_key = Fernet.generate_key().decode()
        token = secrets.token_hex(16)

        await db.add_keys(user_id, chiprkey=chipr_key, token=token)
        await message.answer(
            text=f"{hblockquote('Що робить Encoder')}\n\n"
                 f"Додаток дозволяє {hitalic('зашифровувати текстову інформацію')}, щоб зробити її недоступною для сторонніх.\n\n"
                 f"{hbold('Як це працює?')}\n"
                 f"{hcode('Ти можеш шифрувати повідомлення без необхідності вводити ключ.')}\n"
                 f"🔑 Ключ потрібен лише тим, кому ти передаєш зашифровані дані.\n\n"
                 f"🛡 Твій ключ:\n{hpre(token)}")


@app_router.message(Command("token"))
async def get_token(message: Message):
    user_id = message.from_user.id
    user_data = await db.get_data(tg_id=user_id)

    if user_data and user_data.get('chipr_key') and user_data.get('token'):
        key = user_data.get('token')
        await message.answer(text=f"{hpre(key)}")
    else:
        await message.reply(text="Ти не маєш доступу до даного додатку.")