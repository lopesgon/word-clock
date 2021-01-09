import logging

from flask import Flask
from wordclock.clock.services import start_clock, kill_clock
from wordclock.configurations.configuration import initializeConfiguration

app = Flask(__name__,
            static_url_path='',
            static_folder='../resources/static',
            template_folder='../resources/templates')

if __name__ == "wordclock":
    logging.info("Starting Word-Clock Flask Server")
    initializeConfiguration()
    start_clock()

import wordclock.controllers.defaults, wordclock.controllers.handlers.http_handler
import wordclock.clock.controllers
