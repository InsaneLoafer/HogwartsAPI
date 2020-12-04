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

    # 定义获取token方法
    def get_token(self):
        r = requests.get(
            url=f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}',
        )
        token = r.json()['access_token']
        print(json.dumps(r.json(), indent=2))
        print(token)
        return token

    # 获取客户所有标签
    def get_taglist(self):
        r = requests.post(
            url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={'access_token': self.get_token()},
            json={
                'tag_id': []
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def get_group_id(self, group_name):
        r = self.get_taglist()
        # group_id_list = [group['group_id'] for group in r.json()['tag_group'] if group['group_name'] == group_name]
        for group in r.json()['tag_group']:
            if group['group_name'] == group_name:
                group_id = group['group_id']
                break
            else:
                print('没有此标签组')
        return group_id

    def get_tag_id(self, tag_name):
        r = self.get_taglist()
        # tag_list = [tags['tag'] for tags in r.json()['tag_group']]
        # tag_id = [tag['id'] for tag in tag_list if tag['name'] == tag_name]
        for tags in r.json()['tag_group']:
            tag_list = tags['tag']
            for tag in tag_list:
                if tag['name'] == tag_name:
                    tag_id = tag['id']
                    break
                else:
                    print('没有此标签')
        return tag_id

    # 新增标签
    def add(self, group_name, tags):
        r = requests.post(
            url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={'access_token': self.get_token()},
            json={
                'group_name': group_name,
                'tag': tags
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    # 删除标签
    def delete_by_tagname(self, tagname):
        tag_id = self.get_tag_id(tagname)
        r = requests.delete(
            url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.get_token()},
            json={
                "tag_id": [tag_id]
                # "group_id": []
            }
        )
        return r

    # 删除标签组
    def delete_by_groupname(self, group_name):
        group_id = self.get_group_id(group_name)
        r = requests.delete(
            url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.get_token()},
            json={
                "tag_id": [],
                "group_id": [group_id]
            }
        )
        return r

if __name__ == '__main__':
    tag = Tag()
    r = tag.delete_by_tagname('tag1')
    print(r.status_code)