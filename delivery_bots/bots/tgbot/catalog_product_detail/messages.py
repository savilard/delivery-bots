from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from delivery_bots.api.moltin.auth.auth import get_headers
from delivery_bots.api.moltin.catalog_products.catalog_product import (
    fetch_catalog_product_detail,
    parse_catalog_product_detail_response,
)
from delivery_bots.api.moltin.files.file_detail import get_catalog_product_image_url
from delivery_bots.bots.tgbot.catalog_product_detail.keyboard import (
    create_catalog_product_detail_keyboard,
)


async def send_detailed_catalog_product_description(query: CallbackQuery, state: FSMContext) -> None:
    """Sends message with a detailed catalog product description."""
    headers = await get_headers()

    catalog_product_id = query.data
    await state.update_data(catalog_product_id=catalog_product_id)

    catalog_product_detail = await parse_catalog_product_detail_response(
        await fetch_catalog_product_detail(
            catalog_product_id=catalog_product_id,
            headers=headers,
        ),
    )
    catalog_product_image_url = await get_catalog_product_image_url(
        headers=headers,
        image_id=catalog_product_detail.relationships.main_image.data.id,  # type: ignore
    )

    message_text = '{name}\n Стоимость - {price}\n\n{description}'.format(
        name=catalog_product_detail.name,
        price=catalog_product_detail.meta.display_price.with_tax.formatted,
        description=catalog_product_detail.description,
    )
    await query.message.answer_photo(
        photo=catalog_product_image_url,
        caption=message_text,
        reply_markup=await create_catalog_product_detail_keyboard(),
    )
