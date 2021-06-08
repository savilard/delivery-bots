from typing import Optional

import httpx

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


async def parse_all_entries_response(response: httpx.Response) -> Optional[list[Entry]]:
    """Parse all entries response."""
    raw_entries = response.json().get('data')
    if not raw_entries:
        return None

    return [Entry(**entry) for entry in raw_entries]
