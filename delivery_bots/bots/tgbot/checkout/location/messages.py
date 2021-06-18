from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup

from delivery_bots.api.moltin.entry.entry import (
    fetch_all_entries,
    find_nearest_pizzeria,
    parse_all_entries_response,
)
from delivery_bots.bots.tgbot.checkout.delivery.keyboards import (
    create_delivery_keyboard,
)
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


async def make_message_with_delivery_terms(nearest_pizzeria, state: FSMContext) -> str:
    """Makes message with delivery terms."""
    distance_to_user = nearest_pizzeria['distance_to_user']
    pizzeria_attr = nearest_pizzeria['pizzeria']

    if distance_to_user <= 0.5:  # noqa: WPS459
        message_text = (
            'Может, заберете пиццу из нашей пиццерии неподалёку? '
            + f'Она всего в {distance_to_user} км от Вас! Вот её адрес:'
            + f'{pizzeria_attr.address}\nА можем и бесплатно доставить, нам не сложно)'
        )
        await state.update_data(delivery_total_amount=0)
    elif 0.5 < distance_to_user <= 5:  # noqa: WPS459
        delivery_total_amount = 100
        message_text = (
            'Похоже, придётся ехать до вас на самокате. '
            + f'Доставка будет стоить {delivery_total_amount} рублей. Доставляем или самовывоз?'
        )
        await state.update_data(delivery_total_amount=delivery_total_amount * 100)
    elif 5 < distance_to_user <= 20:  # noqa: WPS432
        delivery_total_amount = 300
        message_text = (
            f'Ближайшая до вас пиццерия - {pizzeria_attr.alias}.'
            + f' Стоимость доставки составит {delivery_total_amount} рублей'
        )
        await state.update_data(delivery_total_amount=delivery_total_amount * 100)
    else:
        message_text = (
            f'Простите, но так далеко мы пиццу не доставляем. Ближайшая пиццерия аж в {distance_to_user} км от Вас!'
        )
    return message_text


async def send_delivery_terms_to_customer(
    message: Message,
    customer_lon,
    customer_lat,
    state: FSMContext,
) -> None:
    """Sends delivery terms to the customer."""
    entries = await parse_all_entries_response(await fetch_all_entries('pizzeria'))
    nearest_pizzeria = await find_nearest_pizzeria(
        entries=entries,
        customer_lon=customer_lon,
        customer_lat=customer_lat,
    )
    await state.update_data(nearest_pizzeria=nearest_pizzeria['pizzeria'].json())
    await state.update_data(customer_lon=customer_lon)
    await state.update_data(customer_lat=customer_lat)

    await message.answer(
        text=await make_message_with_delivery_terms(nearest_pizzeria, state),
        reply_markup=await create_delivery_keyboard(nearest_pizzeria['distance_to_user']),
    )
    await BotState.delivery.set()
