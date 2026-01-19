from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
  waiting_first_name = State()
  waiting_age = State()
  waiting_city = State()
