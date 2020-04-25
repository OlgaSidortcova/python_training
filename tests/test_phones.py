import re
from model.contact import Contact
from random import randrange


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test", firstname="first name333", home_phone="1-23",
                        work_phone="+777"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phone_from_home_page == merge_phone_like_on_home_page(contact_from_edit_page)
    #assert contact_from_home_page.home_phone == clear(contact_from_edit_page.home_phone)
    #assert contact_from_home_page.mobile_phone == clear(contact_from_edit_page.mobile_phone)
    #assert contact_from_home_page.work_phone == clear(contact_from_edit_page.work_phone)


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test", firstname="first name333", home_phone="1-23",
                     work_phone="+777"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    a = contact_from_view_page
    a1 = merge_phone_for_edit_page(contact_from_view_page)
    b = merge_phone_for_edit_page(contact_from_edit_page)
    b1 = contact_from_edit_page
    assert merge_phone_for_edit_page(contact_from_view_page) == merge_phone_for_edit_page(contact_from_edit_page)

    #assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    #assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    #assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phone_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                    filter(lambda x: x is not None, [contact.home_phone, contact.mobile_phone, contact.work_phone]))))


def merge_phone_for_edit_page(contact):
    return "\n".join(filter(lambda x: x != "",
                    filter(lambda x: x is not None, [contact.home_phone, contact.mobile_phone, contact.work_phone])))
