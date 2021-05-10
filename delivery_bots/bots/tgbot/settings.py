from pydantic import BaseSettings, Field


class TgBotSettings(BaseSettings):
    """Telegram bot settings."""

    token: str = Field(env='TELEGRAM_TOKEN')


class RedisSettings(BaseSettings):
    """Redis settings."""

    host: str = Field(env='REDIS_HOST')
    port: int = Field(env='REDIS_PORT')
    password: str = Field(env='REDIS_PASSWORD')
