from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from delivery_bots.bots.tgbot.loader import dp
from delivery_bots.bots.tgbot.menu.messages import edit_menu
from delivery_bots.bots.tgbot.states import BotState


@dp.callback_query_handler(state=BotState.menu)  # type: ignore
async def handle_menu(query: CallbackQuery, state: FSMContext):  # noqa: WPS217
    """Handler for BotState.menu state."""
    state_data = await state.get_data()
    chunk = state_data['chunk']

    if query.data == 'next':
        await edit_menu(query, state, chunk + 1)
        await BotState.menu.set()
    elif query.data == 'prev':
        await edit_menu(query, state, chunk - 1)
        await BotState.menu.set()
