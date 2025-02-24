from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext
from lesson.buttons.def_btn import menu

from lesson.states.register_state import RegisterState

start_router = Router()


@start_router.message(Command("start"))
async def start_cmd(msg: Message, state: FSMContext):
    await msg.answer("Iltimos ismingizni kiriting: ")
    await state.set_state(RegisterState().first_name)


@start_router.message(RegisterState().first_name)
async def first_name(msg: Message, state: FSMContext):
    await state.update_data(first_name=msg.text)
    await msg.answer("Familiyangizni kiriting:  ")
    await state.set_state(RegisterState().last_name)


@start_router.message(RegisterState().last_name)
async def last_name(msg: Message, state: FSMContext):
    await state.update_data(last_name=msg.text)
    await msg.answer("Yosh kiriting:   ")
    await state.set_state(RegisterState().age)


@start_router.message(RegisterState().age)
async def age(msg: Message, state: FSMContext):
    await state.update_data(age=msg.text)
    await msg.answer("email kiriting:")
    await state.set_state(RegisterState().email)


@start_router.message(RegisterState().email)
async def email_cmd(msg: Message, state: FSMContext):
    await state.update_data(email=msg.text)
    await msg.answer("Telefon raqam kiriting:  ", reply_markup=menu)
    await state.set_state(RegisterState().phone_number)


@start_router.message(RegisterState().phone_number)
async def phone_number(msg: Message, state: FSMContext):
    await state.update_data(phone_number=msg.contact)
    await msg.answer("Location yuboring:   ", reply_markup=menu)


@start_router.message(RegisterState().location)
async def location_cmd(msg: Message, state: FSMContext):
    await state.update_data(location=msg.location)
