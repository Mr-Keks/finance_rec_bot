from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
import json


def read_categories():
    with open("data/categories.json", 'r') as file:
        categories_data = json.load(file)
    return categories_data

def preparing_data():
    categories = read_categories()
    # range of categories per page
    categories_data = list(categories["categories"].values())

    # counting pages
    number_of_caterogies = len(categories_data) // 5
    if len(categories_data) % 5 != 0:
        number_of_caterogies += 1
    # split_lists = [my_list[i:i+chunk_size] for i in range(0, len(my_list), chunk_size)]
    # preparing list of data
    #data_per_page  = [categories_data[i:i+number_of_caterogies] for i in range(0, len(categories_data), number_of_caterogies*5)]
    data_per_page = []
    for i in range(number_of_caterogies):
        try:
            data_per_page.append(categories_data[0:5])
            del categories_data[0:5]
        except IndexError:
            data_per_page.append(categories_data[i:])

    return data_per_page

def create_category_keyboard(page_number, category_data=None):
    if not category_data:
        category_data = preparing_data()
    # creation category list for current page
    
    category_buttons = [
        [types.InlineKeyboardButton(
            text=category_button, 
            callback_data=f"category_selected_{str(category_button)}"
            )] for category_button in category_data[page_number-1]
    ]

  
    if page_number > 1:
        left_arrow = [types.InlineKeyboardButton(text="<=", callback_data="left")]
        category_buttons += [left_arrow]
    if page_number < len(category_data):
        right_arrow = [types.InlineKeyboardButton(text="=>", callback_data="right")]
        category_buttons += [right_arrow]
    print(category_buttons)
    category_keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=category_buttons
    )

    
    return category_keyboard
