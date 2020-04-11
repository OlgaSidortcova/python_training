# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="first name", middlename="middle name", lastname="last name",
                       company="company", address="address", home_phone="home phone",
                       mobile_phone="mobile phone",
                       work_phone="work phone"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_contact_empty_phone_and_other(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="first name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
