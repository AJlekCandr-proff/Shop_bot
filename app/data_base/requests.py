from sqlalchemy import select, update, insert

from .Models.catalog import Catalog
from .Models.person import Profile
from app.bot_settings import session_maker


async def select_catalog() -> list[tuple[str, float, int]]:
    async with session_maker() as session:
        query = select(*[Catalog.title_product, Catalog.Cost, Catalog.id]).select_from(Catalog)

        result = await session.execute(query)

        return result


async def select_product(product_id: int | str) -> any:
    async with session_maker() as session:
        query = select(Catalog).where(Catalog.id == product_id)

        result = await session.execute(query)

        result = result.fetchone()[0]
        return result


async def select_profile(user_id: int | str) -> any:
    async with session_maker() as session:
        query = select(Profile).where(Profile.user_id == user_id)

        result = await session.execute(query)

        result = result.fetchone()[0]
        return result


async def update_balance(user_id: int, balance: float) -> None:
    async with session_maker() as session:
        query = update(Profile).where(Profile.user_id == user_id).values(balance=balance)

        await session.execute(query)

        return await session.commit()


async def add_user(user_id: int, name: str) -> None:
    async with session_maker() as session:
        query = insert(Profile).values(balance=0.0, user_id=user_id, name=name).prefix_with('OR IGNORE')

        await session.execute(query)

        await session.commit()
