from typing import Dict, Union

import pytest
from pytest_httpx import HTTPXMock

from delivery_bots.api.moltin.auth.auth import get_headers

URL = 'https://api.moltin.com/oauth/access_token'


@pytest.fixture
def auth_response():
    return {
        'expires': 1524486008,
        'identifier': 'client_credentials',
        'expires_in': 3600,
        'access_token': 'xa3521ca621113e44eeed9232fa3e54571cb08bc',
        'token_type': 'Bearer',
    }


@pytest.mark.asyncio
async def test_get_headers(httpx_mock: HTTPXMock, auth_response: Dict[str, Union[int, str]]):
    httpx_mock.add_response(url=URL, json=auth_response, method='POST')
    response = await get_headers()
    assert response['Authorization'] == f'Bearer {auth_response["access_token"]}'
    assert response['Content-Type'] == 'application/json'
