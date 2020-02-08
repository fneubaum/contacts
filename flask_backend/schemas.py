from marshmallow import Schema, fields, validate, post_load
from models import ContactModel, EmailModel, AddressModel


class EmailSchema(Schema):
    type = fields.String(validate=validate.OneOf(
        ['', 'Work', 'Home', 'School', 'Other']), required=True)
    address = fields.Email(required=True, validate=validate.Length(min=1))


class PhoneSchema(Schema):
    type = fields.String(validate=validate.OneOf(
        ['', 'Mobile', 'Work', 'Home', 'School', 'Other']), required=True)
    country = fields.String(required=True)
    number = fields.String(required=True, validate=validate.Length(min=1))


class AddressSchema(Schema):
    type = fields.String(validate=validate.OneOf(
        ['', 'Work', 'Home', 'School', 'Other']), required=True)
    value = fields.String(required=True)


class ContactSchema(Schema):
    id = fields.Integer(strict=True)
    first_name = fields.String(required=True, validate=validate.Length(min=1))
    last_name = fields.String(required=True, validate=validate.Length(min=1))
    emails = fields.List(fields.Nested(EmailSchema()),
                         validate=validate.Length(min=1), required=True,)
    phones = fields.List(fields.Nested(PhoneSchema()),
                         validate=validate.Length(min=1), required=True,)
    addresses = fields.List(fields.Nested(
        AddressSchema(), required=True,), required=True,)


class ContactListSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(min=1))
    contacts = fields.List(fields.Nested(ContactSchema()), required="True")
