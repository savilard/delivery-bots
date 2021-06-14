from aiogram.types import InlineKeyboardMarkup

from delivery_bots.bots.tgbot.checkout.delivery.buttons import (
    create_delivery_button,
    create_pickup_button,
)


async def create_delivery_keyboard(distance_to_user) -> InlineKeyboardMarkup:
    """
    The function collects a keyboard for product description.

    The radius of the delivery area is indicated in kilometers.
    """
    delivery_button = await create_delivery_button()
    pickup_button = await create_pickup_button()
    delivery_area_radius = 20
    keyboard = [[delivery_button], [pickup_button]] if distance_to_user <= delivery_area_radius else [[pickup_button]]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
