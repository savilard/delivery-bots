from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import CallbackQuery, Message

from delivery_bots.bots.tgbot.settings import TgBotSettings


class DeliveryManFilter(BoundFilter):
    """Checks if the user is a delivery person."""

    key = 'is_delivery_man'

    async def check(self, message: Message = None, query: CallbackQuery = None):
        """Checks from_user.id."""
        tg_id_of_delivery_men = TgBotSettings().tg_id_of_delivery_men
        if message:
            return message.from_user.id in tg_id_of_delivery_men
        if query:
            return query.from_user.id in tg_id_of_delivery_men


class CustomerFilter(BoundFilter):
    """Checks if the user is a customer."""

    key = 'is_customer'

    async def check(self, message: Message = None, query: CallbackQuery = None):
        """Checks from_user.id."""
        tg_id_of_delivery_men = TgBotSettings().tg_id_of_delivery_men
        if message:
            return message.from_user.id not in tg_id_of_delivery_men
        if query:
            return query.from_user.id not in tg_id_of_delivery_men
