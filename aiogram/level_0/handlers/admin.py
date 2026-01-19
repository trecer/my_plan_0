from aiogram import Router
from aiogram.types import CallBackQuery
from aiogram.fsm.context import FSMContext


router = Router()


# router.message.filter(F.from_user.id.in_({admin_ids})
router.callback_query.filter(F.from_user.id.in_({admin_ids})


@router.callback_query(F.data == "get_users")
async def call_get_users(callback_query, state: FSMContext, users: list):
  await callback_query.answer()
  
  text = "Анкеты пользователей:"
  await callback_query.message.answer(text)
  
