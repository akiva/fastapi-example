import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

DATABASE_URL = (
    os.getenv('TEST_DATABASE_URL') if os.getenv('env') == 'test'
    else os.getenv('DATABASE_URL')
)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
database = Database(DATABASE_URL)
Base = declarative_base()
