from aiogram.types import CallbackQuery

from delivery_bots.api.moltin.auth.auth import get_headers
from delivery_bots.api.moltin.catalog_products.catalog_product import (
    fetch_catalog_product_detail,
    parse_catalog_product_detail_response,
)


async def send_detailed_catalog_product_description(query: CallbackQuery) -> None:
    """Sends message with a detailed catalog product description."""
    catalog_product_id = query.data
    headers = await get_headers()
    catalog_product_detail_response = await fetch_catalog_product_detail(catalog_product_id, headers)
    catalog_product_detail = await parse_catalog_product_detail_response(catalog_product_detail_response)
    message_text = '{name}\n Стоимость - {price}\n\n{description}'.format(
        name=catalog_product_detail.name,
        price=catalog_product_detail.meta.display_price.with_tax.formatted,
        description=catalog_product_detail.description,
    )
    await query.message.answer(text=message_text)
