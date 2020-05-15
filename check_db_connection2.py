from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    a = db.get_group_list()
    b = db.get_contact_list()
    c = db.get_contacts_in_group

    l = db.get_contacts_in_group(Group(id='298'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass#db.destroy()




