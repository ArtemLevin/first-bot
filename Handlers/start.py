from loader import dp
from aiogram.types import Message
from Keyboards import kb_main

@dp.message_handler(commands = ["start"])
async def start_command(message: Message):
    await message.answer("Кто хороший мальчик?\nАй-да гулять!", reply_markup=kb_main)

