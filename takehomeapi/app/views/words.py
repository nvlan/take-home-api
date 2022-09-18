from flask import Blueprint, request
from takehomeapi.app.services.words import scrambler
from takehomeapi.app.decorators.decorators import authorize, audit

words_blueprint = Blueprint('records', __name__)

@words_blueprint.route('', methods=('POST',))
@authorize
@audit
def scramble_word():
    data = request.data
    response, code = scrambler(data)
    return response, code
