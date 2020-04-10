# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test"))
    app.contact.modify_first(Contact(firstname="first name333", middlename="123",
                       mobile_phone="mobile phone333",
                       work_phone="work phone333", fax="fax333", email="e-mail333"))


