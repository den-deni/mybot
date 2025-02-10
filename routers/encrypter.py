import logging

from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.markdown import hbold, hpre
from aiogram.fsm.context import FSMContext

from utils.chiper import Encrypter
from database.model import Database
from state.bot_state import BotState

chiper_router = Router()
en = Encrypter()
db = Database()


@chiper_router.message(Command('encrypt'))
async def encrypt_text(message: Message):
    try:
        user_id = message.from_user.id
        data = await db.get_data(tg_id=user_id)
        token = data.get("chipr_key")
        text = message.text.split(maxsplit=1)
        if len(text) > 1:
            text = text[1]
            encrypted_text = en.encrypt(text, token)
            await message.answer(text=f"{hbold('Зашифроване повідомлення:')}\n"
                                 f"{hpre(encrypted_text)}\n"
                                 )
        else:
            await message.reply(text="Команда /encrypt повинна використовуватися з аргументом. Наприклад: /encrypt Привіт світ")

    except Exception:
        await message.reply("Помилка при виконанні запиту. Спробуй пізніше.")


@chiper_router.message(Command('decrypt'))
async def decrypt_text(message: Message):
    try:
        user_id = message.from_user.id
        data = await db.get_data(tg_id=user_id)
        token = data.get("chipr_key")
        text = message.text.split(maxsplit=1)
        if len(text) > 1:
            text = text[1]
            decrypted_text = en.decrypt(text, token)
            await message.answer(text=f"{hbold('Розшифроване повідомлення:')}\n"
                                 f"{hpre(decrypted_text)}\n"
                                 )
        else:
            await message.reply(text="Команда /decrypt повинна використовуватися з аргументом. Наприклад: /decrypt U2FsdGVkX1_n7Y6L46X6Xw_...")

    except Exception:
        await message.reply(f"Помилка при виконанні запиту. Спробуй пізніше.")


@chiper_router.message(Command('textX'))
async def decrypt_with_token(message: Message, state: FSMContext):
    await message.answer(text=f"{hbold('Відправ мені ключ')}")
    await state.set_state(BotState.token)


@chiper_router.message(BotState.token)
async def handle_token(message: Message, state: FSMContext):
    try:
        token = message.text
        data = await db.check_user_token(user_token=token)
        if data is False:
            await message.answer(text=f"{hbold('Ключ не знайдено')}!")
            return
        else:
            await state.update_data(token=message.text)
            await message.answer(text=f"{hbold('Ок тепер відправ текст на розшифруваня')}")
            await state.set_state(BotState.text)
    except Exception:
        await message.reply("Помилка при виконанні запиту. Спробуй пізніше.")



@chiper_router.message(BotState.text)
async def handle_text(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        token = data.get('token')
        chipr_key = await db.get_key(token=token)
        text = message.text
        decrypted_text = en.decrypt_user_key(encrypted_text=text, user_key=chipr_key)
        await message.answer(text=f"{hbold('Розшифроване повідомлення:')}\n"
                                 f"{hpre(decrypted_text)}\n"
                                 )
        await state.clear()
    except Exception:
        await message.reply("Помилка при виконанні запиту. Спробуй пізніше.(Мабуть не вірний шифр 😕)")


