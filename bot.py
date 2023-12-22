import asyncio
import logging

from aiogram import Dispatcher, Bot
from config import config

from heandlers import command_start, command_weather


async def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s-%(name)s-%(levelname)s-%(message)s")

    bot = Bot(token=config.token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(command_start.router, command_weather.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
