from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Validates values from environment variables."""

    token: str = Field(env='TELEGRAM_TOKEN')
    redis_host: str = Field(env='REDIS_HOST')
    redis_port: int = Field(env='REDIS_PORT')
    redis_password: str = Field(env='REDIS_PASSWORD')
