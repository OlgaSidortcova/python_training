import re
from model.contact import Contact
from random import randrange


def test_phones_on_contact_view_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="test", firstname="first name333", home_phone="1-23",
                     work_phone="+777", email="fd@f.j", email2="b-d353f@b.fd", email3="b_d-f@b.rt"))
    contacts = db.get_contact_list()
    #for contact in contacts:
    #    index = contacts.index(contact)
    i = len(contacts)
    for index in range(1, len(contacts)):
        contact_from_db = contacts[index-1]
        id = contact_from_db.id

        contact_from_home_page = app.contact.get_some_by_id(id)

        #contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

        assert contact_from_db == contact_from_home_page

        #assert merge_phones_for_edit_page(contact_from_view_page) == merge_phones_for_edit_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                    filter(lambda x: x is not None, [contact.home_phone, contact.mobile_phone, contact.work_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                    filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))


def merge_phones_for_edit_page(contact):
    return "\n".join(filter(lambda x: x != "",
                    filter(lambda x: x is not None, [contact.home_phone, contact.mobile_phone, contact.work_phone])))
