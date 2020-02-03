from marshmallow import Schema, fields, validate


class ContactSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    emails = fields.List(fields.Nested(EmailSchema()),
                         validate=validate.Length(min=1))
    phones = fields.List(fields.Nested(PhoneSchema()),
                         validate=validate.Length(min=1))
    emails = fields.List(fields.Nested(EmailSchema()),
                         validate=validate.Length(min=1))


class EmailSchema(Schema):
    kind = fields.String(validate=validate.OneOf(
        ['Work', 'Home', 'School', 'Other']), required=True)
    address = fields.Email(required=True)


class PhoneSchema(Schema):
    kind = fields.String(validate=validate.OneOf(
        ['Mobile', 'Work', 'Home', 'School', 'Other']), required=True)
    number = fields.String(required=True)


class EmailSchema(Schema):
    kind = fields.String(validate=validate.OneOf(
        ['Work', 'Home', 'School', 'Other']), required=True)
    value = fields.Email(required=True)
