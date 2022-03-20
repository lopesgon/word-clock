from flask import request
from main import app
from clock import clock_services as clock_services

ROOT_PATH = '/clock'


@app.route(ROOT_PATH + '/kill')
def kill():
    clock_services.kill_clock()
    return "clock killed"


@app.route(ROOT_PATH + '/resume')
def resume():
    clock_services.resume_clock()
    return "clock resumed"


@app.route(ROOT_PATH + '/pause')
def pause():
    clock_services.pause_clock()
    return "clock paused"


@app.route(ROOT_PATH + '/stop')
def stop():
    clock_services.stop_clock()
    return "clock stopped"


@app.route(ROOT_PATH + '/update')
def update_clock_state():
    color_arg = request.args.get('color')
    if color_arg is not None:
        clock_services.change_color(color_arg)

    brightness_arg = request.args.get('brightness')
    if brightness_arg is not None:
        clock_services.change_brightness(brightness_arg)

    return 'clock state updated'
