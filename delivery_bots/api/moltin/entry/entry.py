from typing import Dict, List, Union

import httpx
from geopy import distance

from delivery_bots.api.moltin.auth.auth import get_headers
from delivery_bots.api.moltin.entry.schemas import Entry
from delivery_bots.api.moltin.errors.exceptions import MoltinError


async def fetch_all_entries(flow_slug: str) -> httpx.Response:
    """Fetches all entries."""
    headers = await get_headers()
    base_url = f'https://api.moltin.com/v2/flows/{flow_slug}/entries'
    async with httpx.AsyncClient() as client:
        response = await client.get(url=base_url, headers=headers)
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError:
            raise MoltinError(response.json())  # type: ignore
        return response


async def parse_all_entries_response(response: httpx.Response) -> List[Entry]:
    """Parse all entries response."""
    raw_entries = response.json().get('data')
    return [Entry(**entry) for entry in raw_entries]


def calculate_distance_from_pizzeria_to_customer(entry: Entry, customer_lon: float, customer_lat: float):
    """Calculate distance from pizzeria to user."""
    distance_to_user = distance.distance(  # noqa: WPS317
        (customer_lat, customer_lon),
        (float(entry.latitude), float(entry.longitude)),
    ).km

    return {
        'pizzeria': entry,
        'distance_to_user': round(distance_to_user, 4),
    }


def get_distance_from_pizzeria_to_user(pizzeria: Dict[str, Union[Entry, float]]):
    """
    Gets distance from pizzeria to user.

    :param pizzeria: dictionary with pizzeria and distance to user
    :return: distance from user to pizzeria
    """
    return pizzeria['distance_to_user']


async def find_nearest_pizzeria(entries: List[Entry], customer_lon: float, customer_lat: float):
    """Finds the nearest pizzeria."""
    pizzerias = [calculate_distance_from_pizzeria_to_customer(entry, customer_lon, customer_lat) for entry in entries]
    return min(pizzerias, key=get_distance_from_pizzeria_to_user)
