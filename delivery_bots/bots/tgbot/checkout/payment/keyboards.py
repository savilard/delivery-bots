from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def create_payment_keyboard() -> InlineKeyboardMarkup:
    """Creates payment keyboard."""
    keyboard = [
        [
            InlineKeyboardButton(
                text='💳 Оплатить',
                callback_data='payment',
            ),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
