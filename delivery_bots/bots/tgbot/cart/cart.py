from aiogram.types import CallbackQuery

from delivery_bots.api.moltin.cart.cart import (
    get_cart_products,
    parse_cart_products_response,
)
from delivery_bots.bots.tgbot.cart.messages import display_cart
from delivery_bots.bots.tgbot.common.messages import delete_previous_message
from delivery_bots.bots.tgbot.states import BotState


async def go_to_cart(query: CallbackQuery) -> None:
    """Goes to the cart."""
    cart_products_response = await get_cart_products(cart_id=query.from_user.id)
    cart_products = await parse_cart_products_response(cart_products_response)
    await display_cart(query, cart_products)
    await delete_previous_message(query)
    await BotState.cart.set()
