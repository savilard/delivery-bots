from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from delivery_bots.api.moltin.cart.cart_schemas import Cart
from delivery_bots.api.moltin.cart.schemas import CartProduct
from delivery_bots.bots.tgbot.cart.keyboards import create_cart_keyboard


async def make_cart_content_message(cart_products: list[CartProduct], cart: Cart, state: FSMContext) -> str:
    """Makes cart content message."""
    message_text = [
        '{name}\n{description}\n{quantity} пицц в корзине на сумму {amount}\n\n'.format(
            name=cart_product.name,
            description=cart_product.description,
            quantity=cart_product.quantity,
            amount=cart_product.meta.display_price.with_tax.value.formatted,  # noqa: WPS219
        )
        for cart_product in cart_products
    ]
    await state.update_data(order_description=''.join(message_text))

    cart_total_amount = cart.data.meta.display_price.with_tax.formatted  # noqa: WPS219
    message_text.append(f'К оплате {cart_total_amount}')

    await state.update_data(order_total_amount=cart.data.meta.display_price.with_tax.amount)  # noqa: WPS219

    return ''.join(message_text)


async def display_cart(
    query: CallbackQuery,
    cart_products: list[CartProduct],
    message_text: str,
) -> None:
    """Sends message with Moltin cart content."""
    await query.message.answer(
        text=message_text,
        reply_markup=await create_cart_keyboard(cart_products),
    )
