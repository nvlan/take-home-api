from random import shuffle

error_data = { 'Error' : 'Missing data in the request, please check the apiref'}

def scrambler(data):
    if len(data) == 0:
        return error_data, 400
    else:
        word = list(data.decode("utf-8"))
        shuffle(word)
        word = ''.join(word)
        return word, 200
