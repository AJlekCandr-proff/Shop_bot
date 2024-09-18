from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardBuilder


def main_keyboard() -> ReplyKeyboardMarkup:
    """
    Функция создания главной клавиатуры-меню.

    :return: Объект класса ReplyKeyboardMarkup.
    """

    keyboard = ReplyKeyboardBuilder()

    keyboard.row(KeyboardButton(text='🛒 Купить'))

    keyboard.row(KeyboardButton(text='📘 Правила'), KeyboardButton(text='💰 Пополнить'))
    keyboard.row(KeyboardButton(text='👤 Профиль'), KeyboardButton(text='⁉️ Помощь'))

    return keyboard.as_markup(resize_keyboard=True)
