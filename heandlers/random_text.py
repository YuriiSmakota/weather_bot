from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text)
async def random_text(message: Message):
    await message.answer(f"\"{message.text}\" неопознанная команда.\n"
                         f"<b>{message.from_user.full_name}</b> введите /weather, что бы узнать температуру.")
