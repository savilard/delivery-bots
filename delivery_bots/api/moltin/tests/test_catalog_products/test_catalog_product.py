import http

import httpx
import pytest
import respx

from delivery_bots.api.moltin.catalog_products import catalog_product
from delivery_bots.api.moltin.errors.exceptions import MoltinError

CATALOG_PRODUCT_BASE_URL = 'https://api.moltin.com/v2/products'


class TestFetchCatalogProducts:
    def test_has_fetch_catalog_products_function(self):
        assert hasattr(catalog_product, 'fetch_catalog_products')

    @respx.mock
    @pytest.mark.asyncio
    async def test_successful_response(self, headers):
        request_mock = respx.get(CATALOG_PRODUCT_BASE_URL)
        response = await catalog_product.fetch_catalog_products(headers)
        assert request_mock.called
        assert response.status_code == http.HTTPStatus.OK

    @respx.mock
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'side_effect',
        [
            httpx.Response(http.HTTPStatus.FORBIDDEN, json={'error': 'message'}),
            httpx.Response(http.HTTPStatus.NOT_FOUND, json={'error': 'message'}),
            httpx.Response(http.HTTPStatus.METHOD_NOT_ALLOWED, json={'error': 'message'}),
            httpx.Response(http.HTTPStatus.TOO_MANY_REQUESTS, json={'error': 'message'}),
            httpx.Response(http.HTTPStatus.INTERNAL_SERVER_ERROR, json={'error': 'message'}),
        ],
    )
    async def test_http_status_error_exept(self, headers, side_effect):
        request = respx.get(CATALOG_PRODUCT_BASE_URL)
        request.side_effect = side_effect

        with pytest.raises(MoltinError, match="{'error': 'message'}"):
            assert await catalog_product.fetch_catalog_products(headers)


class TestFetchCatalogProductDetail:
    def test_has_fetch_catalog_product_detail_function(self):
        assert hasattr(catalog_product, 'fetch_catalog_product_detail')

    @respx.mock
    @pytest.mark.asyncio
    async def test_successful_response(self, headers, classic_tomato_pizza):
        catalog_product_id = classic_tomato_pizza.id
        request_mock = respx.get(f'{CATALOG_PRODUCT_BASE_URL}/{catalog_product_id}')
        response = await catalog_product.fetch_catalog_product_detail(
            catalog_product_id=catalog_product_id,
            headers=headers,
        )
        assert request_mock.called
        assert response.status_code == http.HTTPStatus.OK

    @respx.mock
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'side_effect',
        [
            httpx.Response(http.HTTPStatus.FORBIDDEN, json={'error': 'message'}),
            httpx.Response(http.HTTPStatus.NOT_FOUND, json={'error': 'message'}),
            httpx.Response(http.HTTPStatus.METHOD_NOT_ALLOWED, json={'error': 'message'}),
            httpx.Response(http.HTTPStatus.TOO_MANY_REQUESTS, json={'error': 'message'}),
            httpx.Response(http.HTTPStatus.INTERNAL_SERVER_ERROR, json={'error': 'message'}),
        ],
    )
    async def test_http_status_error_exept(self, headers, side_effect, classic_tomato_pizza):
        catalog_product_id = classic_tomato_pizza.id
        request_mock = respx.get(f'{CATALOG_PRODUCT_BASE_URL}/{catalog_product_id}')
        request_mock.side_effect = side_effect

        with pytest.raises(MoltinError, match="{'error': 'message'}"):
            assert await catalog_product.fetch_catalog_product_detail(
                catalog_product_id=catalog_product_id,
                headers=headers,
            )
