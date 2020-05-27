# -*- coding: utf-8 -*-

from model.group import Group
import pytest


def test_add_group(app, db, json_groups, check_ui):
    #with pytest.allure.step("Given a group list"):
    group = json_groups
    #with pytest.allure.step(" When I add group to the list"):
    old_groups = db.get_group_list()
    app.group.create(group)

    new_groups = db.get_group_list()
    old_groups.append(group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
