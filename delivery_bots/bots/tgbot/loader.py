import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from delivery_bots.bots.tgbot.settings import Settings

settings = Settings()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.token, parse_mode=types.ParseMode.HTML)
storage = RedisStorage2(
    host=settings.redis_host,
    port=settings.redis_port,
    password=settings.redis_password,
)
dp = Dispatcher(bot, storage=storage)
