from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher import FSMContext
from aiogram.utils.emoji import emojize

from delivery_bots.bots.tgbot.logger import configure_logging
from delivery_bots.bots.tgbot.menu.handlers import register_menu_handler
from delivery_bots.bots.tgbot.menu.keyboard import create_menu_keyboard
from delivery_bots.bots.tgbot.settings import Settings
from delivery_bots.bots.tgbot.states import BotState


async def start(message: types.Message, state: FSMContext):
    """
    Handler for START state.

    When the bot is launched, the user is sent a menu with catalog products.
    """
    await message.answer(
        text=emojize('Пожалуйста, выберите :pizza:'),
        reply_markup=await create_menu_keyboard(),
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
    settings = Settings()
    configure_logging(level='INFO')

    bot = Bot(token=settings.token, validate_token=True, parse_mode='HTML')

    storage = RedisStorage2(
        host=settings.redis_host,
        port=settings.redis_port,
        password=settings.redis_password,
    )
    dp = Dispatcher(bot, storage=storage)

    register_start_handler(dp)
    register_menu_handler(dp)

    executor.start_polling(
        dp,
        skip_updates=True,
        on_shutdown=shutdown,
    )
