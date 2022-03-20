from flask import Flask

app = Flask(__name__, static_folder="resources")

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=False, port=80)

import controllers.handlers.http_handler
import controllers.default_controller
import controllers.webapp_controller
import controllers.clock_controller

from clock.clock_services import start_clock
start_clock()
