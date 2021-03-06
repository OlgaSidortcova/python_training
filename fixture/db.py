import mysql.connector
from model.group import Group
from model.contact import Contact
import allure

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def destroy(self):
        self.connection.close()

    @allure.step('Given a group list')
    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))

        finally:
            cursor.close()
        return list

    def get_group_list_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append(Group(id=str(group_id)))

        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, email, email2, email3, address, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, home, mobile, work, email, email2, email3, address, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, home_phone=home, mobile_phone=mobile, work_phone=work, email=email, email2=email2, email3=email3, address=address, phone2=phone2))

        finally:
            cursor.close()
        return list

    def get_group_by_id(self, group):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                if group.id == str(id):
                    group_new = (Group(id=str(id), name=name, header=header, footer=footer))

        finally:
            cursor.close()
        return group_new

