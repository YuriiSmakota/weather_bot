from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import Command
from parsers.request_weather import get_temp

router = Router()


@router.message(Command("weather"))
async def weather_command(message: Message):
    await message.answer(get_temp())
