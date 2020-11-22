#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 20:46
# @Author   : ZhangTao
# @File     : test_auth_page.py
from unittest import TestCase
from practice.auth_practice.auth_page import ApiRequest


class TestApiRequest(TestCase):
    req_data = {
        'method': 'get',
        'url': 'http://127.0.0.1:9999/demo1.txt',
        'headers': None,
        'encoding': 'base64'
    }
    def test_send(self):
        ar = ApiRequest()
        print(ar.send(self.req_data))

