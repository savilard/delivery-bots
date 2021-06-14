from aiogram.types import CallbackQuery

from delivery_bots.api.moltin.cart.cart import (
    fetch_cart_response,
    get_cart_products,
    parse_cart_products_response,
)
from delivery_bots.api.moltin.cart.cart_schemas import Cart
from delivery_bots.bots.tgbot.cart.messages import (
    display_cart,
    make_cart_content_message,
)
from delivery_bots.bots.tgbot.common.messages import delete_previous_message
from delivery_bots.bots.tgbot.states import BotState


async def go_to_cart(query: CallbackQuery) -> None:
    """Goes to the cart."""
    cart_products_response = await get_cart_products(cart_id=query.from_user.id)
    cart_products = await parse_cart_products_response(cart_products_response)
    cart_response = await fetch_cart_response(cart_id=query.from_user.id)
    cart = Cart(**cart_response.json())
    cart_content_message = await make_cart_content_message(
        cart_products=cart_products,
        cart_total_amount=cart.data.meta.display_price.with_tax.formatted,  # noqa: WPS219
    )
    await display_cart(
        query=query,
        cart_products=cart_products,
        message_text=cart_content_message,
    )
    await delete_previous_message(query)
    await BotState.cart.set()
