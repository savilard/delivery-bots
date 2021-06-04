from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from delivery_bots.api.moltin.cart.schemas import CartProduct
from delivery_bots.bots.tgbot.common.keyboard_buttons import SHOW_MENU_BUTTON


async def create_cart_keyboard(cart_products: list[CartProduct]) -> InlineKeyboardMarkup:
    """The function collects a keyboard for cart."""
    keyboard = [
        [InlineKeyboardButton(f'Удалить из корзины "{cart_product.name}"', callback_data=cart_product.id)]
        for cart_product in cart_products
    ]
    keyboard.append([SHOW_MENU_BUTTON])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
