# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test", firstname="first name333"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="first name333", lastname="123",
                       mobile_phone="mobile phone333",
                       work_phone="work phone333", fax="fax333", email="e-mail333")
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    print(old_contacts)
    print(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_first_and_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test", firstname="first name333"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="555", lastname="777")
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    print(old_contacts)
    print(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)