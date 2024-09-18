from aiogram import Router, F
from aiogram.types import Message

from ..data_base.requests import select_profile
from ..views import msg_user


router = Router(name=__name__)


@router.message(F.text == '👤 Профиль')
async def send_profile(message: Message) -> None:
    """
    Асинхронный обработчик нажатия кнопки "Профиль 👤".
    Присылает данные профиля пользователя в боте: Telegram ID, полное имя пользователя и баланс.

    :param message: Объект класса Message.
    """

    await message.delete()

    user = await select_profile(user_id=message.from_user.id)

    await message.answer(text=msg_user(user_id=user.user_id, name=user.name, balance=user.balance))
