from loguru import logger

from pydantic import SecretStr

from pydantic_settings import BaseSettings, SettingsConfigDict

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Settings(BaseSettings):
    """Хранит в себе переменные окружения проекта."""

    TELEGRAM_API_TOKEN: SecretStr
    SQLALCHEMY_URL: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf8", extra="ignore")


settings = Settings()


YandexSplitBot = Bot(token=settings.TELEGRAM_API_TOKEN.get_secret_value(), default=DefaultBotProperties(parse_mode='HTML'))


Logger = logger


engine = create_async_engine(url=settings.SQLALCHEMY_URL)


session_maker = async_sessionmaker(bind=engine, expire_on_commit=False, autocommit=False)
