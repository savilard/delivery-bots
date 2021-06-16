import datetime

from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from delivery_bots.bots.tgbot.settings import TgBotSettings


async def send_message(query: CallbackQuery, customer_tg_id: int, message: str) -> None:
    """Sends message to telegram chat."""
    await query.message.bot.send_message(
        chat_id=customer_tg_id,
        text=message,
    )


async def handle_take_order_button(query: CallbackQuery):
    """Handle delivery man."""
    tg_bot_settings = TgBotSettings()
    callback_action, customer_tg_id = query.data.split(':')
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        send_message,
        'date',
        args=[query, customer_tg_id, tg_bot_settings.message_for_customer],
        next_run_time=datetime.datetime.now() + datetime.timedelta(minutes=tg_bot_settings.estimated_delivery_time),
    )
    scheduler.start()


def register_handler_take_order_button(dp: Dispatcher):
    """Register cart handler."""
    dp.register_callback_query_handler(handle_take_order_button, lambda query: 'take_order' in query.data, state='*')
