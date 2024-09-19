from sqlalchemy import String, Float, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.data_base.Models.base import Base


class Profile(Base):
    """Класс модели таблицы в базе данных с профилями пользователей. """

    __tablename__ = 'Profile'

    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    balance: Mapped[float] = mapped_column(Float, nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
