from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from WebApp.persistence.settings import Settings


SQLALCHEMY_DATABASE_URL = Settings.DATABASE_URL
print("Database URL is ", SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
