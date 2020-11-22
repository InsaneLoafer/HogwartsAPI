#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/20 19:13
# @Author   : ZhangTao
# @File     : test_demo.py
import pystache
import requests
from hamcrest import *

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

    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={'h': 'InsaneLoafer'})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']['H'] == 'InsaneLoafer'

    def test_post_json(self):
        payload = {
            'level': 1,
            'name': 'InsaneLoafer'
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_xml(self):
        xml = """<?xml version='1.0' encoding='utf-8'?>
        <a>$</a>"""
        headers = {'Content-Type': 'application/xml'}
        r = requests.post('https://httpbin.testing-studio.com/post', headers=headers)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_mustache(self):
        a = pystache.render(
            'Hi {{person}}!',
            {'person': 'InsaneLoafer'}
        )
        print(a)

    def test_hogwarts_json(self):
        url = 'https://home.testing-studio.com/catagories.json'
        r= requests.get(url)
        print(r.text)
        fact = r.json()['catagory_list']['catagories'][0]['name']
        print(fact)
        assert  fact == '霍格沃兹测试学院公众号'

    def test_hamcrest(self):
        url = 'https://home.testing-studio.com/catagories.json'
        r= requests.get(url)
        print(r.text)
        fact = r.json()['catagory_list']['catagories'][0]['name']
        print(fact)
        assert_that(fact, equal_to('霍格沃兹测试学院公众号'))
