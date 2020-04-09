# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_first_contact(app):

    app.contact.modify_first(Contact(firstname="first name333", middlename="", lastname="",
                       company="", address="", home_phone="",
                       mobile_phone="mobile phone333",
                       work_phone="work phone333", fax="fax333", email="e-mail333"))


