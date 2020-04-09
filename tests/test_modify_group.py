# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_first_group(app):

    app.group.modify_first(Group(name="test111", header="test222", footer="test333"))



def test_modify_first_group_name(app):

    app.group.modify_first(Group(name="New group"))


def test_modify_first_group_header(app):

    app.group.modify_first(Group(header="New header"))

