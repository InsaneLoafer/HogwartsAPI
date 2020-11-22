#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 19:39
# @Author   : ZhangTao
# @File     : test_cookie.py
import requests

# 使用header参数
def test_demo():
    url = 'https://httpbin.testing-studio.com/cookies'
    header = {
        'Cookie': 'hogwarts=school',
        'User-Agent': 'InsaneLoafer'
    }
    r = requests.get(url=url, headers=header)
    print(r.request.headers)

# 使用cookies参数
def test_cookies():
    url = 'https://httpbin.testing-studio.com/cookies'
    header = {
        'User-Agent': 'InsaneLoafer'
    }
    cookie_data = {
        'hogwarts': 'school',
        'student': 'ZT'
    }
    r = requests.get(url=url, headers=header, cookies=cookie_data)
    print(r.request.headers)
