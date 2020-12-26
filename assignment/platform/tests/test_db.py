#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/26 16:03
# @Author   : ZhangTao
# @File     : test_db.py
from assignment.platform.src.backend import db


def test_create_table():
    db.create_all()