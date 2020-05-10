# -*- coding: utf-8 -*-

from model.contact import Contact
import random
from random import randrange


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="test", firstname="first name333"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    id = old_contact.id
    index = old_contacts.index(old_contact)
    new_contact = Contact(firstname="first name333", lastname="123",
                       mobile_phone="mobile phone333",
                       work_phone="work phone333", fax="fax333", email="e-mail333", id=id)

    app.contact.modify_some_by_id(new_contact, id)
    new_contacts = db.get_contact_list()
    old_contacts[index] = new_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_modify_first_contact_first_and_last_name(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(lastname="test", firstname="first name333"))
#    old_contacts = app.contact.get_contact_list()
#    index = randrange(len(old_contacts))
#    contact = Contact(firstname="555", lastname="777")
#    contact.id = old_contacts[index].id
#    app.contact.modify_some_by_index(contact, index)
#    assert len(old_contacts) == app.contact.count()
#    new_contacts = app.contact.get_contact_list()
#    old_contacts[index] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)