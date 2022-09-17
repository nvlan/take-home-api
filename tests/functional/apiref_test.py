from base import BaseTestCase

class ApirefTestCase(BaseTestCase):

    def test_apiref_success(self):
        response = self.client.get('/apiref')
        assert response.status_code == 200

    def test_health_dangerous_payload(self):
        payload = "malicious content \x64\x86\x94"
        response = self.client.get('/apiref', data=payload)
        assert response.status_code == 400
