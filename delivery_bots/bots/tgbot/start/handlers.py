from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.utils.emoji import emojize

from delivery_bots.api.moltin.catalog_products.catalog_product import (
    get_catalog_products,
)
from delivery_bots.bots.tgbot.menu.keyboard import create_menu_keyboard
from delivery_bots.bots.tgbot.servises.filters.role import CustomerFilter
from delivery_bots.bots.tgbot.states import BotState


async def start(message: types.Message, state: FSMContext):
    """
    Handler for START state.

    When the bot is launched, the user is sent a menu with catalog products.
    """
    await state.finish()
    catalog_products = await get_catalog_products()

    await message.answer(
        text=emojize('Пожалуйста, выберите :pizza:'),
        reply_markup=await create_menu_keyboard(catalog_products),
    )
    await state.update_data(chunk=0)
    await BotState.menu.set()


def register_start_handler(dispatcher: Dispatcher):
    """Register start handler."""
    dispatcher.register_message_handler(start, CustomerFilter(), commands=['start'], state='*')
