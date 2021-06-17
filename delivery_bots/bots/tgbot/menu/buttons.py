from aiogram.types import InlineKeyboardButton
from aiogram.utils.emoji import emojize


async def create_menu_button() -> InlineKeyboardButton:
    """Create tgbot menu button."""
    return InlineKeyboardButton(
        text=emojize('🔙 Меню'),
        callback_data='go_to_menu',
    )
