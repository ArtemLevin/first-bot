from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_start = KeyboardButton(text='/start')
btn_help = KeyboardButton(text='/help')
btn_rescueHelp = KeyboardButton(text='Срочно')
btn_location = KeyboardButton(text='Ваша позиция', request_location=True)
btn_phone = KeyboardButton(text='Ваш телефон', request_phone=True)

kb_main.add(btn_start, btn_help)
kb_main.add(btn_rescueHelp)
kb_main.add(btn_location, btn_phone)
