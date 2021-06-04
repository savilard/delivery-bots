from aiogram.types import CallbackQuery

from delivery_bots.api.moltin.cart.schemas import CartProduct
from delivery_bots.bots.tgbot.cart.keyboards import create_cart_keyboard


async def display_cart(
    query: CallbackQuery,
    cart_products: list[CartProduct],
    cart_total_amount: str,
) -> None:
    """Sends message with Moltin cart content."""
    message_text = [
        '{name}\n{description}\n{quantity} пицц в корзине на сумму {amount}\n\n'.format(
            name=cart_product.name,
            description=cart_product.description,
            quantity=cart_product.quantity,
            amount=cart_product.meta.display_price.with_tax.value.formatted,  # noqa: WPS219
        )
        for cart_product in cart_products
    ]
    message_text.append(f'К оплате {cart_total_amount}')
    await query.message.answer(
        text=''.join(message_text),
        reply_markup=await create_cart_keyboard(cart_products),
    )
