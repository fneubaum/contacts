import json
import copy
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


class JSONMiddleware(object):
    def process_request(self, req, resp):
        copy_stream = bytes([p for p in req.stream.read()])
        # print(copy_stream)
        req.json = json.load(req.stream)
        print(req.json)
        # req.stream = copy_stream

    def process_resource(self, req, resp, resource, params):
        pass

    def process_response(self, req, resp, resource, req_succeeded):
        pass
