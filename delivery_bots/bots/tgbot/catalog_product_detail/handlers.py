from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from delivery_bots.bots.tgbot.menu.messages import go_to_menu
from delivery_bots.bots.tgbot.states import BotState


async def catalog_product_detail_handler(query: CallbackQuery, state: FSMContext):
    """Handler for catalog product detail."""
    current_state = await state.get_data()
    chunk = current_state['chunk']
    if query.data == 'go_to_menu':
        await go_to_menu(query, chunk)


def register_catalog_product_detail_handler(dp: Dispatcher):
    """Register menu handler."""
    dp.register_callback_query_handler(catalog_product_detail_handler, state=BotState.catalog_product_detail)
