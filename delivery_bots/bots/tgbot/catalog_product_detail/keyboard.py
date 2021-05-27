from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.emoji import emojize

from delivery_bots.bots.tgbot.common.keyboard_buttons import (
    CART_BUTTON,
    SHOW_MENU_BUTTON,
)

ADD_TO_CART_BUTTON = InlineKeyboardButton(
    text=emojize('➕ Добавить в корзину'),
    callback_data='add_to_cart',
)


async def create_catalog_product_detail_keyboard() -> InlineKeyboardMarkup:
    """The function collects a keyboard for product description."""
    keyboard = [
        [ADD_TO_CART_BUTTON],
        [CART_BUTTON],
        [SHOW_MENU_BUTTON],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
