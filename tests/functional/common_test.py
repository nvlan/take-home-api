from base import BaseTestCase

class CommonTestCase(BaseTestCase):

    def test_health_success(self):
        response = self.client.get('/health')
        assert response.status_code == 200

    def test_health_dangerous_payload(self):
        payload = "malicious content \x64\x86\x94"
        response = self.client.get('/health', data=payload)
        assert response.status_code == 400
