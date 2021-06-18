from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from delivery_bots.bots.tgbot.settings import TgBotSettings
from delivery_bots.bots.tgbot.states import BotState


async def handle_payment(query: types.CallbackQuery, state: FSMContext):
    """Handle payment."""
    current_state = await state.get_data()
    payment_token = TgBotSettings().payment_token
    delivery_total_amount = current_state['delivery_total_amount']
    order_description = current_state['order_description']
    order_total_amount = current_state['order_total_amount']

    await query.message.bot.send_invoice(
        query.from_user.id,
        title='Оплата заказа',
        description=order_description,
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


async def handle_pre_checkout(query: types.CallbackQuery, pre_checkout_query: types.PreCheckoutQuery):
    """Handle pre checkout."""
    await query.message.bot.answer_pre_checkout_query(
        pre_checkout_query.id,
        ok=True,
        error_message=(
            'Инопланетяне пытались украсть вашу карту, но мы успешно защитили ваши учетные данные,'
            + 'попробуем заплатить еще раз через несколько минут, нам нужен небольшой отдых.'
        ),
    )


async def handle_got_payment(message: types.Message):
    """Handle got payment."""
    await message.bot.send_message(
        message.chat.id,
        (
            'Hoooooray! Спасибо за оплату! Мы обработаем ваш заказ на `{} {}`'
            + ' быстро настолько, насколько это возможно! Оставайтесь на связи.'
        ).format(
            message.successful_payment.total_amount / 100,
            message.successful_payment.currency,
        ),
    )


def register_payment_handler(dp: Dispatcher):
    """Register payment handler."""
    dp.register_callback_query_handler(handle_payment, state=BotState.payment)
    dp.pre_checkout_query_handler(handle_pre_checkout, lambda query: True, state=BotState.payment)
    dp.message_handler(handle_got_payment, content_types=types.ContentTypes.SUCCESSFUL_PAYMENT, state=BotState.payment)
