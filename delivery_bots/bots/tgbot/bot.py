from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher import FSMContext
from aiogram.utils.emoji import emojize

from delivery_bots.api.moltin.catalog_products.catalog_product import (
    get_catalog_products,
)
from delivery_bots.bots.tgbot.cart.handlers import register_handler_cart
from delivery_bots.bots.tgbot.catalog_product_detail.handlers import (
    register_catalog_product_detail_handler,
)
from delivery_bots.bots.tgbot.checkout.customer_contacts.handlers import (
    register_handler_waiting_email,
)
from delivery_bots.bots.tgbot.checkout.location.handlers import (
    register_handlers_location,
)
from delivery_bots.bots.tgbot.logger import configure_logging
from delivery_bots.bots.tgbot.menu.handlers import register_menu_handler
from delivery_bots.bots.tgbot.menu.keyboard import create_menu_keyboard
from delivery_bots.bots.tgbot.settings import RedisSettings, TgBotSettings
from delivery_bots.bots.tgbot.states import BotState


async def start(message: types.Message, state: FSMContext):
    """
    Handler for START state.

    When the bot is launched, the user is sent a menu with catalog products.
    """
    catalog_products = await get_catalog_products()

    await message.answer(
        text=emojize('Пожалуйста, выберите :pizza:'),
        reply_markup=await create_menu_keyboard(catalog_products),
    )
    await state.update_data(chunk=0)
    await BotState.menu.set()


def register_start_handler(dispatcher: Dispatcher):
    """Register start handler."""
    dispatcher.register_message_handler(start, commands=['start'], state='*')


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

    executor.start_polling(
        dp,
        skip_updates=True,
        on_shutdown=shutdown,
    )
