from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from bot.keyboards.reply_keyboards.record_keyboards import record_start_button_markup

start = Router()

@start.message(CommandStart())
async def start_bot(message: types.Message, state: FSMContext):
    await message.answer("Початок роботи бота...")
    await message.answer("Для початку роботи настисність 'Запис'", reply_markup=record_start_button_markup)