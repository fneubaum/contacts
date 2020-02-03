from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import BaseModel


Session = sessionmaker()
engine = create_engine('sqlite://', echo=True)
Session.configure(bind=engine)


def create_tables():
    BaseModel.metadata.create_all(engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
