from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text)
async def random_text(message: Message):
    await message.answer(f"Неопознанная команда. Для начала, \n"
                         f"введите /weather, что бы узнать температуру в городе.")
