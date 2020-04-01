# -*- coding: utf-8 -*-

import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="first name", middlename="middle name", lastname="last name",
                                    company="company", address="address", home_phone="home phone",
                                    mobile_phone="mobile phone",
                                    work_phone="work phone", fax="fax", email="e-mail"))
    app.return_to_home_page()
    app.logout()


def test_add_contact_empty_phone_and_other(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="first name", middlename="middle name", lastname="last name",
                                    company="company", address="address", home_phone="",
                                    mobile_phone="",
                                    work_phone="", fax="", email=""))
    app.return_to_home_page()
    app.logout()
