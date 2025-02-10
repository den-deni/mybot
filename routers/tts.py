import os

from aiogram import Router, Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from utils.audio_text import text_to_speech


tts_router = Router()

@tts_router.message(Command("tts"))
async def tts_msg(message: Message, bot: Bot):
    try:
        text = message.text.split(maxsplit=1)
        if len(text) > 1:
            text = ' '.join(text[1:])
            file = text_to_speech(text)
            audio = FSInputFile(path=file)
            await bot.send_audio(chat_id=message.chat.id, audio=audio)
            os.remove(file)
        else:
            await message.reply(text="Команда /tts повинна використовуватися з аргументом. Наприклад: /tts Привіт світ")

    except Exception:
        await message.reply(text="Помилка при виконанні запиту. Спробуй пізніше.")