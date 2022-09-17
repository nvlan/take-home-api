from takehomeapi.app.services.db import db

def get_audit_data():
    response = {}
    query = "SELECT * FROM audit ORDER BY id DESC LIMIT 10;"
    db.get_cursor().execute(query)
    result = db.get_cursor().fetchall()
    for item in result:
        id, endpoint, payload = item
        response[id] = [endpoint, payload]
    return response, 200
