import os
import json
import unittest
from test.v2.basetest import BaseTestCase
from app import create_app


class TestUsers(BaseTestCase):

    def test_signup(self):
        """ test for signin up"""
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

    def test_login(self):
        """ test for login """
        login_data = {
            "email": "salmamaranga@gmail.com",
            "password": "Password123"
        }

        response = self.post(
            "api/v2/auth/login", data=login_data)
        self.assertEqual(response.status_code, 200)

    def test_login_with_empty_fields(self):
        login_data = {}
        response = self.post("api/v2/auth/login", data=login_data)
        self.assertEqual(response.status_code, 400)

    def test_login_with_missing_email(self):
        login_data = {
            "email": "",
            "password": "Password123"
        }
        response = self.post("api/v2/auth/login", data=login_data)
        self.assertEqual(response.status_code, 400)

    def test_login_with_missing_password(self):
        login_data = {
            "email": "salmamaranga@gmail.com",
            "password": ""
        }
        response = self.post("api/v2/auth/login", data=login_data)
        self.assertEqual(response.status_code, 400)
