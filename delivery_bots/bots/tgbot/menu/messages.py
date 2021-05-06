from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ParseMode
from aiogram.utils.emoji import emojize

from delivery_bots.bots.tgbot.loader import bot
from delivery_bots.bots.tgbot.menu.keyboard import create_menu_keyboard


async def edit_menu(query: CallbackQuery, state: FSMContext, chunk: int):
    """Edits a menu when navigating through it."""
    keyboard = await create_menu_keyboard(chunk=chunk)
    await state.update_data(chunk=chunk)

    return await bot.edit_message_text(
        text=emojize('Пожалуйста, выберите :pizza:'),
        chat_id=query.from_user.id,
        message_id=query.message.message_id,
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard,
    )
