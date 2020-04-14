# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test", firstname="first name333"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="first name333", lastname="123",
                       mobile_phone="mobile phone333",
                       work_phone="work phone333", fax="fax333", email="e-mail333")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_some(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_first_and_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test", firstname="first name333"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="555", lastname="777")
    contact.id = old_contacts[index].id
    app.contact.modify_some(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)