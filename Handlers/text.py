from loader import dp
from aiogram.types import Message
from aiogram.dispatcher import filters


@dp.message_handler(text='Срочно')
async def start_command(message: Message):
    await message.answer(f"Какая срочная помощь требуется, {message.from_user.first_name}?")
