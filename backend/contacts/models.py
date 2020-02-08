from sqlalchemy import create_engine, Column, Integer, Unicode, ForeignKey, MetaData, JSON, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

meta = MetaData()


class ContactListModel(BaseModel):
    __tablename__ = 'contactlists'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(length=100))

    def __repr__(self):
        return f'<Contactlist {self.name}> and {self.id}'


class ContactModel(BaseModel):
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


class EmailModel(BaseModel):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    kind = Column(Unicode(length=50))
    address = Column(Unicode(length=100))
    contact_id = Column(Integer, ForeignKey('contacts.id'), index=True)

    contact = relationship(
        "ContactModel", back_populates="emails", cascade="all", single_parent=True)

    def __repr__(self):
        return f'{self.kind} email of {self.contact}'

    @property
    def serializable(self):
        return {
            'id': self.id,
            'kind': self.kind,
            'address': self.address
        }


class PhoneModel(BaseModel):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    kind = Column(Unicode(length=50))
    number = Column(Unicode(length=20))
    contact_id = Column(Integer, ForeignKey('contacts.id'), index=True)

    contact = relationship(
        "ContactModel", back_populates="phones", cascade="all", single_parent=True)

    def __repr__(self):
        return f'{self.kind} phone of {self.contact}'

    @property
    def serializable(self):
        return {
            'id': self.id,
            'kind': self.kind,
            'number': self.number
        }


class AddressModel(BaseModel):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    kind = Column(Unicode(length=50))
    value = Column(Unicode(length=100))
    contact_id = Column(Integer, ForeignKey('contacts.id'),
                        index=True)

    contact = relationship(
        "ContactModel", back_populates="addresses", cascade="all")

    def __repr__(self):
        return f'{self.kind} address of {self.contact}'

    @property
    def serializable(self):
        return {
            'id': self.id,
            'kind': self.kind,
            'value': self.value
        }
