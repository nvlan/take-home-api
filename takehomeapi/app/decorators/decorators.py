from flask import request
from werkzeug.exceptions import BadRequest, Unauthorized
from werkzeug.wrappers import Response
from .helpers import validate_auth, sanitize
from takehomeapi.app.services.db import db
import json

def authorize(function):
    def wrapper_authorize():
        try:
            auth = request.headers['Authorization']
        except:
            resp = Response(
            response=json.dumps({
                'Error': 'Missing authorization header in request'}),
                mimetype='application/json',
                status=400)
            raise BadRequest('Error processing request', response=resp)
        else:
            if auth.split()[0] != 'Basic' or len(auth.split()) < 2:
                resp = Response(
                response=json.dumps({
                    'Error': 'Wrong or incomplete token in request'}),
                    mimetype='application/json',
                    status=400)
                raise BadRequest('Error processing request', response=resp)
            auth_token = auth.split()[1]
            success = validate_auth(auth_token)
            if not success:
                resp = Response(
                response=json.dumps({
                    'message': 'Not Authorized',
                    'error': True}),
                    mimetype='application/json',
                    status=403)
                raise Unauthorized('Error processing request', response=resp)
        return function()
    wrapper_authorize.__name__ = function.__name__
    return wrapper_authorize

def audit(function):
    def wrapper_audit():
        endpoint = request.path
        payload = request.data
        if not sanitize(payload):
            raise BadRequest('Invalid input - only letters are allowed!')
        else:
            query="INSERT INTO audit (endpoint, payload) values (%s, %s)"
            values=(endpoint,payload)
            db.get_cursor().execute(query,values)
            db.connection.commit()
        return function()
    wrapper_audit.__name__ = function.__name__
    return wrapper_audit
