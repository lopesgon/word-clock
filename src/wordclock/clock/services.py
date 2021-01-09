import logging
from colorutils import Color
from wordclock.clock.models import Clock

clock = None

def start_clock():
    logging.debug("Starting clock thread..")
    global clock
    if (clock is None):
        clock = Clock()
        clock.start()

def get_clock():
    logging.debug("Getting clock thread")
    global clock
    if (clock is None):
        logging.warning("Trying to get a non-instantiated clock. This should'nt append.")
        start_clock()

    return clock

def kill_clock():
    logging.info("Killing clock thread..")
    global clock
    if (clock is None):
        logging.warn("Tried to kill a non-existing clock thread..")
    else:
        clock.stop()
        clock.kill()
        clock.join()

def resume_clock():
    clock = get_clock()
    clock.resume()

def pause_clock():
    clock = get_clock()
    clock.pause()

def stop_clock():
    clock = get_clock()
    clock.stop()

def change_color(color_hex):
    color = Color(hex=color_hex)
    clock.change_color(color.rgb)