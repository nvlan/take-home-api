import mysql.connector, time
from takehomeapi.config import settings

dbconf = {
    'user' : getattr(settings, 'DB_USER'),
    'password' : getattr(settings, 'DB_PASS'),
    'host' : getattr(settings, 'DB_HOST'),
    'port' : getattr(settings, 'DB_PORT'),
    'database' : getattr(settings, 'DB_DATABASE'),
}

class database():

    def __init__(self):
        retries = getattr(settings, 'DB_RETRIES')
        retry_counter = 0
        while retry_counter < retries:
            try:
                self.connection=mysql.connector.Connect(**dbconf)
                self.cursor=self.connection.cursor()
                retry_counter += 1
            except mysql.connector.errors.DatabaseError as error:
                if retry_counter == retries:
                    raise
                else:
                    time.sleep(5)
            else:
                break

    def get_cursor(self):
        return self.cursor
    def get_connection(self):
        return self.connection

db = database()
