from functools import lru_cache
from pathlib import Path
from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import PostgresDsn

load_dotenv(Path(".env"))


@lru_cache()
def get_database_url() -> str:
    """
    Получить url базы данных
    :return: url базы данных
    """
    user = getenv("POSTGRES_USER")
    password = getenv("POSTGRES_PASSWORD")
    host = getenv("POSTGRES_HOST")
    port = getenv("POSTGRES_PORT")
    db = getenv("POSTGRES_DB")
    schema = getenv("SCHEMA")

    dsn = PostgresDsn(f"{schema}://{user}:{password}@{host}:{port}/{db}")
    return str(dsn)


engine = create_engine(get_database_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
