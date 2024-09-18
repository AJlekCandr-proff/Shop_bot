from aiogram import Router, F
from aiogram.types import Message

from ..views import msg_rules


router = Router(name=__name__)


@router.message(F.text == '📘 Правила')
async def support_user(message: Message) -> None:
    """
    Асинхронный обработчик нажатия кнопки "📘 Правила".
    Присылает правила к использованию бота.

    :param message: Объект класса Message.
    """

    await message.answer(text=msg_rules())
