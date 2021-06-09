from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup

from delivery_bots.bots.tgbot.states import BotState


async def request_customer_location(message: Message) -> None:
    """Requests customer location."""
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        KeyboardButton('Отправить локацию', request_location=True),
    )
    await message.answer(
        text='Пришлите нам ваш адрес текстом или геолокацию',
        reply_markup=keyboard,
    )
    await BotState.geo.set()
