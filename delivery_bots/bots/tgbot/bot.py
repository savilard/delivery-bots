from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from delivery_bots.bots.tgbot.cart.handlers import register_handler_cart
from delivery_bots.bots.tgbot.catalog_product_detail.handlers import (
    register_catalog_product_detail_handler,
)
from delivery_bots.bots.tgbot.checkout.customer_contacts.handlers import (
    register_handler_waiting_email,
)
from delivery_bots.bots.tgbot.checkout.delivery.handlers import (
    register_handler_delivery,
)
from delivery_bots.bots.tgbot.checkout.delivery_man.handlers import (
    register_handler_take_order_button,
)
from delivery_bots.bots.tgbot.checkout.location.handlers import (
    register_handlers_location,
)
from delivery_bots.bots.tgbot.common.filters.role import (
    CustomerFilter,
    DeliveryManFilter,
)
from delivery_bots.bots.tgbot.logger import configure_logging
from delivery_bots.bots.tgbot.menu.handlers import register_menu_handler
from delivery_bots.bots.tgbot.settings import RedisSettings, TgBotSettings
from delivery_bots.bots.tgbot.start.handlers import register_start_handler


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

    register_start_handler(dp)
    register_menu_handler(dp)
    register_catalog_product_detail_handler(dp)
    register_handler_cart(dp)
    register_handlers_location(dp)
    register_handler_waiting_email(dp)
    register_handler_delivery(dp)
    register_handler_take_order_button(dp)

    dp.filters_factory.bind(DeliveryManFilter)
    dp.filters_factory.bind(CustomerFilter)

    executor.start_polling(
        dp,
        skip_updates=True,
        on_shutdown=shutdown,
    )
