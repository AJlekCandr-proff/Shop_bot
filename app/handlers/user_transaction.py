from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from ..utils.states_form import StatesUser
from ..views import msg_payment


router = Router(name=__name__)


@router.message(F.text == '💰 Пополнить')
async def send_payment(message: Message, state: FSMContext) -> None:
    await message.answer(text='Введите сумму к пополнению: ')

    await state.set_state(StatesUser.get_sum)


@router.message(StatesUser.get_sum)
async def get_sum_to_payment(message: Message, state: FSMContext) -> None:
    await message.answer(text='Отлично! ')





