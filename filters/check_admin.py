from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from typing import Callable, Awaitable, Dict, Any
from aiogram.exceptions import TelegramBadRequest


class Admin(BaseMiddleware):
    def __init__(self, admin_id: int):
        super().__init__()
        self.admin_id = admin_id

    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message | CallbackQuery,
                       data: Dict[str, Any]):
        user_id = event.from_user.id
        if user_id != int(self.admin_id):
            try:
                await event.answer(text='Only admin can use this command')
            except TelegramBadRequest:
                pass
            return True
        return await handler(event, data)