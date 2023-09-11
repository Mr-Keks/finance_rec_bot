from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# general buttons
record_start_button = KeyboardButton(text="Запис")
skip_button = KeyboardButton(text="Пропустити")
edit_button = KeyboardButton(text="Редагувати")
save_record_button = KeyboardButton(text="Зберегти")

record_start_button_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            record_start_button,
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True   
)

skip_button_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            skip_button,            
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

edit_button_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            edit_button,
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

save_record_button_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            edit_button,
            save_record_button,
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Головне меню")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# currency buttons
uah_button = KeyboardButton(text="Гривня")
eu_button = KeyboardButton(text="Євро")

currency_buttons_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            uah_button,
            eu_button,
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
