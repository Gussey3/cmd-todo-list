from functools import cached_property
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: str
    postgres_db: str
    schema: str
    db_source: str

    @cached_property
    def database_url(self) -> str:
        dsn = PostgresDsn(
            f"{self.schema}://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )
        return str(dsn)

    model_config = SettingsConfigDict(env_file=Path(".env"))


settings = Settings()
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
