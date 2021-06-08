import httpx
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.utils.emoji import emojize

from delivery_bots.api.moltin.entry.entry import (
    fetch_all_entries,
    parse_all_entries_response,
)
from delivery_bots.bots.tgbot.checkout.location.location import find_nearest_pizzeria
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
    await state.update_data(customer_lon=location.longitude)
    await state.update_data(customer_lat=location.latitude)


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

    await state.update_data(customer_address=message.text)
    await state.update_data(customer_lon=location[0])
    await state.update_data(customer_lat=location[1])

    entries = await parse_all_entries_response(await fetch_all_entries('pizzeria'))
    await find_nearest_pizzeria(
        entries=entries,
        customer_lon=location[0],
        customer_lat=location[1],
    )


def register_handlers_location(dp: Dispatcher):
    """Register cart handler."""
    dp.register_message_handler(handle_customer_location, state=BotState.geo, content_types=types.ContentType.LOCATION)
    dp.register_message_handler(handle_customer_address, state=BotState.geo)
