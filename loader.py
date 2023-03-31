import os
from aiogram import Dispatcher, Bot


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)