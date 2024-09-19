from sqlalchemy import select, update, insert

from .Models.catalog import Catalog
from .Models.person import Profile
from app.bot_settings import session_maker


async def select_catalog() -> list[tuple[str, float, int]]:
    """
    Асинхронный метод работы с базой данных.
    Берет из таблицы каталога элементы.

    :return: Список кортежей (Название, цена и ID товара).
    """

    async with session_maker() as session:
        query = select(*[Catalog.title_product, Catalog.Cost, Catalog.id]).select_from(Catalog)

        result = await session.execute(query)

        return result


async def select_product(product_id: int | str) -> Catalog:
    """
    Асинхронный метод работы с базой данных.
    Берет из таблицы каталога отдельный товар и информацию о нем.

    :return: Класс Catalog.
    """

    async with session_maker() as session:
        query = select(Catalog).where(Catalog.id == product_id)

        result = await session.execute(query)

        result = result.fetchone()[0]
        return result


async def select_profile(user_id: int | str) -> Profile:
    """
    Асинхронный метод работы с базой данных.
    Берет из таблицы профиль отдельного пользователя.

    :return: Класс Profile.
    """

    async with session_maker() as session:
        query = select(Profile).where(Profile.user_id == user_id)

        result = await session.execute(query)

        result = result.fetchone()[0]
        return result


async def update_balance(user_id: int, balance: float) -> None:
    """
    Асинхронный метод работы с базой данных.
    Обновляет и перезаписывает баланс пользователя.

    :param user_id: Telegram ID пользователя.
    :param balance: Новой (обновленный) баланс.
    """

    async with session_maker() as session:
        query = update(Profile).where(Profile.user_id == user_id).values(balance=balance)

        await session.execute(query)

        return await session.commit()


async def add_user(user_id: int, name: str) -> None:
    """
    Асинхронный метод работы с базой данных.
    Добавляет профиль пользователя в базу данных.

    :param user_id: Telegram ID пользователя.
    :param name: Имя пользователя в Telegram.
    """

    async with session_maker() as session:
        query = insert(Profile).values(balance=0.0, user_id=user_id, name=name).prefix_with('OR IGNORE')

        await session.execute(query)

        await session.commit()
