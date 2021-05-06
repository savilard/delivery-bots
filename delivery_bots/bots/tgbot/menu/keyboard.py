from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from more_itertools import chunked

from delivery_bots.api.moltin.auth.auth import get_headers
from delivery_bots.api.moltin.catalog_products.catalog_product import (
    fetch_catalog_products,
)
from delivery_bots.api.moltin.catalog_products.schemas import CatalogProduct

NEXT_BUTTON = InlineKeyboardButton(
    text='Вперёд ➡️',
    callback_data='next',
)

PREV_BUTTON = InlineKeyboardButton(
    text='⬅️ Назад',
    callback_data='prev',
)


async def create_menu_keyboard(chunk=0) -> InlineKeyboardMarkup:
    """The function collects a keyboard for main menu of telegram bot."""
    headers = await get_headers()
    raw_catalog_products = await fetch_catalog_products(headers)

    if 'data' in raw_catalog_products:
        catalog_products = [
            CatalogProduct(**raw_catalog_product) for raw_catalog_product in raw_catalog_products.get('data')
        ]

        chunks = list(chunked(catalog_products, 8))

        keyboard = [
            [
                InlineKeyboardButton(
                    catalog_product.name,
                    callback_data=catalog_product.id,
                ),
            ]
            for catalog_product in chunks[chunk]
            if catalog_product.status == 'live'
        ]

        if chunk == 0:
            keyboard.append([NEXT_BUTTON])
        elif chunk == len(chunks) - 1:
            keyboard.append([PREV_BUTTON])
        else:
            keyboard.append([PREV_BUTTON, NEXT_BUTTON])

        return InlineKeyboardMarkup(inline_keyboard=keyboard)
