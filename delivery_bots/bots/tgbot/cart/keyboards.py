from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from delivery_bots.api.moltin.cart.schemas import CartProduct
from delivery_bots.bots.tgbot.checkout.buttons import create_checkout_button
from delivery_bots.bots.tgbot.menu.buttons import create_menu_button


async def create_cart_keyboard(cart_products: list[CartProduct]) -> InlineKeyboardMarkup:
    """The function collects a keyboard for cart."""
    keyboard = [
        [InlineKeyboardButton(f'Удалить из корзины "{cart_product.name}"', callback_data=cart_product.id)]
        for cart_product in cart_products
    ]
    keyboard.append([await create_checkout_button()])
    keyboard.append([await create_menu_button()])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
