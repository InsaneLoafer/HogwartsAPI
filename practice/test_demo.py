#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/20 19:13
# @Author   : ZhangTao
# @File     : test_demo.py
import requests

class TestDemo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            'level': 1,
            'name': 'InsaneLoafer'
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            'level': 1,
            'name': 'InsaneLoafer'
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

