from aiogram.types import CallbackQuery


async def delete_previous_message(query: CallbackQuery) -> None:
    """
    Deletes the previous message.

    Args:
        query: aiogram callback query
    """
    await query.message.delete()
