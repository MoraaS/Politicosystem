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
            "phonenumber": "0713452678",
            "password": "Password@123",
            "passporturl": "passporturl",
            "isAdmin": False
        }

        response = self.post(
            "api/v2/auth/signup", data=signup_data)
        self.assertEqual(response.status_code, 201)

    def test_signup_with_no_firstname(self):
        signup_data = {
            "lastname": "moraa",
            "othername": "maranga",
            "email": "salmamaranga@gmail.com",
            "password": "Password123"
        }
        response = self.post("api/v2/auth/signup", data=signup_data)
        self.assertEqual(response.status_code, 400)

    def test_signup_with_no_lastname(self):
        signup_data = {
            "firstname": "salma",
            "othername": "maranga",
            "email": "salmamaranga@gmail.com",
            "password": "Password123"
        }
        response = self.post("api/v2/auth/signup", data=signup_data)
        self.assertEqual(response.status_code, 400)

    def test_signup_with_no_othername(self):
        signup_data = {
            "firstname": "salma",
            "lastname": "maranga",
            "email": "salmamaranga@gmail.com",
            "password": "Password123"
        }
        response = self.post("api/v2/auth/signup", data=signup_data)
        self.assertEqual(response.status_code, 400)

    def test_signup_with_no_email(self):
        signup_data = {
            "firstname": "salma",
            "lastname": "maranga",
            "othername": "maranga",
            "password": "Password123"
        }
        response = self.post("api/v2/auth/signup", data=signup_data)
        self.assertEqual(response.status_code, 400)

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
