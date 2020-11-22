#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 19:57
# @Author   : ZhangTao
# @File     : test_auth.py
import requests
from requests.auth import HTTPBasicAuth
def test_auth():
    res = requests.get('https://httpbin.testing-studio.com/basic-auth/Insane/123',
                       auth = HTTPBasicAuth('Insane', '123'))
    print(res.text)