from typing import Dict

import httpx

from delivery_bots.api.moltin.errors.exceptions import MoltinError

CATALOG_PRODUCT_BASE_URL = 'https://api.moltin.com/v2/products'


async def fetch_catalog_products(headers: Dict[str, str]):
    """
    Fetches Moltin catalog products.

    :param headers: headers for auth to Moltin API
    :return: list of catalog products or error
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(url=CATALOG_PRODUCT_BASE_URL, headers=headers)
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError:
            raise MoltinError(response.json())  # type: ignore
        return response.json()


async def fetch_catalog_product_detail(catalog_product_id: str, headers) -> httpx.Response:
    """Fetches moltin catalog product detail."""
    async with httpx.AsyncClient(base_url=CATALOG_PRODUCT_BASE_URL) as client:
        response = await client.get(url=f'/{catalog_product_id}', headers=headers)
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError:
            raise MoltinError(response.json())  # type: ignore
        return response.json()
