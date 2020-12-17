from flask import abort
from wordclock import app
from wordclock.configurations.clock_config import loadProperties

@app.route('/hello')
def getHelloWorld():
    loadProperties()
    return "Hello World!"

@app.route('/abort')
def abortANotFoundError():
    abort(404)

@app.route('/')
def servePage():
    return app.send_static_file('index.html')

@app.route('/', methods=['POST'])
def post_request():
    return 'post success\n'
