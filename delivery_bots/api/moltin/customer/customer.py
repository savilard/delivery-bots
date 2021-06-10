import http
from typing import Optional

import httpx

from delivery_bots.api.moltin.auth.auth import get_headers
from delivery_bots.api.moltin.errors.exceptions import MoltinError

BASE_URL = 'https://api.moltin.com/v2/customers/'


async def create_customer(customer_name: str, customer_email: str) -> Optional[httpx.Response]:
    """Creates a customer."""
    headers = await get_headers()
    payloads = {
        'data': {
            'type': 'customer',
            'name': customer_name,
            'email': customer_email,
        },
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=BASE_URL,
            headers=headers,
            json=payloads,
        )

        if response.status_code == http.HTTPStatus.CONFLICT:
            return None

        try:
            response.raise_for_status()
        except httpx.HTTPStatusError:
            raise MoltinError(response.json())  # type: ignore
        return response
