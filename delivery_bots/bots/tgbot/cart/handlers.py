from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from delivery_bots.api.moltin.cart.cart import remove_product_from_cart
from delivery_bots.bots.tgbot.cart.cart import go_to_cart
from delivery_bots.bots.tgbot.menu.messages import go_to_menu
from delivery_bots.bots.tgbot.states import BotState


async def handler_cart(query: CallbackQuery, state: FSMContext):
    """Handler for Moltin cart."""
    current_state = await state.get_data()
    chunk = current_state['chunk']

    if query.data == 'go_to_menu':
        await go_to_menu(query, chunk)
        return None

    if query.data == 'checkout':
        await query.message.answer(text='Пришлите, пожалуйста, ваш email.')
        await BotState.waiting_mail.set()
        return None

    await remove_product_from_cart(cart_id=query.from_user.id, cart_product_id=query.data)
    await go_to_cart(query=query, state=state)


def register_handler_cart(dp: Dispatcher):
    """Register cart handler."""
    dp.register_callback_query_handler(handler_cart, state=BotState.cart)
