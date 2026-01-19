from aiogram import Router, F
from aiogram.types import CallBackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import or_f


from .keyboards.inline import inline_kb_fill_out_form

router = Router()


# router.message.filter(not F.from_user.id.in_({users_ids})
# router.callback_query.filter(not F.from_user.id.in_({users_ids})


@router.message(Form.waiting_first_name)
async def handle_first_name(message: Message, state: FSMContext):
  text = "Введите своё имя:"
  await message.answer(text)
  await state.set_state(Form.waiting_age)


@router.message(Form.waiting_age)
async def handle_age(message: Message, state: FSMContext):
  text = "Введите свою дату рождения:"
  await message.answer(text)
  await state.update_data(first_name=message.text)
  await state.set_state(Form.waiting_city)

@router.message(Form.waiting_city)
async def handle_city(message: Message, state: FSMContext):
  text = "Введите свой город:"
  await message.answer(text)
  await state.update_data(city=message.text)
  await state.set_state(Form.waiting_city)

  text = "Проверьте данные и выберите решение:\n- Отмена - заполнить сначала;\n- Подтвердить - сохранить введенные данные"
  await message.await(text, reply_markup=inline_kb_fill_out_form)


@router.callback_query(f_or(F.data == "fill_out_form", F.data == "cancel_fill_out_form"))
async def cb_choice_fill_out_form(callback_query: CallBackQuery, state: FSMContext):
  callback_query.await()
  text = "Заполнение формы завершено" if callback_query.data == "fill_out_form" else "Вы отменили заполнение формы. Вы можете сначала заполнить форму" 
  await state.set_state(None) if F.data != "cancel_fill_out_form" else await state.finale()
  await callback_query.message.edit_text(text, reply_markup=None)
  

