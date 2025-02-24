from aiogram.fsm.state import State, StatesGroup


class RegisterState(StatesGroup):
    first_name = State()
    last_name = State()
    age = State()
    email = State()
    phone_number = State()
    location = State()