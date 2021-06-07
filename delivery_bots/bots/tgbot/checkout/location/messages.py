from aiogram.types import CallbackQuery, KeyboardButton, ReplyKeyboardMarkup

from delivery_bots.bots.tgbot.states import BotState


async def request_customer_location(query: CallbackQuery) -> None:
    """Requests customer location."""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        KeyboardButton('Отправить локацию', request_location=True),
    )
    await query.message.answer(
        text='Пришлите нам ваш адрес текстом или геолокацию',
        reply_markup=keyboard,
    )
    await BotState.geo.set()
