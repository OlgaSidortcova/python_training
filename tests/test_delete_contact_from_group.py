from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from(app, db):
    group_list_with_contacts = db.get_group_list_with_contacts()
    if len(group_list_with_contacts) != 0:
        group = group_list_with_contacts[0]
        contacts = orm.get_contacts_in_group(group)
        contact = random.choice(contacts)

    elif len(db.get_group_list()) == 0:
        group = create_group(app, db)
        contact = create_contact(app, group)

    else:
        groups = orm.get_group_list()
        group = random.choice(groups)
        contact = create_contact(app, group)

    old_contacts = db.get_contact_list()
    l_before = orm.get_contacts_in_group(Group(id=group.id))

    app.contact.delete_some_contact_by_id(contact.id)
    old_contacts.remove(contact)

    new_contacts = db.get_contact_list()
    l_after = orm.get_contacts_in_group(Group(id=group.id))
    assert len(l_before) == len(l_after) + 1
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def create_contact(app, group):
    contact = Contact(lastname="qqqq", firstname='bbb', address='ccccc', group=group.name)
    app.contact.create(contact)
    contacts = orm.get_contacts_in_group(group)
    contact = contacts[0]
    return contact


def create_group(app, db):
    group = Group(name="888", header='8888', footer='88888')
    app.group.create(group)
    group = db.get_group_list()[0]
    return group
