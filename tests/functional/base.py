import unittest, base64
from takehomeapi import create_app
from takehomeapi.config import settings

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.headers = {'Content-type': 'text/plain'}
        self.user = getattr(settings, 'AUTH_USER')
        self.password = getattr(settings, 'AUTH_PASS')

    def generate_auth(self):
        auth_plain = self.user + ':' + self.password
        auth_plain_b64 = auth_plain.encode('ascii')
        auth_b64 = base64.b64encode(auth_plain_b64)
        auth = auth_b64.decode('ascii')
        return auth

    def tearDown(self):
        self.app_context.pop()
