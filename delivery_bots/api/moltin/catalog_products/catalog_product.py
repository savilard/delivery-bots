from typing import Dict

import httpx

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
        except (httpx.HTTPStatusError, httpx.RequestError):
            return None
        return response.json()
