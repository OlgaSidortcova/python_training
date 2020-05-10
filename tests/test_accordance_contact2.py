import re
from model.contact import Contact
from random import randrange


def test_phones_on_contact_view_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="test", firstname="first name333", home_phone="1-23",
                     work_phone="+777", email="fd@f.j", email2="b-d353f@b.fd", email3="b_d-f@b.rt"))
    contacts = db.get_contact_list()
    for contact_from_db in contacts:
        id = contact_from_db.id
        contact_from_home_page = app.contact.get_some_by_id(id)
        assert contact_from_db == contact_from_home_page
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(
            contact_from_db)
        assert contact_from_home_page.all_phone_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.address == contact_from_db.address


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                    filter(lambda x: x is not None, [contact.home_phone, contact.mobile_phone, contact.work_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                    filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))


def merge_address_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                    filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))


def merge_phones_for_edit_page(contact):
    return "\n".join(filter(lambda x: x != "",
                    filter(lambda x: x is not None, [contact.home_phone, contact.mobile_phone, contact.work_phone])))

