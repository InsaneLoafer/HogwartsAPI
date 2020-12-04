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
        # print(json.dumps(r.json(), indent=2))
        # print(token)
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

    # 通过标签组名称获取其id，以及整个标签组名称列表
    def get_group(self, group_name = None):
        global group_id, group_list
        r = self.get_taglist()
        # group_id_list = [group['group_id'] for group in r.json()['tag_group'] if group['group_name'] == group_name]
        # 定义标签组名称列表
        group_list = []
        group_id = ''
        for group in json.loads(r.text)['tag_group']:
            group_list.append(group['group_name'])
            # print(group)
            if group_name != None and group['group_name'] == group_name:
                group_id = group['group_id']
                print(group_id)
                break

        print(group_list)
        return group_list, group_id

    # 通过标签名称获取其id，以及整个标签名称列表
    def get_tag(self, tag_name=None):
        global tag_id, tag_list
        r = self.get_taglist()
        # tag_list = [tags['tag'] for tags in r.json()['tag_group']]
        # tag_id = [tag['id'] for tag in tag_list if tag['name'] == tag_name]
        # 定义标签名称列表
        tag_list = []
        tag_id = ''
        for tags in json.loads(r.text)['tag_group']:
            # print(tags['tag'])
            for tag in tags['tag']:
                # print(tag['name'])
                tag_list.append(tag['name'])
                if tag_name != None and tag['name'] == tag_name:
                    tag_id = tag['id']
                    break
        # print(tag_list)
        return tag_list, tag_id

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

    # 修改标签
    def edit(self, old_name, new_name=None, order=None):
        global id
        id = ''
        groups = self.get_group()
        tags = self.get_tag()
        if old_name in groups:
            id = self.get_group(old_name)[1]
        elif old_name in tags:
            id = self.get_tag(old_name)[1]

        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={'access_token': self.get_token()},
            json={
                'id': id,
                'name': new_name,
                'order': order
            }
        )
        # print(json.dumps(r.json(), indent=2))
        return r

    # 删除标签
    def delete_by_tagname(self, tagname):
        tag_list, tag_id = self.get_tag(tagname)
        r = requests.post(
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
        group_list, group_id = self.get_group(group_name)
        r = requests.post(
            url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.get_token()},
            json={
                # "tag_id": [],
                "group_id": [group_id]
            }
        )
        return r

if __name__ == '__main__':
    tag = Tag()
    r = tag.edit('tag2', 'tag11')
    print(r.status_code)