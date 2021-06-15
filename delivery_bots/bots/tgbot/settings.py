from typing import List

from pydantic import BaseSettings, Field


class TgBotSettings(BaseSettings):
    """Telegram bot settings."""

    token: str = Field(env='TELEGRAM_TOKEN')
    tg_id_of_delivery_men: List[int] = Field(env='ID_OF_DELIVERY_MEN')


class RedisSettings(BaseSettings):
    """Redis settings."""

    host: str = Field(env='REDIS_HOST')
    port: int = Field(env='REDIS_PORT')
    password: str = Field(env='REDIS_PASSWORD')


class YandexGeocoderApiSettings(BaseSettings):
    """Yandex geocoder api settings."""

    api_key: str = Field(env='YANDEX_GEOCODER_API_KEY')
