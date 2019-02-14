import os
import json
import unittest
from test.v2.basetest import BaseTestCase
from app import create_app


class TestUsers(BaseTestCase):
    ''' loads the app with all configurations for testings'''

    def setUp(self):
        config_name = os.getenv("APP_SETTINGS")
        app = create_app('testing')
        self.client = app.test_client(self)
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()

    def test_signup(self):
        """ test for signing up"""
        signup_data = {
            "firstname": "salma",
            "lastname": "moraa",
            "othername": "maranga",
            "email": "salmamaranga@gmail.com",
            "password": "Password123"
        }

        response = self.post(
            "api/v2/auth/signup", data=signup_data)
        self.assertEqual(response.status_code, 201)

