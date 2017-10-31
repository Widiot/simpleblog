import unittest
from flask import url_for
from simpleblog import create_app, db


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # 测试注册和登录
    def test_register_and_login(self):
        # 注册一个用户
        response = self.client.post(
            url_for('auth.register'),
            data={
                'email': 'user@example.com',
                'password': 'test',
                'confirm': 'test'
            })
        self.assertEqual(response.status_code, 302)