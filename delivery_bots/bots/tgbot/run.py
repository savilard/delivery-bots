from aiogram import Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.utils.emoji import emojize

from delivery_bots.bots.tgbot.loader import dp
from delivery_bots.bots.tgbot.logger import configure_logging
from delivery_bots.bots.tgbot.menu.keyboard import create_menu_keyboard
from delivery_bots.bots.tgbot.states import BotState


@dp.message_handler(commands=['start'], state='*')  # type: ignore
async def start(message: types.Message, state: FSMContext):
    """
    Handler for START state.

    When the bot is launched, the user is sent a store menu.
    """
    await message.answer(
        text=emojize('Пожалуйста, выберите :pizza:'),
        reply_markup=await create_menu_keyboard(),
    )
    await state.update_data(chunk=0)
    await BotState.menu.set()


async def shutdown(dispatcher: Dispatcher):
    """Closes the connection to the state store."""
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    configure_logging('INFO')
    executor.start_polling(
        dp,
        skip_updates=True,
        on_shutdown=shutdown,
    )
