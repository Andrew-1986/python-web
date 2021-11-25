from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.query import Query
from models import PhoneBook, Emails, Phones, Addresses


def test():
    engine = create_engine('sqlite:///phonebook.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    ph = PhoneBook(name = 'Jack', birthday = '1983-05-08')
    ph.addresses = [Addresses(address = 'Kyiv'),]
    ph.phones = [Phones(phone = '1234567890'),]
    ph.emails = [Emails(email = 'jack@gmail.com')]
    session.add(ph)
    session.commit()

    print(session.query(PhoneBook).count())
    print(session.query(Emails).count())

    ph1 = session.query(PhoneBook).filter(PhoneBook.id == ph.id).one()

    print(ph1.emails[0].email)

    result = session.query(PhoneBook).join(Addresses).filter(Addresses.address.like('Kyiv')).all()

    for ph in result:
        print(ph.name)

    session.delete(ph1)

    session.commit()

    print(session.query(PhoneBook).count())
    print(session.query(Emails).count())

    session.close()


if __name__ == '__main__':
    test()