import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Db_URL = "sqlite:///portfolio.db"

engine = sqlalchemy.create_engine(Db_URL, connect_args={"check_same_thread": False})
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
