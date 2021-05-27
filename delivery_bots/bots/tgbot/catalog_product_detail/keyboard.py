from aiogram.types import InlineKeyboardMarkup

from delivery_bots.bots.tgbot.common.keyboard_buttons import (
    CART_BUTTON,
    SHOW_MENU_BUTTON,
)


async def create_catalog_product_detail_keyboard() -> InlineKeyboardMarkup:
    """The function collects a keyboard for product description."""
    keyboard = [
        [CART_BUTTON],
        [SHOW_MENU_BUTTON],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
