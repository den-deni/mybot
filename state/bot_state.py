from aiogram.fsm.state import StatesGroup, State


class BotState(StatesGroup):
    youtube = State()
    city = State()
    coins = State()
    token = State()
    text = State()