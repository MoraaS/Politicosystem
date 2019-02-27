import os
import json
import unittest
from app import create_app
from app.api.v2.models.dbconfig import Database


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        config_name = os.getenv("APP_SETTINGS")
        app = create_app(config_name)
        self.client = app.test_client(self)
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.admin_data = {
            "firstname": "Salma",
            "lastname": "Moraa",
            "othername": "Maranga",
            "email": "saladmin@gmail.com",
            "phonenumber": "0713623572",
            "password": "Salmaadmin@123",
            "passporturl": "passporturl",
            "isAdmin": True
        }

        self.user_data = {
            "firstname": "John",
            "lastname": "Doe",
            "othername": "Donald",
            "email": "johndoe@gmail.com",
            "phonenumber": "0713452678",
            "password": "Password@123",
            "passporturl": "passporturl",
            "isAdmin": False
        }

        self.parties_data = {
            "name": "republican",
            "hqaddress": "washington",
            "logourl": "photo.com"
        }

        self.office_data = {
            "name": "senator",
            "office_type": "state"
        }

    def admin_token(self):
        # create admin
        self.post(
            "api/v2/auth/admin", data=self.admin_data)
        # login to get token
        response = self.post(
            "api/v2/auth/login", data={"email": "saladmin@gmail.com",
                                       "password": "Salmaadmin@123"})
        return response.json['data'][0]['token']

    def create_party(self, party):
        auth_header = {"Authorization": "" + self.admin_token()}
        response = self.client.post(path='/api/v2/parties',
                                    data=json.dumps(party),
                                    content_type='application/json',
                                    headers=auth_header)
        return response

    def create_office(self, office_data):
        auth_header = {"Authorization": "" + self.admin_token()}
        response = self.client.post(path='/api/v2/offices',
                                    data=json.dumps(office_data),
                                    content_type='application/json',
                                    headers=auth_header)
        return response

    def create_candidate(self, office_id, party_id, user_id):
        auth_header = {"Authorization": "" + self.admin_token()}
        data = {
            "party_id": party_id,
            "candidate_id": user_id
        }
        response = self.client.post(path="api/v2/offices/{}/register".format(office_id),
                                    data=json.dumps(data),
                                    headers=auth_header,
                                    content_type='application/json')
        return response

    def get(self, url):
        return self.client.get(url, content_type="application/json")

    def post(self, url, data):
        return self.client.post(url,
                                data=json.dumps(data),
                                content_type="application/json")

    def delete(self, url):
        return self.client.delete(url,
                                  content_type="application/json")

    def patch(self, url, data):
        return self.client.patch(url, data=json.dumps(data),
                                 content_type="application/json")

    def tearDown(self):
        self.app.testing = False
        db = Database()
        db.destroy_tables()
