import os
from flask import send_file
from main import app

WEBAPP_PATH = "webapp/"
WEBAPP_ROOT = WEBAPP_PATH + "index.html"


@app.route('/')
def main():
    index_path = os.path.join(app.static_folder, WEBAPP_ROOT)
    return send_file(index_path)


@app.route("/<path:path>")
def route_frontend(path):
    # ...could be a webapp file needed by the front end that
    # doesn't use the `webapp` path (like in `<script src="bundle.js">`)
    file_path = os.path.join(app.static_folder, WEBAPP_PATH, path)
    if os.path.isfile(file_path):
        return send_file(file_path)
    # ...or should be handled by the SPA's "router" in front end
    else:
        index_path = os.path.join(app.static_folder, WEBAPP_ROOT)
        return send_file(index_path)
