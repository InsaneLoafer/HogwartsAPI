#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/1 22:34
# @Author   : ZhangTao
# @File     : test_tags.py
import pytest
from assignment.wx_work1.tags import Tag

class TestTag:
    def setup_class(self):
        self.tag = Tag()
        self.tag.get_token()

    # 测试查看标签列表
    def test_tag_list(self):
        r = self.tag.get_taglist()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    # 测试创建标签
    @pytest.mark.parametrize("group_name, tag_names", [
        ["group1", [{'name': 'tag1'}]],
        ["group2", [{'name': 'tag2'}, {'name': 'tag3'}]],
    ])
    def test_tag_add(self, group_name, tag_names):
        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        # assert r.json()['errcode'] == 0
        r = self.tag.get_taglist()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        # 验证列表中是否有所添加的标签
        group = [group for group in r.json()['tag_group'] if group['group_name'] == group_name][0]
        tags = [{'name': tag['name']} for tag in group['tag']]
        print(group)
        print(tags)
        assert group['group_name'] == group_name
        assert tags == tag_names

    # 测试不支持创建空标签组
    def test_tag_add_fail(self):
        r = self.tag.add('', '')
        assert r.status_code == 200
        assert r.json()['errcode'] != 0

    # 测试编辑标签
    @pytest.mark.parametrize("old_name, new_name, order", [
        ['group1', 'Insane1', 1],
        ['tag1', 'TagInsane1', 2]
    ])
    def test_edit_tag(self, old_name, new_name, order):
        r= self.tag.edit(old_name, new_name, order)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    # 测试删除标签
    @pytest.mark.parametrize("tag_name", [
        "tag1", "tag2", "tag3"
    ])
    def test_tag_delete(self, tag_name):
        r = self.tag.delete_by_tagname(tag_name)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0


    # 测试删除标签组
    @pytest.mark.parametrize("group_name", [
        "group1", "group2"
    ])
    def test_group_delete(self, group_name):
        r = self.tag.delete_by_tagname(group_name)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

