# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first(Group(name="test111", header="test222", footer="test333"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    new_groups = app.group.get_group_list()
    app.group.modify_first(Group(name="New group"))
    assert len(old_groups) == len(new_groups)


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
