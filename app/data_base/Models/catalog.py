from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.data_base.Models.base import Base


class Catalog(Base):
    """Класс модели таблицы в базе данных с каталогом товаров. """

    __tablename__ = 'Catalog'

    title_product: Mapped[str] = mapped_column(String, nullable=Float)
    Cost: Mapped[float] = mapped_column(Float, nullable=False)
