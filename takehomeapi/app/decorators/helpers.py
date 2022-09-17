from takehomeapi.config import settings
import base64, re

def validate_auth(auth):
    try:
        payload_b64_bytes = base64.b64decode(auth)
    except:
        return False
    else:
        payload = payload_b64_bytes.decode('ascii')
        if payload.split(':')[0] == getattr(settings, 'AUTH_USER') and payload.split(':')[1] == getattr(settings, 'AUTH_PASS'):
            return True, payload
        else:
            return False, payload

def sanitize(payload):
    filter = re.compile(r'^[a-zA-Z]*$')
    if filter.match(payload.decode("utf-8")):
        return True
    else:
        return False
