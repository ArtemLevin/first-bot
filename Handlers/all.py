from loader import dp
from aiogram.types import Message

@dp.message_handler()
async def start_command(message: Message):
    await message.answer(f"{message.from_user.first_name}, хороший вопрос. Надо подумать")