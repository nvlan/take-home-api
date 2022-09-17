
class BaseConfig():
    def __init__(self):
        self.PREFIX_APP_URL = '/takehome'
        self.STATIC_ROOT = '/opt/code/takehomeapi/app/statics'
        self.AUTH_USER = 'root'
        self.AUTH_PASS = 'password'
        self.DB_USER = 'user'
        self.DB_PASS = 'password'
        self.DB_HOST = 'mariadb'
        self.DB_PORT = 3306
        self.DB_DATABASE = 'takehomeapi'
        self.DB_RETRIES = 5

settings = BaseConfig()
