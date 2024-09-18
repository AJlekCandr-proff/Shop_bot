from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder, InlineKeyboardMarkup


def categories_menu() -> InlineKeyboardMarkup:
    """
    Функция создания меню каталога (категорий).

    :return: Объект класса InlineKeyboardMarkup.
    """

    inline_markup = InlineKeyboardBuilder()

    inline_markup.add(InlineKeyboardButton(text='🟡 ЯНДЕКС СПЛИТ 🟡', callback_data='category_split'))

    return inline_markup.as_markup()


def catalog_menu(catalog: list[tuple[str, float, int]]) -> InlineKeyboardMarkup:
    """
    Функция создания меню каталога (товаров).

    :param catalog: Список-каталог товаром.
    :return: Объект класса InlineKeyboardMarkup.
    """

    inline_markup = InlineKeyboardBuilder()

    for product in catalog:
        inline_markup.row(InlineKeyboardButton(text=f'{product[0]} | Цена: {product[1]}', callback_data=str(product[2])))

    return inline_markup.as_markup()


def buy_menu() -> InlineKeyboardMarkup:
    """
    Функция создания меню-клавиатуры для покупки товара.

    :return: Объект класса InlineKeyboardMarkup.
    """

    inline_markup = InlineKeyboardBuilder()

    inline_markup.row(InlineKeyboardButton(text='Купить 💳', callback_data='Buy'))

    return inline_markup.as_markup()
