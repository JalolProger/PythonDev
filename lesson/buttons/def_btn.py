from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Contact Yuborish', request_contact=True),
     KeyboardButton(text="Location", request_location=True)],
    ],
    resize_keyboard=True)