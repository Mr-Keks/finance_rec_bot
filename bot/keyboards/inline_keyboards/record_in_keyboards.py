from aiogram.utils.keyboard import InlineKeyboardBuilder
import json


def read_categories():
    with open("data/categories.json", 'r') as file:
        categories_data = json.load(file)
    return categories_data

categories = read_categories()

def create_category_keyboard():
    category_keyboard = InlineKeyboardBuilder()
    
    # range of categories per page
 
    categories_data = list(categories["categories"].values())
    
    for category_button in categories_data:
        category_keyboard.button(text=category_button, callback_data=f"category_selected_{str(category_button)}")
    
    return category_keyboard
