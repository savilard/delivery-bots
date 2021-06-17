import ujson
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from delivery_bots.api.moltin.cart.cart import (
    fetch_cart_response,
    get_cart_products,
    parse_cart_products_response,
)
from delivery_bots.api.moltin.cart.cart_schemas import Cart
from delivery_bots.api.moltin.entry.schemas import Entry
from delivery_bots.bots.tgbot.cart.messages import make_cart_content_message
from delivery_bots.bots.tgbot.checkout.delivery_man.keyboards import (
    create_deliverer_keyboard,
)
from delivery_bots.bots.tgbot.checkout.payment.keyboards import create_payment_keyboard
from delivery_bots.bots.tgbot.states import BotState


async def handle_delivery(query: CallbackQuery, state: FSMContext):  # noqa: WPS210
    """Handler for BotState.delivery state."""
    current_state = await state.get_data()
    nearest_pizzeria = Entry(**ujson.loads(current_state['nearest_pizzeria']))

    if query.data == 'pickup':
        message = (
            f'Отлично! Вы можете забрать заказ в ближайшей пиццерии "{nearest_pizzeria.alias}"'
            + f', которая расположена по адресу: {nearest_pizzeria.address}.'
        )
        await query.message.answer(text=message)

    elif query.data == 'delivery':
        cart_products_response = await get_cart_products(cart_id=query.from_user.id)
        cart_products = await parse_cart_products_response(cart_products_response)
        cart_response = await fetch_cart_response(cart_id=query.from_user.id)
        cart = Cart(**cart_response.json())
        cart_content_message = await make_cart_content_message(
            cart_products=cart_products,
            cart_total_amount=cart.data.meta.display_price.with_tax.formatted,  # noqa: WPS219
        )
        await query.message.answer(
            text='Ваш заказ успешно оформлен! Оплатите его картой через телеграм.',
            reply_markup=await create_payment_keyboard(),
        )
        await query.message.bot.send_message(
            chat_id=nearest_pizzeria.deliveryman_tg_id,
            text=cart_content_message,
        )
        await query.message.bot.send_location(
            chat_id=nearest_pizzeria.deliveryman_tg_id,
            latitude=current_state['customer_lat'],
            longitude=current_state['customer_lon'],
            reply_markup=await create_deliverer_keyboard(
                button_text='Взять заказ',
                callback_action='take_order',
                customer_tg_id=query.from_user.id,
            ),
        )


def register_handler_delivery(dp: Dispatcher):
    """Register cart handler."""
    dp.register_callback_query_handler(handle_delivery, state=BotState.delivery)
