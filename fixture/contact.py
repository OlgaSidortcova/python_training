import time
from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select
import allure

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php"):
            wd.find_element_by_link_text("add new").click()

    @allure.step('I add a contact: "{contact}" to the list')
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

    @allure.step('I delete a first contact')
    def delete_first(self):
        self.delete_some(0)

    @allure.step('I delete a contact with id: "{id}"')
    def delete_some_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_some_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(1)
        self.contact_cache = None

    @allure.step('I delete a contact with index: "{index}"')
    def delete_some_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_some_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(1)
        self.contact_cache = None

    @allure.step('I modify a contact: "{contact}"')
    def modify_first(self, contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_first()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.enter_value(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    @allure.step('I modify a contact with index: "{index}"')
    def modify_some_by_index(self, contact, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_some_by_index(index)
        xpath = "//table[@id='maintable']/tbody/tr[" + str(index + 2) + "]/td[8]/a/img"
        wd.find_element_by_xpath(xpath).click()
        self.enter_value(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    @allure.step('I modify a contact with id: "{id}"')
    def modify_some_by_id(self, contact, id):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_element_by_xpath("//input[@id='%s']/../.." % id)
        row.find_elements_by_tag_name("td")[7].click()
        self.enter_value(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    @allure.step('I select a contact with index: "{index}"')
    def select_some_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    @allure.step('I select a contact with id: "{id}"')
    def select_some_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='%s']" % id).click()

    @allure.step('I get a contact with id: "{id}"')
    def get_some_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='%s']" % id)
        self.open_home_page()
        row = wd.find_element_by_xpath("//input[@id='%s']/../.." % id)
        cells = row.find_elements_by_tag_name("td")
        firstname = cells[2].text
        lastname = cells[1].text
        id = cells[0].find_element_by_tag_name("input").get_attribute("value")
        all_phones = cells[5].text
        all_emails = cells[4].text
        contact = Contact(lastname=lastname, firstname=firstname, id=id,
                                              all_phone_from_home_page=all_phones,
                                              all_emails_from_home_page=all_emails)

        return contact

    @allure.step('I enter a contact: "{contact}"')
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
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("phone2", contact.phone2)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    @allure.step('I calculate contact count')
    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    @allure.step('I get a contact list')
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  all_phone_from_home_page=all_phones, all_emails_from_home_page=all_emails))
            # below is my_way
            # count = len(wd.find_elements_by_name("selected[]"))
            # for i in range(2, count+2):
            #   xpath = "//table[@id='maintable']/tbody/tr[" + str(i) + "]/td[2]"
            #  lastname = wd.find_element_by_xpath(xpath).text
            #  xpath = "//table[@id='maintable']/tbody/tr[" + str(i) + "]/td[3]"
            #  firstname = wd.find_element_by_xpath(xpath).text
            #  xpath = "//table[@id='maintable']/tbody/tr[" + str(i) + "]/td[1]/input"
            # id = wd.find_element_by_xpath(xpath).get_attribute("value")
            # self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cache)

    @allure.step('I open a contact to edit by index: "{index}"')
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    @allure.step('I open a contact to view by index: "{index}"')
    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    @allure.step('I get a contact info from edit page by index: "{index}"')
    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=first_name, lastname=last_name, id=id, home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, email=email, email2=email2, email3=email3, phone2=phone2)

    @allure.step('I get a contact info from view page by index: "{index}"')
    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        if re.search("H: (.*)", text) is None:
            home_phone = None
        else:
            home_phone = re.search("H: (.*)", text).group(1)
        if re.search("W: (.*)", text) is None:
            work_phone = None
        else:
            work_phone = re.search("W: (.*)", text).group(1)
        if re.search("M: (.*)", text) is None:
            mobile_phone = None
        else:
            mobile_phone = re.search("M: (.*)", text).group(1)
        if re.search("P: (.*)", text) is None:
            phone2 = None
        else:
            phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone, mobile_phone=mobile_phone, phone2=phone2)

    @allure.step('I add a contact: "{contact}" to a group: "{group}"')
    def add_in_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_some_by_id(contact.id)
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group.name)
        wd.find_element_by_name("add").click()
        self.open_home_page()

    @allure.step('I del a contact: "{contact}" from a group: "{group}"')
    def del_from_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        Select(wd.find_element_by_name("group")).select_by_visible_text(group.name)
        self.select_some_by_id(contact.id)
        wd.find_element_by_name("remove").click()
        self.open_home_page()
