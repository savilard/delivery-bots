from aiogram.types import InlineKeyboardButton
from aiogram.utils.emoji import emojize


async def create_cart_button() -> InlineKeyboardButton:
    """Makes cart button."""
    return InlineKeyboardButton(
        text=emojize('🛒 Корзина'),
        callback_data='go_to_cart',
    )


async def create_add_product_to_cart_button() -> InlineKeyboardButton:
    """Makes add product to cart button."""
    return InlineKeyboardButton(
        text=emojize('➕ Добавить в корзину'),
        callback_data='add_to_cart',
    )
