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

    def test_tag_list(self):
        r = self.tag.get_taglist()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

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