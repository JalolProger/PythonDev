from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

msg_router = Router()


@msg_router.message()
async def start_cmd(msg: Message)
    user_txt = msg.text
    await msg.reply(user_txt)