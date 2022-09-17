from flask import Blueprint
from takehomeapi.app.services.audit import get_audit_data
from takehomeapi.app.decorators.decorators import authorize, audit

audit_blueprint = Blueprint('audit', __name__)

@audit_blueprint.route('', methods=('GET',))
@authorize
@audit
def audit_data():
    response, code = get_audit_data()
    return response, code
