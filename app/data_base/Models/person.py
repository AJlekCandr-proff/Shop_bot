from sqlalchemy import String, Float, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.data_base.Models.base import Base


class Profile(Base):
    """Класс модели таблицы в базе данных с каталогом товаров. """

    __tablename__ = 'Profile'

    name: Mapped[str] = mapped_column(String, nullable=False)
    balance: Mapped[float] = mapped_column(Float, nullable=False)
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
