import httpx

from delivery_bots.api.moltin.errors.exceptions import MoltinError
from delivery_bots.api.moltin.files.schemas import MoltinFile

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


async def parse_moltin_file_detail_response(response: httpx.Response) -> MoltinFile:
    """
    Parse moltin file detail response.

    Args:
        response: response if fetching moltin file detail response

    Returns:
        MoltinFile
    """
    raw_moltin_file_detail = response.json()
    return MoltinFile(**raw_moltin_file_detail)


async def get_catalog_product_image_url(image_id: str, headers: dict[str, str]) -> str:
    """Gets catalog product image id.

    Args:
        image_id: id of moltin catalog product
        headers: headers for moltin api auth

    Returns:
        object: link to moltin catalog product image
    """
    file_detail_response = await fetch_moltin_file_detail(
        headers=headers,
        file_id=image_id,
    )
    file_detail = await parse_moltin_file_detail_response(response=file_detail_response)
    return file_detail.data.link.href
