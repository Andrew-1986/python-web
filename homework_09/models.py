from datetime import datetime
import re
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql.expression import null


Base = declarative_base()


class PhoneBook(Base):
    __tablename__ = "phonebook"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    __birthday = Column("birthday",DateTime, nullable=True)

    emails = relationship("Emails", cascade="all, delete", backref="phonebook")
    phones = relationship("Phones", cascade="all, delete", backref="phonebook")
    addresses = relationship("Addresses", cascade="all, delete", backref="phonebook")

    @hybrid_property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, new_value):
        if not new_value:
            self.__birhday = new_value
        else:
            if not re.match('\d{4}-\d{2}-\d{2}', new_value):
                raise ValueError('Birthday must be "yyyy-mm-dd" format')
            b_year, b_month, b_day = new_value.split('-')
            if int(b_month) > 12 or int(b_day) > 31:
                raise ValueError(
                    'Month must be in "01-12" day must be in "01-31"')
            else:
                self.__birthday = datetime(int(b_year), int(b_month), int(b_day))


class Emails(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True)
    __email = Column("email", String(50), nullable=False)
    type = Column(Integer, default=0)
    person_id = Column(Integer, ForeignKey(PhoneBook.id, ondelete="CASCADE"))


    @hybrid_property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_value):
        if not new_value:
            self.__email = new_value
        else:
            if not re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', new_value):
                raise ValueError(
                    'Email not valid format, must be "name@domenname.com"')
            else:
                self.__email = new_value


class Phones(Base):
    __tablename__ = "phones"
    id = Column(Integer, primary_key=True)
    __phone = Column("phone", String(11), nullable=False)
    type = Column(Integer, default=0)
    person_id = Column(Integer, ForeignKey(PhoneBook.id, ondelete="CASCADE"))

    @hybrid_property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_value):
        if not re.match('\d{10}$', new_value):
            raise ValueError('Phone number must have 10 digits')
        else:
            self.__phone = new_value


class Addresses(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    address = Column(String(250), nullable=False)
    type = Column(Integer, default=0)
    person_id = Column(Integer, ForeignKey(PhoneBook.id, ondelete="CASCADE"))