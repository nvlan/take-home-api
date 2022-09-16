import os

class BaseConfig(object):
    PREFIX_APP_URL = '/takehome'
    STATIC_ROOT = '/Users/nicodemus/repos/take-home-api/app/statics'
    AUTH_USER = 'root'
    AUTH_PASS = 'password'


settings = globals()['BaseConfig']
