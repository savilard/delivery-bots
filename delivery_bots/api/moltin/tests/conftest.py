import pytest


@pytest.fixture
def headers():
    """Fake Moltin API auth headers."""
    return {
        'Authorization': 'Bearer test_token',
        'Content-Type': 'application/json',
    }
