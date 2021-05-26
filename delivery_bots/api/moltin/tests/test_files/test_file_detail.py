import http

import httpx
import pytest
import respx

from delivery_bots.api.moltin.errors.exceptions import MoltinError
from delivery_bots.api.moltin.files import file_detail

FILE_BASE_URL = 'https://api.moltin.com/v2/files/'


@pytest.fixture
def file_id():
    return 'f8cf26b3-6d38-4275-937a-624a83994702'


def test_has_fetch_moltin_file_detail_function():
    assert hasattr(file_detail, 'fetch_moltin_file_detail')


@respx.mock
@pytest.mark.asyncio
async def test_successful_response(headers, file_id):
    request = respx.get(f'{FILE_BASE_URL}/{file_id}')
    response = await file_detail.fetch_moltin_file_detail(headers, file_id)
    assert request.called
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
async def test_http_status_error_except(headers, side_effect, file_id):
    request = respx.get(f'{FILE_BASE_URL}/{file_id}')
    request.side_effect = side_effect

    with pytest.raises(MoltinError, match="{'error': 'message'}"):
        assert await file_detail.fetch_moltin_file_detail(headers, file_id)
