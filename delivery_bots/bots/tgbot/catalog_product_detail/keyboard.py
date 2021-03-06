from aiogram.types import InlineKeyboardMarkup

from delivery_bots.bots.tgbot.cart.buttons import (
    create_add_product_to_cart_button,
    create_cart_button,
)
from delivery_bots.bots.tgbot.menu.buttons import create_menu_button


async def create_catalog_product_detail_keyboard() -> InlineKeyboardMarkup:
    """The function collects a keyboard for product description."""
    cart_button = await create_cart_button()
    add_product_to_cart_button = await create_add_product_to_cart_button()

    keyboard = [
        [add_product_to_cart_button],
        [cart_button],
        [await create_menu_button()],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
