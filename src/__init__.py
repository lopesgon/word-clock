from flask import Flask
from markupsafe import escape

app = Flask(__name__, 
            static_url_path='', 
            static_folder='../web/static', 
            template_folder='../web/templates')

from controllers import defaults
from controllers.handlers import http_handler