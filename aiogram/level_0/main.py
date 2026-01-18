import asyncio

from aiogram import Dispatcher, Router, Bot
from aiogram.fsm.storage.memory import MemoryStorage

from config import settings


async def main():
    storage = MemoryStorage()
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher(storage=storage)
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

