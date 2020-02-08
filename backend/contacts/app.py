import falcon
from .models import BaseModel
from .resources import ContactResource, ContactListResource
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import base
from falcon_autocrud.middleware import Middleware as AutoCRUDMiddleware

engine = create_engine('sqlite:///db.sqlite3', echo=True)
BaseModel.metadata.create_all(engine)
api = application = falcon.API(
    middleware=[AutoCRUDMiddleware()],)

api.add_route('/contact', ContactListResource(engine))
api.add_route('/contact/{id}', ContactResource(engine))

if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')

        httpd.serve_forever()
