from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_in_group(app, db):
    old_contacts = db.get_contact_list()
    groups = db.get_group_list()
    if len(groups) == 0:
        group = Group(name="888", header='8888', footer='88888')
        app.group.create(group)
        group = db.get_group_list()[0]
    else:
        group = random.choice(groups)

    l_before = len(orm.get_contacts_in_group(Group(id=group.id)))
    contact = Contact(firstname="FirstnamejujUFirstname", lastname="LastnamehixLastname",
                      email="emailcgxPJLtRS MHsUDemail", home_phone="529", group=group.name)

    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    l_after = len(orm.get_contacts_in_group(Group(id=group.id)))
    old_contacts.append(contact)
    assert l_before + 1 == l_after
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

