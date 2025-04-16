from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.db_settings import db_settings

engine = create_engine(db_settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
