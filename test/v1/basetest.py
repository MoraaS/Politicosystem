
'''Entry point for the tests'''
import json
import unittest
from app import app


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def get(self, url):
        return self.client.get(url, content_type="application/json")

    def post(self, url, data):
        return self.client.post(url,
                                data=json.dumps(data),
                                content_type="application/json",)

    def tearDown(self):
        pass
  
