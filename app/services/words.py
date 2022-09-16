from flask import current_app
from random import shuffle

error_data = { 'Error' : 'Missing or wrong data in the request, please check the apiref'}

def scrambler(data=None):
    if data is None:
        return error_data, 400
    else:
        word = list(data.decode("utf-8"))
        shuffle(word)
        word = ''.join(word)
        return word, 200
