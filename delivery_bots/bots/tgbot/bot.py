from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from delivery_bots.bots import register_filters, register_handlers
from delivery_bots.bots.tgbot.logger import configure_logging
from delivery_bots.bots.tgbot.settings import RedisSettings, TgBotSettings


async def shutdown(dispatcher: Dispatcher):
    """Closes the connection to the BotState."""
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    tg_bot_settings = TgBotSettings()
    redis_settings = RedisSettings()

    configure_logging(level='INFO')

    bot = Bot(token=tg_bot_settings.token, validate_token=True, parse_mode='HTML')

    storage = RedisStorage2(
        host=redis_settings.host,
        port=redis_settings.port,
        password=redis_settings.password,
    )

    dp = Dispatcher(bot, storage=storage)

    register_handlers(dp)
    register_filters(dp)

    executor.start_polling(
        dp,
        skip_updates=True,
        on_shutdown=shutdown,
    )
