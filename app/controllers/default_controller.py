from flask import abort
from main import app

ROOT_PATH = '/api'


@app.route(ROOT_PATH + '/hello')
def getHelloWorld():
    return "hello world"


@app.route(ROOT_PATH + '/abort')
def abortANotFoundError():
    abort(404)


@app.route(ROOT_PATH + '/', methods=['POST'])
def post_request():
    return 'post success\n'
