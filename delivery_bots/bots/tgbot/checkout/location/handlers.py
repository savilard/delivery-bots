import httpx
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.utils.emoji import emojize

from delivery_bots.bots.tgbot.checkout.location.messages import (
    send_delivery_terms_to_customer,
)
from delivery_bots.bots.tgbot.settings import YandexGeocoderApiSettings
from delivery_bots.bots.tgbot.states import BotState


async def fetch_coordinates(geocoder_api_key: str, place: str):
    """Fetches the coordinates by place address."""
    payload = {
        'geocode': place,
        'apikey': geocoder_api_key,
        'format': 'json',
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url='https://geocode-maps.yandex.ru/1.x/', params=payload)
        response.raise_for_status()
        places_found = response.json()['response']['GeoObjectCollection']['featureMember']
        try:
            most_relevant = places_found[0]
        except IndexError:
            return None
        return most_relevant['GeoObject']['Point']['pos'].split(' ')


async def handle_customer_location(message: types.Message, state: FSMContext):
    """Processes the received coordinates of the customer."""
    location = message.location
    await send_delivery_terms_to_customer(
        message=message,
        customer_lon=location.longitude,
        customer_lat=location.latitude,
        state=state,
    )


async def handle_customer_address(message: types.Message, state: FSMContext):
    """Processes the received address of the customer."""
    location = await fetch_coordinates(
        geocoder_api_key=YandexGeocoderApiSettings().api_key,
        place=message.text,
    )
    if location is None:
        await message.answer(emojize('Не смогли определить адрес :house:, попробуйте еще раз.'))
        await BotState.geo.set()
        return None

    await send_delivery_terms_to_customer(
        message=message,
        customer_lon=location[0],
        customer_lat=location[1],
        state=state,
    )


def register_handlers_location(dp: Dispatcher):
    """Register cart handler."""
    dp.register_message_handler(handle_customer_location, state=BotState.geo, content_types=types.ContentType.LOCATION)
    dp.register_message_handler(handle_customer_address, state=BotState.geo)
