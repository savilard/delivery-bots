from aiogram.dispatcher.filters.state import State, StatesGroup


class BotState(StatesGroup):
    """State class."""

    menu = State()
