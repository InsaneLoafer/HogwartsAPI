#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/26 15:22
# @Author   : ZhangTao
# @File     : test_backend.py
from datetime import datetime

import requests


def test_testcase_get():
    testcase_url = 'http://127.0.0.1:4444/testcase'
    r = requests.post(
        testcase_url,
        json={
            'name': f'case1{datetime.now().isoformat()}',
            'description': 'description1',
            'steps': ['1', '2', '3']
        }
    )
    assert r.status_code == 200
    r = requests.get(testcase_url)
    print(r.json())
    assert r.json()['body']

def test_task_get():
    testcase_url = 'http://127.0.0.1:4444/taskservice'
    r = requests.post(
        testcase_url,
        json={
            'name': f'task1{datetime.now().isoformat()}',
            'description': 'description2',
        }
    )
    assert r.status_code == 200
    r = requests.get(testcase_url)
    print(r.json())
    assert r.json()['body']

