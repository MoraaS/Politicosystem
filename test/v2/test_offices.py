import os
import json
import unittest
import datetime
import jwt
from test.v2.basetest import BaseTestCase
from app import create_app


class TestUsers(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.office_data2 = {
            "name": "governor",
            "office_type": "state"
        }

    def test_create_office(self):
        """ test for creating an office"""

        response = self.create_office(self.office_data)
        self.assertEqual(response.status_code, 201)

    def test_get_all_offices(self):
        # create two offices
        self.create_office(self.office_data)
        self.create_office(self.office_data2)

        response = self.get("api/v2/offices")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['offices']), 2)

    def test_create_office_with_short_name(self):
        """ test for creating an office with a short name"""
        office = {
            "name": "jed",
            "office_type": "state"
        }
        response = self.create_office(office)
        self.assertEqual(response.status_code, 400)

    def test_create_office_with_numbers(self):
        """ test for creating an office that contains a number"""
        office = {
            "name": "office1",
            "office_type": "state"
        }
        response = self.create_office(office)
        self.assertEqual(response.status_code, 400)

    def test_create_existing_office(self):
        """ test for creating an existing office"""
        self.create_office(self.office_data)
        response = self.create_office(self.office_data)
        self.assertEqual(response.status_code, 400)

    def test_create_office_missing_name(self):
        """ test for creating an office without name in request"""
        office = {
            "office_type": "state"
        }
        response = self.create_office(office)
        self.assertEqual(response.status_code, 400)

    def test_get_non_existing_office(self):
        office_id = 3000

        response = self.get("api/v2/offices/{}".format(office_id))
        self.assertEqual(response.status_code, 404)

    def test_register_candidate_in_null_office(self):
        auth_header = {"Authorization": "" + self.admin_token()}

        data = {
            "party_id": 1,
            "candidate_id": 1
        }
        response = self.client.post(path="api/v2/offices/{}/register".format(12),
                                    data=json.dumps(data),
                                    headers=auth_header,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)


