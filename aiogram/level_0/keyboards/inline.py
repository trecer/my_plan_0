from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_kb_approve = InlineKeyboardMurkup(inline_keyboard=[[InlineKeyboardButton(text="Подтвердить", callback_data="fill_out_form")],
                                                          [InlineKeyboardButton(text="Отменить", callback_data="cancel_fill_out_form")]])
