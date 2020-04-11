# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first(Contact(firstname="first name333", middlename="123",
                       mobile_phone="mobile phone333",
                       work_phone="work phone333", fax="fax333", email="e-mail333"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)