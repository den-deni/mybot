import secrets
import asyncio
import logging
import sys

from cryptography.fernet import Fernet

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config.setting import Config
from commands.list_cmd import admin, private, group
from routers.today import data_router
from routers.app import app_router
from routers.settings_bot import settings_router
from routers.tts import tts_router
from routers.youtube import youtube_router
from routers.encrypter import chiper_router
from database.model import Database
from text_templates import helper

dp = Dispatcher()
db = Database()


routers = [data_router, app_router, settings_router, tts_router, youtube_router, chiper_router]

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await db.create_table()
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    chipr_key = Fernet.generate_key().decode()
    token = secrets.token_hex(16)
    await db.add_data(user_id, user_name, chipr_key, token)
    await message.answer(helper.HELP_TEXT)



async def main() -> None:
    token = Config.BOT_TOKEN
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(*routers)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=group, scope=types.BotCommandScopeAllChatAdministrators())
    await bot.set_my_commands(commands=admin, scope=types.BotCommandScopeChat(chat_id=Config.ADMIN))
    await dp.start_polling(bot)



logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)



if __name__ == "__main__":
    logging.info("Bot started")
    asyncio.run(main())