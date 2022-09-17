from base import BaseTestCase

class AuditTestCase(BaseTestCase):

    def test_audit_success(self):
        auth = self.generate_auth()
        self.headers.setdefault('Authorization', 'Basic ' + auth)
        response = self.client.get('/audit',
                        headers=(self.headers))
        assert response.status_code == 200

    def test_audit_dangerous_payload(self):
        auth = self.generate_auth()
        self.headers.setdefault('Authorization', 'Basic ' + auth)
        payload = "malicious content \x64\x86\x94"
        response = self.client.get('/audit',
                        headers=(self.headers), data=payload)
        assert response.status_code == 400

    def test_audit_bad_auth(self):
        auth = "wrong:verywrong"
        self.headers.setdefault('Authorization', 'Basic ' + auth)
        response = self.client.get('/audit',
                        headers=(self.headers))
        assert response.status_code == 403

    def test_audit_no_auth(self):
        response = self.client.get('/audit')
        assert response.status_code == 400
