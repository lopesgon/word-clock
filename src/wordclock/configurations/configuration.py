import json, logging, os
from types import SimpleNamespace as Namespace
from logging.config import dictConfig

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

CLOCK_PROPS_FILE="src/resources/configuration.json"

configuration = json.load(open(CLOCK_PROPS_FILE, "r"), object_hook=lambda d: Namespace(**d))

def isProduction():
    flask_env = os.environ.get("FLASK_ENV").lower()
    if flask_env == 'production':
        return True
    
    environment = configuration.environment.lower()
    return environment == 'prod' or environment == 'production'

def getClockConfiguration():
    return configuration.clock

def initializeConfiguration():
    logging.info("Initializing configuration")
    if (isProduction):
        logging.debug("init todo")
    else:
        logging.debug("init else todo")
