import httpx

from delivery_bots.api.moltin.errors.exceptions import MoltinError

FILE_BASE_URL = 'https://api.moltin.com/v2/files/'


async def fetch_moltin_file_detail(headers: dict[str, str], file_id: str) -> httpx.Response:
    """
    Fetches moltin file detail.

    Args:
        headers: moltin headers
        file_id: moltin file id

    Returns:
         httpx.Response

    Raises:
        MoltinError: Always
    """
    file_url = f'{FILE_BASE_URL}/{file_id}'
    async with httpx.AsyncClient() as client:
        response = await client.get(url=file_url, headers=headers)
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError:
            raise MoltinError(response.json())  # type: ignore
        return response
