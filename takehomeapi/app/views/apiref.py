from flask import Blueprint, send_from_directory
from takehomeapi.config import settings
from takehomeapi.app.decorators.decorators import audit

apiref_blueprint = Blueprint('apiref', __name__)

@apiref_blueprint.route('', methods=('GET',))
@audit
def apiref():
    root_dir = getattr(settings, 'STATIC_ROOT')
    return send_from_directory(root_dir, 'apiref.html')
    return "OK", 200
