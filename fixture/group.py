from model.group import Group
import allure

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    @allure.step('I add a group: "{group}" to the list')
    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.enter_value(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    @allure.step('I delete a group by id: "{id}" to the list')
    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        # select
        self.select_group_by_id(id)
        # submit
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    @allure.step('I delete a group by index: "{index}" to the list')
    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        # select
        self.select_group_by_index(index)
        # submit
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    @allure.step('I delete the first group')
    def delete_first(self):
        self.delete_group_by_index(0)
        #wd = self.app.wd
        #self.open_groups_page()
        # select
        #self.select_first_group()
        # submit
        #wd.find_element_by_name("delete").click()
        #self.return_to_group_page()
        #self.group_cache = None

    @allure.step('I select a group by index: "{index}"')
    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    @allure.step('I select a group by id: "{id}"')
    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    @allure.step('I select the first group')
    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    @allure.step('I modify the first group')
    def modify_first(self, group):
        self.modify_group_by_index(group, 0)

    @allure.step('I modify the group by index: {index}')
    def modify_group_by_index(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        # fill group form
        self.enter_value(group)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    @allure.step('I modify a group: "{group}" with id: {id}')
    def modify_group_by_id(self, group, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("edit").click()
        # fill group form
        self.enter_value(group)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    @allure.step('I enter the value for a group: "{group}"')
    def enter_value(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    @allure.step('I calculate the group count')
    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=str(text), id=id))
        return list(self.group_cache)
