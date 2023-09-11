from aiogram import Bot, Dispatcher, Router
from config.settings import BOT_TOKEN
from aiogram.enums import ParseMode

from bot.handlers.messages.record import record_router
from bot.handlers.start import start


# Initialization the bot and dispotcher
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
# record_router = Router()
dp = Dispatcher()
dp.include_routers(record_router, start)
