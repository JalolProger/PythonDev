import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from config import API_TOKEN
from default_btn import menu
from inline_btn import inline_btn

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(msg: Message):
    await msg.answer("Buyurtmani birga joylashtiramizmi? 🤗", reply_markup=menu)


@dp.message()
async def cmd_message(msg: Message):
    if msg.text == "⬅️Asosiy Menu":
        await msg.delete(message=msg)
        await msg.answer("Quyidagilardan birini tanlang", reply_markup=inline_btn)
    else:
        await msg.answer("Notanish so'z!")

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot ishladi....")
    asyncio.run(main())