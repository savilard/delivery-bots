import ujson
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from delivery_bots.api.moltin.entry.schemas import Entry
from delivery_bots.bots.tgbot.states import BotState


async def handle_delivery(query: CallbackQuery, state: FSMContext):
    """Handler for BotState.delivery state."""
    current_state = await state.get_data()
    nearest_pizzeria = Entry(**ujson.loads(current_state['nearest_pizzeria']))

    if query.data == 'pickup':
        message = (
            f'Отлично! Вы можете забрать заказ в ближайшей пиццерии "{nearest_pizzeria.alias}"'
            + f', которая расположена по адресу: {nearest_pizzeria.address}.'
        )
        await query.message.answer(text=message)


def register_handler_delivery(dp: Dispatcher):
    """Register cart handler."""
    dp.register_callback_query_handler(handle_delivery, state=BotState.delivery)
