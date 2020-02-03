from sqlalchemy import Column, Integer, Unicode, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class ContactModel(BaseModel):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(length=100))
    last_name = Column(Unicode(length=100))
    emails = relationship(
        "EmailModel", back_populates="contact", cascade="all, delete-orphan")
    phones = relationship(
        "PhoneModel", back_populates="contact", cascade="all, delete-orphan")
    addresses = relationship(
        "AddressModel", back_populates="contact", cascade="all, delete-orphan")

    def __repr__(self):
        return f'Contact {self.first_name} {self.last_name}'


class EmailModel(BaseModel):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    kind = Column(Unicode(length=100))
    address = Column(Unicode(length=100))
    contact_id = Column(Integer, ForeignKey('contacts.id'), index=True)

    contact = relationship(
        "ContactModel", back_populates="emails", cascade="all, delete-orphan")

    def __repr__(self):
        return f'{self.kind} email of {self.contact}'


class PhoneModel(BaseModel):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    kind = Column(Unicode(length=100))
    number = Column(Unicode(length=100))
    contact_id = Column(Integer, ForeignKey('contacts.id'), index=True)

    contact = relationship(
        "ContactModel", back_populates="phones", cascade="all, delete-orphan")

    def __repr__(self):
        return f'{self.kind} phone of {self.contact}'


class AddressModel(BaseModel):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    kind = Column(Unicode(length=100))
    value = Column(Unicode(length=100))
    contact_id = Column(Integer, ForeignKey('contacts.id'), index=True)

    contact = relationship(
        "ContactModel", back_populates="addresses", cascade="all, delete-orphan")

    def __repr__(self):
        return f'{self.kind} address of {self.contact}'
