from flask import Flask
from takehomeapi.app.views.health import health_blueprint
from takehomeapi.app.views.apiref import apiref_blueprint
from takehomeapi.app.views.words import words_blueprint
from takehomeapi.app.views.audit import audit_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_blueprint, url_prefix='/health')
    app.register_blueprint(words_blueprint, url_prefix='/words')
    app.register_blueprint(audit_blueprint, url_prefix='/audit')
    app.register_blueprint(apiref_blueprint, url_prefix='/apiref')
    return app
