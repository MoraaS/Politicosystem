
'''Entry point for the tests'''
import os
import json
import unittest
from app import create_app


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        config_name = os.getenv("APP_SETTINGS")
        app = create_app(config_name)
        self.client = app.test_client(self)
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()

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
