from flask import Flask
from app.views.health import health_blueprint
from app.views.apiref import apiref_blueprint
from app.views.words import words_blueprint
from app.views.audit import audit_blueprint
from app.views.root import proxy_route
from app.services.db import connect_db
from werkzeug.middleware.dispatcher import DispatcherMiddleware

def create_app():
    # create application instance
    app = Flask(__name__)
    app.config.from_object('config.settings')
#    app.wsgi_app = DispatcherMiddleware(proxy_route, {app.config['PREFIX_APP_URL']: app.wsgi_app})
    app.register_blueprint(health_blueprint, url_prefix='/health')
    app.register_blueprint(words_blueprint, url_prefix='/words')
    app.register_blueprint(audit_blueprint, url_prefix='/audit')
    app.register_blueprint(apiref_blueprint, url_prefix='/apiref')
#    connect_db()
    return app
