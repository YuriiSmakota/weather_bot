from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command

router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(f"Добро пожаловать в сервис <b>Weather Wiz</b>.\n"
                         f"Что бы узнать температуру, введите команду /weather")

