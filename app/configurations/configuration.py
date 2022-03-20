import json
import logging
import os
from logging.config import dictConfig
from types import SimpleNamespace as Namespace

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})


def isProduction():
    flask_env = os.environ.get("FLASK_ENV").lower()
    if flask_env == 'production':
        return True

    configuration = getConfiguration()
    environment = configuration.environment.lower()
    return environment == 'prod' or environment == 'production'


def getClockConfiguration():
    configuration = getConfiguration()
    return configuration.clock


def initializeConfiguration():
    logging.info("Initializing configuration")
    if isProduction:
        logging.debug("init todo")
    else:
        logging.debug("init else todo")


def getConfiguration():
    from main import app

    filename = os.path.join(app.static_folder, 'configuration.json')
    return json.load(open(filename, "r"), object_hook=lambda d: Namespace(**d))
