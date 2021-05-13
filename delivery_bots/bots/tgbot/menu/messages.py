from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ParseMode
from aiogram.utils.emoji import emojize

from delivery_bots.api.moltin.auth.auth import get_headers
from delivery_bots.api.moltin.catalog_products.catalog_product import (
    fetch_catalog_products,
    parse_catalog_products_response,
)
from delivery_bots.bots.tgbot.menu.keyboard import create_menu_keyboard


async def edit_menu(query: CallbackQuery, state: FSMContext, chunk: int):
    """Edits a menu when navigating through it."""
    headers = await get_headers()

    catalog_products_response = await fetch_catalog_products(headers)
    catalog_products = await parse_catalog_products_response(catalog_products_response)

    keyboard = await create_menu_keyboard(catalog_products, chunk=chunk)

    await state.update_data(chunk=chunk)

    return await query.message.edit_text(
        text=emojize('Пожалуйста, выберите :pizza:'),
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard,
    )
