from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from delivery_bots.api.moltin.cart.schemas import CartProduct


async def create_cart_keyboard(cart_products: list[CartProduct]) -> InlineKeyboardMarkup:
    """The function collects a keyboard for cart."""
    keyboard = [
        [InlineKeyboardButton(f'Удалить из корзины "{cart_product.name}"', callback_data=cart_product.id)]
        for cart_product in cart_products
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
