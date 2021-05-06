from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from delivery_bots.api.moltin.auth.auth import get_headers
from delivery_bots.api.moltin.catalog_products.catalog_product import fetch_catalog_products
from delivery_bots.api.moltin.catalog_products.schemas import CatalogProduct


async def create_menu_keyboard() -> InlineKeyboardMarkup:
    """The function collects a keyboard for main menu of telegram bot."""
    headers = await get_headers()
    raw_catalog_products = await fetch_catalog_products(headers)

    if 'data' in raw_catalog_products:
        catalog_products = [
            CatalogProduct(**raw_catalog_product) for raw_catalog_product in raw_catalog_products.get('data')
        ]

        keyboard = [
            [
                InlineKeyboardButton(
                    catalog_product.name,
                    callback_data=catalog_product.id,
                ),
            ]
            for catalog_product in catalog_products
            if catalog_product.status == 'live'
        ]

        return InlineKeyboardMarkup(inline_keyboard=keyboard)
