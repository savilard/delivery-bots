from aiogram.types import InlineKeyboardButton
from aiogram.utils.emoji import emojize


async def create_checkout_button() -> InlineKeyboardButton:
    """Create tgbot checkout button."""
    return InlineKeyboardButton(
        text=emojize('💱 Оформить заказ'),
        callback_data='checkout',
    )
