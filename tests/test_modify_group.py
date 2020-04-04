# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="test111", header="test222", footer="test333"))
    app.session.logout()

