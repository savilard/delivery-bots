from typing import List

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Validates values from environment variables."""

    token: str = Field(env='TELEGRAM_TOKEN')
    redis_host: str = Field(env='REDIS_HOST')
    redis_port: int = Field(env='REDIS_PORT')
    redis_password: str = Field(env='REDIS_PASSWORD')
    estimated_delivery_time: int = Field(env='ESTIMATED_DELIVERY_TIME')
    message_for_customer: str = Field(env='MESSAGE_FOR_CUSTOMER')
    deliverers_tg_ids: List[int] = Field(env='DELIVERERS_TG_IDS')
    payment_token: str = Field(env='PAYMENT_TOKEN')
