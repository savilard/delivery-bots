from typing import Dict

import httpx
from delivery_bots.api.moltin.auth.schemas import Auth
from pydantic import BaseSettings, Field

MOLTIN_API_OAUTH_URL = 'https://api.moltin.com/oauth'


class Settings(BaseSettings):
    """Gets and validates values from environment variables."""

    client_id: str = Field(env='ELASTICPATH_CLIENT_ID')
    client_secret: str = Field(env='ELASTICPATH_CLIENT_SECRET')


async def get_headers() -> Dict[str, str]:
    """Gets headers for authorization on Moltin."""
    settings = Settings()
    payload = {
        'client_id': settings.client_id,
        'client_secret': settings.client_secret,
        'grant_type': 'client_credentials',
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url='https://api.moltin.com/oauth/access_token', data=payload)
        response.raise_for_status()
        auth = Auth(**response.json())
        return {
            'Authorization': f'Bearer {auth.access_token}',
            'Content-Type': 'application/json',
        }
