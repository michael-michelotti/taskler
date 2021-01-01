import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine(f'postgresql://postgres:{os.environ["PG_PASS"]}@localhost:5432/tasklerdb')
db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import taskler.models
    Base.metadata.create_all(bind=engine)


init_db()
