import psycopg2

from sqlalchemy import create_engine
from sqlalchemy import URL
from app.core.config import settings
from app.db.base import Base
from app.db import models


DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,
    host=settings.DATABASE_HOST,
    port=settings.DATABASE_PORT,
    database=settings.DATABASE_NAME,
)

engine = create_engine(DATABASE_URL)


def get_db_connection():
    connection = psycopg2.connect(
        host=settings.DATABASE_HOST,
        port=settings.DATABASE_PORT,
        database=settings.DATABASE_NAME,
        user=settings.DATABASE_USER,
        password=settings.DATABASE_PASSWORD
    )
    return connection

def create_tables():
    Base.metadata.create_all(bind=engine)


