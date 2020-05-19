from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    c1 = Contact(id='421')
    g1 = Group(id='421')
    l = db.get_contacts_in_groups()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass#db.destroy()




