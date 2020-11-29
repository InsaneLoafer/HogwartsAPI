#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/29 15:03
# @Author   : ZhangTao
# @File     : mitm_rewrite.py
import json
from mitmproxy import http
import os

def response(flow: http.HTTPFlow):
    # 限制条件进行url过滤
    if 'quote.json' in flow.request.pretty_url and 'x=' in flow.request.pretty_url:
        # 获取响应信息，并使用json.loads转换为Python可编辑的json文件
            data = json.loads(flow.response.content)
            for i in range(len(data['data']['items'])):
                # 为了与第一种方法区别结果，这里将所有股票名改为InsaneLoafer
                data['data']['items'][i]['quote']['name'] = "Insane"
                # 修改第二只股票，名字加长一倍
                if i == 1:
                    data['data']['items'][i]['quote']['name'] *= 2
                # 修改第三只股票，将其名字置空
                elif i == 2:
                    data['data']['items'][i]['quote']['name'] = ''
            # 重新以二进制原格式返回响应信息
            flow.response.text = json.dumps(data)

if __name__ == '__main__':
    os.system(r"mitmdump -p 8999 -s 'D:\My_Files\HogwartsAPI\assignment\mock_practice\mitm_rewrite.py'")
