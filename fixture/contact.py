import time
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.enter_value(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(
                wd.find_elements_by_xpath("//input[@value='Delete']")) > 0):
            wd.find_element_by_link_text("home").click()

    def delete_first(self):
        self.delete_some(0)

    def delete_some_contact(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_some(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(1)
        self.contact_cache = None

    def modify_first(self, contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_first()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.enter_value(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_some(self, contact, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_some(index)
        xpath = "//table[@id='maintable']/tbody/tr[" + str(index + 2) + "]/td[8]/a/img"
        wd.find_element_by_xpath(xpath).click()
        self.enter_value(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_some(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def enter_value(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)

        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)

        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            count = len(wd.find_elements_by_name("selected[]"))
            for i in range(2, count+2):
                xpath = "//table[@id='maintable']/tbody/tr[" + str(i) + "]/td[2]"
                lastname = wd.find_element_by_xpath(xpath).text
                xpath = "//table[@id='maintable']/tbody/tr[" + str(i) + "]/td[3]"
                firstname = wd.find_element_by_xpath(xpath).text
                xpath = "//table[@id='maintable']/tbody/tr[" + str(i) + "]/td[1]/input"
                id = wd.find_element_by_xpath(xpath).get_attribute("value")
                self.contact_cache.append(Contact(lastname=str(lastname), firstname=firstname, id=id))
        return list(self.contact_cache)
