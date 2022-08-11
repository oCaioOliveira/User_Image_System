from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pathlib import Path

db_path = Path(__file__).parent.joinpath('db.sqlite3')

engine = create_engine(
    f'sqlite:///{db_path.as_posix()}',
    connect_args={'check_same_thread': False}
)

SessionLocal = Session(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()