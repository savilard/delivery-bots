from aiogram.types import InlineKeyboardButton


async def create_pickup_button() -> InlineKeyboardButton:
    """Creates pickup button."""
    return InlineKeyboardButton(
        text='Самовывоз',
        callback_data='pickup',
    )


async def create_delivery_button() -> InlineKeyboardButton:
    """Creates delivery button."""
    return InlineKeyboardButton(
        text='Доставка',
        callback_data='delivery',
    )
