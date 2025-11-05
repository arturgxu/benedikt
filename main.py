import asyncio
import logging
from aiogram import Bot, Dispatcher

from core.logger import setup_logger
from core.config import BOT_TOKEN
from handlers import commands
from handlers import chat

setup_logger()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    """
    The entry point of the bot. This is where handlers are registered and polling starts.
    """
    logging.info("Benedikt gets in touch!")

    dp.include_router(commands.router)
    dp.include_router(chat.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Benedikt steps into the shadows...")