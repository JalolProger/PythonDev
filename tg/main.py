import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile, BotCommand
from aiogram.filters import Command


from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_cmd(msg: Message):
    is_premium = getattr(msg.from_user, "is_premium", False)
    if is_premium:
        await msg.reply("Zursiz")
    else:
        await msg.reply("Pas odamsiz")
        await msg.answer(f"{msg}")


async def menu_btn():
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="help", description="Yordam"),
        BotCommand(command="settings", description="Sozlash uchun"),
        BotCommand(command="photo", description="Rasm junatish"),
        BotCommand(command="video", description="Video junatish"),
        BotCommand(command="document", description="Hujjat yuborish")
    ]
    await bot.set_my_commands(commands)


@dp.message(Command("video"))
async def video_cmd(msg: Message):
    yonalish = "C:/Users/USER/Desktop/tg-bot/videos/mars.mp4"
    video = FSInputFile(yonalish)
    await msg.answer_video(video, caption="Mana video")


@dp.message(Command("photo"))
async def photo_cmd(msg: Message):
    yonalish = "C:/Users/USER/Desktop/tg-bot/images/mars.jpg"
    photo = FSInputFile(yonalish)
    await msg.answer_photo(photo, caption="Mana rasm")


@dp.message(Command("document"))
async def document_cmd(msg: Message):
    yonalish = "C:/Users/USER/Desktop/tg-bot/documents/mars.pdf"
    document = FSInputFile(yonalish)
    await msg.answer_document(document, caption="Mana hujjat")

@dp.message(Command("music"))
async def music_cmd(msg: Message):
    yonalish = "C:/Users/USER/Desktop/tg-bot/music/mars"


@dp.message()
async def echo(message: Message):
    await message.answer(message.text)


async def start():
    await menu_btn()
    await dp.start_polling(bot)


if __name__ == '__main__':
    print("Bot has been started")
    asyncio.run(start())

