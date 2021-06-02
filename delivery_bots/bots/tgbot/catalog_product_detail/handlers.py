from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.emoji import emojize

from delivery_bots.api.moltin.cart.cart import add_product_to_cart
from delivery_bots.bots.tgbot.menu.messages import go_to_menu
from delivery_bots.bots.tgbot.states import BotState


async def catalog_product_detail_handler(query: CallbackQuery, state: FSMContext):
    """Handler for catalog product detail."""
    current_state = await state.get_data()
    chunk = current_state['chunk']
    if query.data == 'go_to_menu':
        await go_to_menu(query, chunk)
    elif query.data == 'add_to_cart':
        cart_response = await add_product_to_cart(
            catalog_product_id=current_state['catalog_product_id'],
            catalog_product_quantity=1,
            cart_id=str(query.from_user.id),
        )

        if 'data' not in cart_response.json():
            return
        await query.answer(emojize(':pizza: успешно добавлена в корзину!'))
        await BotState.catalog_product_detail.set()


def register_catalog_product_detail_handler(dp: Dispatcher):
    """Register menu handler."""
    dp.register_callback_query_handler(catalog_product_detail_handler, state=BotState.catalog_product_detail)
