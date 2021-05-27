from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from more_itertools import chunked

from delivery_bots.api.moltin.catalog_products.schemas import CatalogProduct
from delivery_bots.bots.tgbot.common.keyboard_buttons import CART_BUTTON

NEXT_BUTTON = InlineKeyboardButton(
    text='Вперёд ➡️',
    callback_data='next',
)

PREV_BUTTON = InlineKeyboardButton(
    text='⬅️ Назад',
    callback_data='prev',
)


async def create_menu_keyboard(catalog_products: List[CatalogProduct], chunk=0) -> InlineKeyboardMarkup:
    """The function collects a keyboard for main menu of telegram bot."""
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

    keyboard.append([CART_BUTTON])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
