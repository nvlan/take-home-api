from takehomeapi.app.services.db import db
import logging

logger = logging.getLogger(__name__)

def get_audit_data():
    response = {}
    query = "SELECT * FROM audit ORDER BY id DESC LIMIT 10;"
    try:
        db.get_cursor().execute(query)
        result = db.get_cursor().fetchall()
    except mysql.connector.errors.DatabaseError as error:
        logging.error('Error executing query: ' + str(result))
    else:
        for item in result:
            id, endpoint, payload = item
            response[id] = [endpoint, payload]
        return response, 200
