import os

from aiogram import Bot, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from utils.yt_downloader import load_audio


youtube_router = Router()

import os
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import FSInputFile

youtube_router = Router()

@youtube_router.message(Command("music"))
async def get_musik(message: Message, bot: Bot):
    file = None  # Добавляем для предотвращения ошибок в finally

    try:
        text_parts = message.text.split(maxsplit=1)

        if len(text_parts) > 1:
            url = text_parts[1]  # Берем только ссылку

            if url.startswith("https://music"):
                file = load_audio(url=url)  # Загружаем аудио

                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

                audio = FSInputFile(path=file)
                await bot.send_audio(chat_id=message.chat.id, audio=audio)
            else:
                await message.reply(text="Невірний формат посилання. Приклад: /music https://music.youtube")
        else:
            await message.reply(text="Команда /music повинна використовуватися з аргументом. Наприклад: /music https://music.youtube")

    except Exception as e:
        await message.reply(text=f"Помилка при завантаженні аудіо: {e}")

    finally:
        if file and os.path.exists(file):  # Проверяем, что файл существует
            os.remove(file)