from flask import Flask
from markupsafe import escape

app = Flask(__name__, 
            static_url_path='', 
            static_folder='../resources/static', 
            template_folder='../resources/templates')

from controllers import defaults
from controllers.handlers import http_handler