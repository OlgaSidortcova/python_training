# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_name(prefix, maxlen):
    symbols = string.ascii_letters + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits * 5 + string.punctuation
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(lastname="", firstname="", email="", home_phone="")] + [
    Contact(firstname=random_name("Fname", 10), lastname=random_name("Lname", 14), email=random_name("email", 18), home_phone=random_phone(10), email2=random_name("email", 18), work_phone=random_phone(10))
    for i in range(10)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact1(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname=random_name("FirstnamejujUFirstname", 10), lastname="LastnamehixLastname",
            email="emailcgxPJLtRS MHsUDemail", home_phone="529")

    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
