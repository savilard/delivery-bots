from typing import Dict, List

import httpx

from delivery_bots.api.moltin.catalog_products.schemas import CatalogProduct
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
        return response


async def fetch_catalog_product_detail(catalog_product_id: str, headers) -> httpx.Response:
    """Fetches moltin catalog product detail."""
    async with httpx.AsyncClient(base_url=CATALOG_PRODUCT_BASE_URL) as client:
        response = await client.get(url=f'/{catalog_product_id}', headers=headers)
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError:
            raise MoltinError(response.json())  # type: ignore
        return response


async def parse_catalog_products_response(response: httpx.Response) -> List[CatalogProduct]:
    """Parse catalog product response.

    :param response: response of fetching catalog products.
    :return: list of catalog products in format List[CatalogProduct]
    """
    raw_catalog_products = response.json()
    return [CatalogProduct(**raw_catalog_product) for raw_catalog_product in raw_catalog_products.get('data')]


async def parse_catalog_product_detail_response(response: httpx.Response) -> CatalogProduct:
    """Parse catalog product detail.

    :param response: response of fetching catalog product detail.
    :return: catalog product detail.
    """
    raw_catalog_product_detail = response.json()
    return CatalogProduct(**raw_catalog_product_detail)
