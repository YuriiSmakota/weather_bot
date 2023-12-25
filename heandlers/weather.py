from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from parsers.request_weather import get_temp
from heandlers.city_input import InputCity

router = Router()


@router.message(Command("weather"))
async def command_weather(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(InputCity.input_city)
    await message.answer(f"Введите город: ")


@router.message(InputCity.input_city)
async def city_input(message: Message):

    city = message.text
    await message.answer(get_temp(city))

