from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def create_deliverer_keyboard(
    customer_tg_id,
    button_text: str,
    callback_action: str,
) -> InlineKeyboardMarkup:
    """Creates a keyboard for delivery man."""
    keyboard = [
        [
            InlineKeyboardButton(
                text=button_text,
                callback_data=f'{callback_action}:{customer_tg_id}',
            ),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
