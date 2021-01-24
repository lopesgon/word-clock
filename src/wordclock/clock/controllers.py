import logging
from flask import request, abort
from wordclock import app
import wordclock.clock.services as clock_services

@app.route('/clock/resume')
def resume():
    clock_services.resume_clock()
    return "clock resumed"

@app.route('/clock/pause')
def pause():
    clock_services.pause_clock()
    return "clock paused"

@app.route('/clock/stop')
def stop():
    clock_services.stop_clock()
    return "clock stopped"

@app.route('/clock/update')
def update_clock_state():
    color_arg = request.args.get('color')
    if color_arg is not None:
        clock_services.change_color(color_arg)
    
    brightness_arg = request.args.get('brightness')
    if brightness_arg is not None:
        clock_services.change_brightness(brightness_arg)
    
    return 'clock state updated'