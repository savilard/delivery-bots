from http import HTTPStatus
from typing import Dict

import httpx
import pytest
import respx
import ujson
from pytest_httpx import HTTPXMock

from delivery_bots.api.moltin.catalog_products import catalog_product
from delivery_bots.api.moltin.catalog_products.schemas import (
    CatalogProduct,
    DisplayPrice,
    Meta,
    Stock,
    TaxPrice,
)

CATALOG_PRODUCT_BASE_URL = 'https://api.moltin.com/v2/products'


@pytest.fixture
def classic_tomato_pizza():
    return CatalogProduct(
        type='product',
        id='ce9b47f7-58ee-43f7-9712-c6ee6bd6e24b',
        status='live',
        name='Classic Tomato',
        slug='classic-tomato',
        sku='classic-tomato-001',
        description='Crushed Tomato Sauce, Basil, Romano, Olive Oil, Mozzarella',
        meta=Meta(
            display_price=DisplayPrice(
                with_tax=TaxPrice(amount=1295, currency='USD', formatted='$12.95'),
                without_tax=TaxPrice(amount=1295, currency='USD', formatted='$12.95'),
            ),
            stock=Stock(availability='in-stock', level=500),
        ),
    )


@pytest.fixture
def buffalo_chicken_pizza():
    return CatalogProduct(
        type='product',
        id='ce9b47f7-65ee-44f7-5214-c6ee6bd6e24b',
        status='live',
        name='Buffalo Chicken',
        slug='buffalo-chicken',
        sku='buffalo-chicken-001',
        description='Cheddar Mozzarella Blend, Roasted Red Onion, Hickory Smoked Bacon, Buttermilk Ranch Drizzle',
        meta=Meta(
            display_price=DisplayPrice(
                with_tax=TaxPrice(amount=1995, currency='USD', formatted='$19.95'),
                without_tax=TaxPrice(amount=1995, currency='USD', formatted='$19.95'),
            ),
            stock=Stock(availability='in-stock', level=500),
        ),
    )


@pytest.fixture
def catalog_products_response(classic_tomato_pizza, buffalo_chicken_pizza):
    return ujson.dumps(
        {
            'data': [classic_tomato_pizza.dict(), buffalo_chicken_pizza.dict()],
        },
    )


@pytest.fixture
def catalog_product_detail_response(classic_tomato_pizza):
    return ujson.dumps(
        {
            'data': classic_tomato_pizza.dict(),
        },
    )


class TestFetchCatalogProducts:
    """Tests for a function fetch_catalog_products."""

    def test_has_fetch_catalog_products_function(self):
        """Tests the existence of a fetch_catalog_products function."""
        assert hasattr(catalog_product, 'fetch_catalog_products')

    @pytest.mark.asyncio
    async def test_successful_fetch_of_product_catalog(
        self,
        httpx_mock: HTTPXMock,
        catalog_products_response,
        headers,
    ):
        """Tests the successful execution of the fetch_catalog_products function."""
        httpx_mock.add_response(
            url=CATALOG_PRODUCT_BASE_URL,
            json=catalog_products_response,
            method='GET',
        )
        response = await catalog_product.fetch_catalog_products(headers=headers)
        assert response == catalog_products_response

    @pytest.mark.asyncio
    @pytest.mark.parametrize('status_code', [HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR])
    async def test_unsuccessful_fetch_of_product_catalog(
        self,
        httpx_mock: HTTPXMock,
        catalog_products_response,
        headers: Dict[str, str],
        status_code: int,
    ):
        """Tests the failed execution of the fetch_catalog_products function."""
        httpx_mock.add_response(
            url=CATALOG_PRODUCT_BASE_URL,
            json=catalog_products_response,
            method='GET',
            status_code=status_code,
        )
        response = await catalog_product.fetch_catalog_products(headers=headers)
        assert response is None


class TestFetchCatalogProductDetail:
    """Tests for a function fetch_catalog_product_detail."""

    def test_has_fetch_catalog_product_detail_function(self):
        """Tests the existence of a fetch_catalog_product_detail function."""
        assert hasattr(catalog_product, 'fetch_catalog_product_detail')

    @pytest.mark.asyncio
    @respx.mock
    async def test_fetch_catalog_product_detail(
        self,
        catalog_product_detail_response,
        classic_tomato_pizza,
        headers,
    ):
        request_mock = respx.get(f'{CATALOG_PRODUCT_BASE_URL}/{classic_tomato_pizza.id}')
        request_mock.return_value = httpx.Response(200, json=catalog_product_detail_response)
        response = await catalog_product.fetch_catalog_product_detail(
            catalog_product_id=classic_tomato_pizza.id,
            headers=headers,
        )

        assert response.json() == catalog_product_detail_response
