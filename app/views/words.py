from flask import Blueprint, request
from app.services.words import scrambler
from app.decorators.decorators import authorize

words_blueprint = Blueprint('records', __name__)

@words_blueprint.route('', methods=('POST',))
@authorize
def scramble_word():
    data = request.data
    response, code = scrambler(data)
    return response, code
