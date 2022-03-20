from flask import make_response, jsonify
from main import app


@app.errorhandler(404)
def not_found(error):
    data = {'message': error.description, 'code': 'Not Found'}
    response = make_response(jsonify(data), 404)
    response.headers['X-Something'] = 'A header value'
    return response


@app.errorhandler(400)
def bad_request(error):
    print(error)
    data = {'message': error.description, 'code': 'Bad Request'}
    response = make_response(jsonify(data), 400)
    return response
