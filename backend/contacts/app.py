import falcon
from .resources import ContactResource
from .utils import create_tables

create_tables()
api = application = falcon.API()
contact_list = ContactResource()
api.add_route('/contact', contact_list, suffix='list')
