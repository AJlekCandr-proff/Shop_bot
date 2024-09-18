from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from ..keyboards.keyboards import main_keyboard
from ..data_base.requests import add_user


router = Router(name=__name__)


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """
    Асинхронный обработчик команды /start.
    Присылает приветствие и меню для пользователя. Добавляет пользователя в базу данных.

    :param message: Объект класса Message.
    """

    await add_user(user_id=message.from_user.id, name=message.from_user.full_name)

    await message.answer(text='Добро пожаловать!', reply_markup=main_keyboard())
