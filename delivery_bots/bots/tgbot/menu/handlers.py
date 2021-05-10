from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from delivery_bots.bots.tgbot.menu.messages import edit_menu
from delivery_bots.bots.tgbot.states import BotState


async def handle_menu(query: CallbackQuery, state: FSMContext):
    """Handler for BotState.menu state."""
    current_state = await state.get_data()
    chunk = current_state['chunk']

    if query.data == 'next':
        await edit_menu(query=query, state=state, chunk=chunk + 1)
        await BotState.menu.set()
    elif query.data == 'prev':
        await edit_menu(query=query, state=state, chunk=chunk - 1)
        await BotState.menu.set()


def register_menu_handler(dp: Dispatcher):
    """Register menu handler."""
    dp.register_callback_query_handler(handle_menu, state=BotState.menu)
