from aiogram.fsm.state import StatesGroup, State


class RecordState(StatesGroup):
    START = State()
    CATEGORY = State()
    ADITIONAL_DESCRIPTION = State()
    COST = State()
    CURRENCY = State()
    CONFIRMATION = State()
    SAVING = State()


