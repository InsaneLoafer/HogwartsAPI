#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/26 14:14
# @Author   : ZhangTao
# @File     : flask_app.py

from flask import Flask, escape, request, session
import os

app = Flask(__name__)

# 设置秘钥
app.secret_key = 'insaneLoafer'

@app.route('/')
def hello():
    name = request.args.get('name', 'world')
    return f'Hello, {escape(name)}!'

@app.route('/login', methods=['get', 'post'])
def login():
    res = {
        'method': request.method,
        'url': request.path,
        'args': request.args,
        'form': request.form
    }
    session['username'] = request.args.get('name')
    return res

if __name__ == '__main__':
    app.run(debug=True, port=4444)
