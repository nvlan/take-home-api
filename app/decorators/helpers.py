from flask import current_app
import base64

def validate_auth(auth):
    payload_b64_bytes = base64.b64decode(auth)
    payload = payload_b64_bytes.decode('ascii')
    if payload.split(':')[0] == current_app.config['AUTH_USER'] and payload.split(':')[1] == current_app.config['AUTH_PASS']:
        return True, payload
    else:
        return False, payload
