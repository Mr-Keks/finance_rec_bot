import json
import os

from aiogram import types, F, Router
from typing import Any, Dict
from aiogram.fsm.context import FSMContext

from datetime import datetime

from bot.keyboards.inline_keyboards.record_in_keyboards import create_category_keyboard
from bot.keyboards.reply_keyboards.record_keyboards import skip_button_markup, save_record_button_markup, currency_buttons_markup, record_start_button_markup, main_menu
from bot.states.record_state import RecordState


record_router = Router()

@record_router.message(F.text == "Головне меню")
async def menu(message: types.Message, state: FSMContext):
    await message.answer("Ви у головному меню", reply_markup=record_start_button_markup)

@record_router.message(F.text == "Запис")
async def choose_category(message: types.Message, state:FSMContext):
    await state.set_state(RecordState.CATEGORY)
    await message.answer("Виберіть категорію", reply_markup=create_category_keyboard().as_markup())
    
@record_router.callback_query(RecordState.CATEGORY, F.data.startswith("category_selected_"))
async def category(query: types.CallbackQuery, state: FSMContext):
    await state.update_data(category=query.data.split("category_selected_")[1])
    await state.set_state(RecordState.ADITIONAL_DESCRIPTION)
    await query.message.answer("Додатковий опис", reply_markup=skip_button_markup)

@record_router.message(RecordState.ADITIONAL_DESCRIPTION)
async def add_desc(message: types.Message, state: FSMContext):
    user_answ = message.text

    if user_answ == "Пропустити":
        user_answ = ""
    await state.set_state(RecordState.COST)
    await state.update_data(add_desc=user_answ)
    await message.answer("Введіть суму:")

@record_router.message(RecordState.COST)
async def cost(message: types.Message, state: FSMContext):
    await state.update_data(cost=message.text)
    await state.set_state(RecordState.CURRENCY)
    await message.answer("Виберіть валюту", reply_markup=currency_buttons_markup)

@record_router.message(RecordState.CURRENCY)
async def cost_and_confirmation(message: types.Message, state: FSMContext):
    data = await state.update_data(currency=message.text)
    
    answer = f"""
    Ваш запис\n
    Категорія: {data["category"]},
    Опис: {data["add_desc"]},
    Сума: {data["cost"]},
    Валюта: {data["currency"]}
    """
    await state.set_state(RecordState.CONFIRMATION)
    await message.answer(answer)
    await message.answer("Щоб зберегти натисніть кнопку", reply_markup=save_record_button_markup)

@record_router.message(F.text == "Зберегти", RecordState.CONFIRMATION)
async def confirmation(message: types.Message, state: FSMContext):
    data = await state.get_data()

    await state.clear()

    await saving(message=message, data=data)

async def saving(message: types.Message, data: Dict[str, Any], state=FSMContext):
    user = message.from_user.id

    if data["currency"] == "Гривня":
        data["currency"] = "uah"
    elif data["currency"] == "Євро":
        data["currency"] = "eu"
        
    file_name = datetime.today().date().__str__()
    try:
        if not os.path.exists(f"{file_name}.json"):
            with open(f"{file_name}.json", "w", encoding='utf-8') as json_file:
                base_structure = {
                    file_name: []
                }
                json.dump(base_structure, json_file, indent=4)

        with open(f"{file_name}.json", "r", encoding='utf-8') as file:
            existing_data = json.load(file)

        with open(f"{file_name}.json", "w", encoding='utf-8') as file:
            existing_data[file_name].append(data)
            json.dump(existing_data, file, indent=4)
            
        
        await message.answer("Дані збережено", reply_markup=main_menu)
    except Exception as ex:
        await message.answer("Сталася якась помилка :/")
        print(ex)