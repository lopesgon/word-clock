from flask import make_response
from wordclock import app

@app.errorhandler(404)
def not_found(error):
    resp = make_response('404 not found is returned', 404)
    resp.headers['X-Something'] = 'A header value'
    return resp
