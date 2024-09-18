from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from ..bot_settings import YandexSplitBot, settings
from ..data_base.requests import update_balance, select_profile
from ..keyboards.inline_markup import accept_menu, connection_menu
from ..utils.states_form import StatesUser
from ..views import msg_payment, msg_check_payment


router = Router(name=__name__)


@router.message(F.text == '💰 Пополнить')
async def send_payment(message: Message, state: FSMContext) -> None:
    await message.answer(text='Введите сумму к пополнению: ')

    await state.set_state(StatesUser.get_sum)


@router.message(StatesUser.get_sum)
async def get_sum_to_payment(message: Message, state: FSMContext) -> None:
    await message.answer(text=msg_payment(float(message.text)))

    await state.update_data(sum=message.text)
    await state.set_state(StatesUser.check_pay)


@router.message(StatesUser.check_pay)
async def check_screen_admin(message: Message, state: FSMContext) -> None:
    data = await state.get_data()

    await YandexSplitBot.send_photo(
        chat_id=settings.ADMIN_ID,
        photo=message.photo[-1].file_id,
        caption=msg_check_payment(user_id=message.from_user.id, name=message.from_user.full_name, sum=data['sum']),
        reply_markup=accept_menu()
    )

    await message.answer(text='Ожидайте подтверждения транзакции от администрации 🕓', reply_markup=connection_menu(settings.ADMIN_URL))

    await state.update_data(user_id=message.from_user.id)
    await state.set_state(StatesUser.get_confirmation)


@router.callback_query(F.data == 'accept_payment', StatesUser.get_confirmation)
async def set_balance_user(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    user = await select_profile(data['user_id'])

    await update_balance(user_id=user.user_id, balance=user.balance + float(data['sum']))

    await callback.message.answer(text='<b>Деньги зачислены на баланс пользователю.</b>')

    await YandexSplitBot.send_message(chat_id=user.user_id, text='<b>Деньги зачислены Вам на баланс!</b>')
