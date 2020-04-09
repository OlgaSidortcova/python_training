# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):

    app.contact.create(Contact(firstname="first name", middlename="middle name", lastname="last name",
                       company="company", address="address", home_phone="home phone",
                       mobile_phone="mobile phone",
                       work_phone="work phone", fax="fax", email="e-mail"))



def test_add_contact_empty_phone_and_other(app):

    app.contact.create(Contact(firstname="first name", middlename="middle name", lastname="last name",
                       company="company", address="address", home_phone="",
                       mobile_phone="",
                       work_phone="", fax="", email=""))

