from aiogram import Dispatcher, types

from delivery_bots.bots.tgbot.settings import TgBotSettings
from delivery_bots.bots.tgbot.states import BotState


async def handle_payment(query: types.CallbackQuery):
    """Handle payment."""
    payment_token = TgBotSettings().payment_token
    order_total_amount = 50000
    delivery_total_amount = 10000

    await query.message.bot.send_invoice(
        query.from_user.id,
        title='Оплата заказа',
        description='Тестовое описание',
        provider_token=payment_token,
        currency='RUB',
        is_flexible=False,
        prices=[
            types.LabeledPrice(label='Заказ', amount=order_total_amount),
            types.LabeledPrice(label='Доставка', amount=delivery_total_amount),
        ],
        start_parameter='create_invoice_pizza',
        payload='pizza_order',
        need_phone_number=True,
    )


def register_payment_handler(dp: Dispatcher):
    """Register payment handler."""
    dp.register_callback_query_handler(handle_payment, state=BotState.payment)
