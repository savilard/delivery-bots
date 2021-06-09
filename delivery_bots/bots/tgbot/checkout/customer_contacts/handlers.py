from aiogram import Dispatcher
from aiogram.types import Message
from validate_email import validate_email

from delivery_bots.bots.tgbot.checkout.location.messages import (
    request_customer_location,
)
from delivery_bots.bots.tgbot.states import BotState


async def handle_waiting_email(message: Message) -> None:
    """Handler for Store.waiting_mail state."""
    is_email_valid = validate_email(message.text)
    if not is_email_valid:
        await message.answer(text='Кажется, вы неправильно ввели email. Повторите попытку.')
        await BotState.waiting_mail.set()
        return None
    await request_customer_location(message)


def register_handler_waiting_email(dp: Dispatcher):
    """Register cart handler."""
    dp.register_message_handler(handle_waiting_email, state=BotState.waiting_mail)
