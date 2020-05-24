from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_in_group(app):
    groups = orm.get_group_list()
    target_contact = None
    if len(groups) == 0:
        group = Group(name="888", header='8888', footer='88888')
        app.group.create(group)
        target_group = orm.get_group_list()[0]
    else:

        for group in groups:
            contacts = orm.get_contacts_not_in_group(Group(id=group.id))
            if len(contacts) != 0:
                target_contact = contacts[0]
                target_group = group
    
    if target_contact is None:
        contact = Contact(firstname="FirstnamejujUFirstname", lastname="LastnamehixLastname",
                          email="emailcgxPJLtRS MHsUDemail", home_phone="529")
        app.contact.create(contact)
        target_contact = sorted(orm.get_contact_list(), key=Contact.id_or_max)[len(orm.get_contact_list())-1]
        target_group = orm.get_group_list()[0]

    old_groups = orm.get_groups_for_contact(Contact(id=target_contact.id))
    app.contact.add_in_group(target_contact, target_group)
    new_groups = orm.get_groups_for_contact(Contact(id=target_contact.id))
    new_groups.remove(target_group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
