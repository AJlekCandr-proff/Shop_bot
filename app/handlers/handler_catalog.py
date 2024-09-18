from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from ..views import msg_product
from ..utils.states_form import StatesUser
from ..bot_settings import YandexSplitBot, settings
from ..data_base.requests import *
from ..keyboards.inline_markup import categories_menu, catalog_menu, buy_menu


router = Router(name=__name__)


@router.message(F.text == '🛒 Купить')
async def send_category(message: Message, state: FSMContext) -> None:
    """
    Асинхронный обработчик нажатия кнопки "🛒 Купить".
    Присылает каталог игр и открывает состояние FSM 'choice_product' для выбора товара.

    :param message: Объект класса Message.
    :param state: Объект класса FSMContext.
    """

    await message.delete()

    await message.answer(text='<b>Просмотр категорий</b>', reply_markup=categories_menu())

    await state.set_state(state=StatesUser.choice_game)


@router.callback_query(F.data.startswith('category_'))
async def send_catalog(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Асинхронный обработчик нажатия кнопки выбора категории товара.
    Отправляет каталог выбранной категории и открывает состояние FSM 'choice_product' для выбора товара.

    :param callback: Объект класса CallbackQuery.
    :param state: Объект класса FSMContext.
    """

    await callback.message.delete()

    await callback.message.answer(text='<b>Просмотр подкатегорий</b>', reply_markup=catalog_menu(await select_catalog()))

    await state.set_state(state=StatesUser.choice_product)


@router.callback_query(StatesUser.choice_product)
async def send_product(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Асинхронный обработчик выбора товара в выбранной игре.
    Присылает информацию о выбранном товаре и присылает меню для выбора действия с товаром,
    открывает состояние FSM "buy_product".

    :param callback: Объект класса CallbackQuery.
    :param state: Объект класса FSMContext.
    """

    await callback.message.delete()

    product = await select_product(int(callback.data))

    await callback.message.answer(text=msg_product(product.title_product, product.Cost), reply_markup=buy_menu())

    await state.update_data(price=product.Cost, product=product.title_product)
    await state.set_state(state=StatesUser.buy_product)


@router.callback_query(StatesUser.buy_product)
async def buy_product_game(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Асинхронный обработчик нажатия кнопки "Купить 💳".
    Списывает деньги с баланса и запрашивает адрес электронной почты.
    В противном случае, при недостаточном балансе,
    выводит сообщение об ошибке и предложение пополнить баланс.

    :param callback: Объект класса CallbackQuery.
    :param state: Объект класса FSMContext.
    """

    await callback.message.delete()

    data = await state.get_data()
    product = data['product']
    price = data['price']

    user = await select_profile(user_id=callback.from_user.id)

    if user.balance >= price:
        await update_balance(user_id=callback.from_user.id, balance=user.balance - price)

        await callback.message.answer(text='Спасибо за покупку! С вами свяжется администрация бота в ближайшее время...')

        await YandexSplitBot.send_message(
            chat_id=settings.ADMIN_ID,
            text=f'🔔 <i>Новая покупка 🛍</i>\n\n'
                 f'<b>👤 Пользователь:</b> <a href="tg:user?id={user.user_id}">{callback.from_user.full_name}</a>\n'
                 f'<b>🆔 Telegram:</b> <ins>{user.user_id}</ins>\n\n'
                 f'<b>📦 Товар:</b> {product}\n'
                 f'<b>💰 Сумма:</b> {price} ₽\n\n'
        )
    else:
        await callback.message.answer(
            text=f'❌ Недостаточно средств на балансе!\n\n'
                 f'💰 Баланс: {user.balance} ₽\n\n',
        )
