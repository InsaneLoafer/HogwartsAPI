#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 22:06
# @Author   : ZhangTao
# @File     : test_send.py
import yaml

from practice.multi_env_practice.env_demo import Api


class TestSend(Api):
    def test_send(self):
        print(self.send(data=yaml.safe_load(open('env.yaml'))))