from flask import Blueprint
from takehomeapi.app.decorators.decorators import audit

health_blueprint = Blueprint('health', __name__)

@health_blueprint.route('', methods=('GET',))
@audit
def health():
    return "Health: OK, Status: Doing good!", 200
