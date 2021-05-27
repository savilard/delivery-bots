from aiogram.types import InlineKeyboardButton
from aiogram.utils.emoji import emojize

SHOW_MENU_BUTTON = InlineKeyboardButton(
    text=emojize('🔙 Меню'),
    callback_data='go_to_menu',
)

CART_BUTTON = InlineKeyboardButton(
    text=emojize('🛒 Корзина'),
    callback_data='go_to_cart',
)
