from base import BaseTestCase

class WordsTestCase(BaseTestCase):

    def test_scramble_word_success(self):
        auth = self.generate_auth()
        self.headers.setdefault('Authorization', 'Basic ' + auth)
        payload = "palabras"
        response = self.client.post('/words',
                        headers=(self.headers), data=payload)
        assert response.status_code == 200

    def test_scramble_word_illegal_char(self):
        auth = self.generate_auth()
        self.headers.setdefault('Authorization', 'Basic ' + auth)
        payload = "malicious content \x64\x86\x94"
        response = self.client.post('/words',
                        headers=(self.headers), data=payload)
        assert response.status_code == 400

    def test_scramble_word_no_payload(self):
        auth = self.generate_auth()
        self.headers.setdefault('Authorization', 'Basic ' + auth)
        response = self.client.post('/words',
                        headers=(self.headers))
        assert response.status_code == 400

    def test_scramble_word_bad_auth(self):
        auth = "wrong:verywrong"
        self.headers.setdefault('Authorization', 'Basic ' + auth)
        response = self.client.post('/words',
                        headers=(self.headers))
        assert response.status_code == 403

    def test_scramble_word_no_auth(self):
        payload = "palabras"
        response = self.client.post('/words',
                        data=payload)
        assert response.status_code == 400
