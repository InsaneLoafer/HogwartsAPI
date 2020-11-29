#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/29 14:29
# @Author   : ZhangTao
# @File     : mitm_maplocal.py
from mitmproxy import http
import os

# 使用maplocal进行mock
# 方法名必须死request
def request(flow: http.HTTPFlow):
    # 发起请求，判断 url 是不是预期的值
    if "quote.json" in flow.request.pretty_url:
        # 打开一个保存在本地的数据文件
        with open ("quote.json", encoding="utf-8") as f:
            # 创造一个 response
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                # 读取文件中的数据作为返回内容
                f.read(),
                {"Content-Type": "application/json"}  # (optional) headers
            )

if __name__ == '__main__':
    os.system(r"mitmdump -p 8999 -s 'D:\My_Files\HogwartsAPI\assignment\mock_practice\mitm_pra.py'")