from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command("start"))
async def command_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"Добро пожаловать в сервис <b>Weather Wiz</b>.\n"
                         f"Что бы узнать температуру в городе, введите команду /weather")

