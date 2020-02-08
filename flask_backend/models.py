from sqlalchemy import create_engine, Column, Integer, Unicode, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def contact_from_dict(con, model, is_creation=False):
    model.first_name = con['first_name']
    model.last_name = con['last_name']
    if is_creation:
        db.session.add(model)
        db.session.commit()
    model.emails = []
    for e in con['emails']:
        email = EmailModel(type=e['type'], address=e['address'])
        model.emails.append(email)
    model.phones = []
    for p in con['phones']:
        phone = PhoneModel(
            type=p['type'], country=p['country'], number=p['number'])
        model.phones.append(phone)
    model.addresses = []
    for a in con['addresses']:
        address = AddressModel(type=a['type'], value=a['value'])
        model.addresses.append(address)
    db.session.commit()
    return model


class ContactModel(db.Model):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(length=100))
    last_name = Column(Unicode(length=100))
    emails = relationship(
        "EmailModel", back_populates="contact", cascade="all")
    phones = relationship(
        "PhoneModel", back_populates="contact", cascade="all")
    addresses = relationship(
        "AddressModel", back_populates="contact", cascade="all")

    def __repr__(self):
        return f'Contact {self.first_name} {self.last_name}'

    @property
    def serializable(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.first_name,
            'emails': self.emails.serializable,
            'phones': self.phones.serializable,
            'addresses': self.addresses.serializable
        }


class EmailModel(db.Model):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    type = Column(Unicode(length=50))
    address = Column(Unicode(length=100))
    contact_id = Column(Integer, ForeignKey('contacts.id'), index=True)

    contact = relationship(
        "ContactModel", back_populates="emails", cascade="all", single_parent=True)

    def __repr__(self):
        return f'{self.type} email of {self.contact}'

    @property
    def serializable(self):
        return {
            'id': self.id,
            'type': self.kind,
            'address': self.address
        }


class PhoneModel(db.Model):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    type = Column(Unicode(length=50))
    country = Column(Unicode(length=20))
    number = Column(Unicode(length=20))
    contact_id = Column(Integer, ForeignKey('contacts.id'), index=True)

    contact = relationship(
        "ContactModel", back_populates="phones", cascade="all", single_parent=True)

    def __repr__(self):
        return f'{self.type} phone of {self.contact}'

    @property
    def serializable(self):
        return {
            'id': self.id,
            'type': self.type,
            'country': self.country,
            'number': self.number
        }


class AddressModel(db.Model):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    type = Column(Unicode(length=50))
    value = Column(Unicode(length=100))
    contact_id = Column(Integer, ForeignKey('contacts.id'),
                        index=True)

    contact = relationship(
        "ContactModel", back_populates="addresses", cascade="all")

    def __repr__(self):
        return f'{self.type} address of {self.contact}'

    @property
    def serializable(self):
        return {
            'id': self.id,
            'kind': self.type,
            'value': self.value
        }
