#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 21:55
# @Author   : ZhangTao
# @File     : env_demo.py
import requests
import yaml

class Api:
    data = yaml.safe_load(open('env.yaml'))
    url = data['url']
    env = data['test_env']
    print(data, url, env)
    def send(self):
        # 替换服务器地址
        # data['url'] = str(data['url']).replace('testing-studio', data['test_env'][data]['default'])
        self.url = str(self.url).replace('testing-studio', self.env[self.data['default']])
        r = requests.request(method=self.data['method'], url=self.url, headers=self.data['headers'])
        return r

if __name__ == '__main__':
    a = Api()
    print(a.send())

