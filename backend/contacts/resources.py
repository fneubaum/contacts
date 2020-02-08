import json
import falcon
from marshmallow import ValidationError
from falcon_autocrud.resource import CollectionResource, SingleResource
from .models import ContactModel, ContactListModel, EmailModel, AddressModel, PhoneModel
from .schemas import ContactSchema, ContactListSchema


class ContactListResource(CollectionResource):
    model = ContactModel
    allow_put_insert = True
    allow_subresources = True
    methods = ['GET', 'POST', 'PUT', 'PATCH']

    def before_post(self, req, resp, db_session, resource, *args, **kwargs):
        try:
            ContactSchema().load(req.context['doc'])
        except ValidationError as err:
            raise falcon.HTTPBadRequest('Malformed JSON', err.messages)


class ContactResource(SingleResource):
    model = ContactModel
    allow_subresources = True
    allowed_included = ['emails']
    extra_select = [EmailModel.address, EmailModel.kind]

    def on_get(self, req, resp, *args, **kwargs):
        with session_scope(self.db_engine, sessionmaker_=self.sessionmaker, **self.sessionmaker_kwargs) as db_session:
            result = db_session.query(self.model).join(EmailModel)
            req.context['result'] = result
