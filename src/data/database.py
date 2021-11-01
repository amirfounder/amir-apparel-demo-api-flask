from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
  'postgresql://postgres:root@localhost:5432/postgres',
  echo=True
)

session = scoped_session(
  sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    bind=engine
  )
)

Base = declarative_base()
Base.query = session.query_property()
