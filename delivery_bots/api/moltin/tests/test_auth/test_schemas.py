import pytest

from delivery_bots.api.moltin.auth.schemas import Auth


@pytest.fixture
def auth_response():
    """Moltin auth response fixture."""
    return {
        'expires': 1524486008,
        'identifier': 'client_credentials',
        'expires_in': 3600,
        'access_token': 'xa3521ca621113e44eeed9232fa3e54571cb08bc',
        'token_type': 'Bearer',
    }


def test_auth_schema(auth_response):
    """Test moltin auth schema."""
    auth = Auth(**auth_response)
    assert auth.expires == 1524486008
    assert auth.identifier == 'client_credentials'
    assert auth.expires_in == 3600
    assert auth.access_token == 'xa3521ca621113e44eeed9232fa3e54571cb08bc'
    assert auth.token_type == 'Bearer'
