# -*- coding: utf-8 -*-
import unittest

from group import Group
from application import Application

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="test1", header="test2", footer="test3"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.open_home_page()
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
