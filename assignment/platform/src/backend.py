#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/12/26 15:04
# @Author   : ZhangTao
# @File     : backend.py
import json
from typing import List

from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
# fake db
# app.config['db'] = []

# sqllite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:jinhua911@localhost:3306/hogwarts_db'
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'hello! My insane world!!'


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)
    steps = db.Column(db.String(1024), unique=True, nullable=True)

    def __repr__(self):
        return '<TestCase %r>' % self.username


# 创建Task数据库并关联TestCase的id
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), unique=True, nullable=False)
    description = db.Column(db.String(1024), unique=True, nullable=True)

    # 进行关联
    testcase_id = db.Column(db.Integer, db.ForeignKey('testcase.id'), nullable=False)
    test_case = db.relationship('TestCase', backref=db.backref('task', lazy=True))

    def __repr__(self):
        return '<Task %r>' % self.name


class TestCaseService(Resource):
    def get(self):
        """
        测试用例的浏览获取
        /testcase.json /testcase.json?id=1
        """
        # testcases = app.config['db']
        # 进行查询
        testcases: List = TestCase.query.all()
        res = [{
            'id': testcase.id,
            'name': testcase.name,
            'description': testcase.description,
            'steps': json.loads(testcase.steps)
        } for testcase in testcases]

        return {
            'body': res
        }

    def post(self):
        """
        上传用例，更新用例
        /testcase.json {'name': 'xx',
        'description': 'xx'}
        """

        # print(request.json)
        # app.config['db'].append(dict(request.json))
        testcase = TestCase(
            name=request.json.get('name'),
            description=request.json.get('description'),
            steps=json.dumps(request.json.get('steps'))
        )

        # print(app.config['db'])
        db.session.add(testcase)
        db.session.commit()
        return 'ok'


class TaskService(Resource):
    def get(self):
        """
        测试任务的浏览获取
        /taskservice
        """

        # 进行查询
        tasks: List = Task.query.all()
        res = [{
            'id': task.id,
            'name': task.name,
            'description': task.description,
        } for task in tasks]

        return {
            'body': res
        }

    def post(self):
        """
        测试任务的修改与更新
        /taskservice
        """

        task = Task(
            name=request.json.get('name'),
            description=request.json.get('description')
        )

        db.session.add(task)
        db.session.commit()
        return 'ok'

    def delete(self):
        """
        测试任务的删除
        /taskservice
        """

        task = Task(id=request.json.get('id'))

        db.session.delete(task)
        db.session.commit()
        return 'delete successful!'


class ReportService(Resource):
    def get(self):
        pass


api.add_resource(TestCaseService, '/testcase')
api.add_resource(TaskService, '/task')
api.add_resource(ReportService, '/report')

if __name__ == '__main__':
    app.run(debug=True, port=4444)
