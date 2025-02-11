from aiogram.types import BotCommand

admin = [
    BotCommand(command='start', description='Запуск бота'),
    BotCommand(command='insta', description='Отримати дані з Instagram'),
    BotCommand(command='youtube', description='Завантажити музику'),
    BotCommand(command='today', description='Що сьогодні'),
    BotCommand(command='admin', description='admin panel'),
    BotCommand(command='tts', description='Текст в голос'),
    BotCommand(command='token', description='Показати ключ'),
    BotCommand(command='settings', description='Налаштування')
]

private = [
    BotCommand(command='start', description='Запустити перезапустити бот'),
    BotCommand(command='music', description='Завантажити музику YoutubeMusic'),
    BotCommand(command='today', description='Що сьогодні'),
    BotCommand(command='token', description='Показати ключ'),
    BotCommand(command='tts', description='Текст в голос'),
    BotCommand(command='settings', description='Налаштування'),
    BotCommand(command='help', description='Довідка')
]

group = [
    BotCommand(command='mute', description='Замутити користувача'),
    BotCommand(command='ban', description='Забанити користувача')
]