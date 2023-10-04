from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# general buttons
record_start_button = KeyboardButton(text="Make a record")
skip_button = KeyboardButton(text="Skip")
edit_button = KeyboardButton(text="Edit")
save_record_button = KeyboardButton(text="Save")

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
            KeyboardButton(text="Main menu")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# currency buttons
uah_button = KeyboardButton(text="UAH")
eu_button = KeyboardButton(text="EURO")

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
