from pydantic import BaseModel


class Auth(BaseModel):
    """Auth schemas of Moltin."""

    expires: int
    identifier: str
    expires_in: int
    access_token: str
    token_type: str
