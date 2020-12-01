#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/1 21:29
# @Author   : ZhangTao
# @File     : tags.py
import json
import requests

# 定义corpid和secret，用于生成token
corpid = 'ww359520348538abb8'
secret = 'vwr-RNYhUXeQZ-BMwJv-3XSACzjd-Cqox6c7ogjpq3U'

class Tag:
    def __init__(self):
        self.token = ''

    # 定义获取token方法
    def get_token(self):
        r = requests.get(
            url=f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}',
        )
        self.token = r.json()['access_token']
        print(json.dumps(r.json(), indent=2))
        print(self.token)

    # 获取客户所有标签
    def get_taglist(self):
        r = requests.post(
            url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={'access_token': self.token},
            json={
                'tag_id': []
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    # 新增标签
    def add(self, group_name, tags):
        r = requests.post(
            url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={'access_token': self.token},
            json={
                'group_name': group_name,
                'tag': tags
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    # 删除标签
    def delete_by_tagid(self, tagid):
        r = requests.delete(
            url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.token},
            json={
                "tag_id": tagid,
                "group_id": []
            }
        )
        return r.json()

    # 删除标签组
    def delete_by_groupid(self, groupid):
        r = requests.delete(
            url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.token},
            json={
                "tag_id": [],
                "group_id": groupid
            }
        )
        return r.json()

if __name__ == '__main__':
    tag = Tag()
    tag.get_token()