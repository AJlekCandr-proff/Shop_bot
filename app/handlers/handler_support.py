from aiogram import Router, F
from aiogram.types import Message


router = Router(name=__name__)


@router.message(F.text == '⁉️ Помощь')
async def support_user(message: Message) -> None:
    """
    Асинхронный обработчик нажатия кнопки "⁉️ Помощь".
    Присылает контакт администратора или менеджера для консультации по возможным проблемам.

    :param message: Объект класса Message.
    """

    await message.answer(
        text='🪖 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 - <a href="https://t.me/splityandexx">НАПИСАТЬ</a>',
        disable_web_page_preview=True
    )
