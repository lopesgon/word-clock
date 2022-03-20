import logging
import re
from flask import abort
from colorutils import Color
from clock.clock_model import Clock

clock = None


def start_clock():
    logging.debug("Starting clock thread..")
    global clock
    if clock is None:
        clock = Clock()
        clock.start()


def get_clock():
    logging.debug("Getting clock thread")
    global clock
    if clock is None:
        logging.warning("Trying to get a non-instantiated clock. This shouldn't append.")
        start_clock()

    return clock


def resume_clock():
    get_clock().resume()


def pause_clock():
    get_clock().pause()


def stop_clock():
    get_clock().stop()


def change_color(color_hex):
    if color_hex == "":
        logging.warn("Tried to change leds color without value")
        abort(400, description="Changing leds color requires a not empty string value")

    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color_hex)
    if not match:
        logging.warn("Color input value [{}] isn't a valid hex color value".format(str(color_hex)))
        abort(400, description="Color param is invalid. You must provide a valid hex color value")
    color = Color(hex=color_hex)
    clock.change_color(color.rgb)


def change_brightness(brightness):
    if brightness.isnumeric() and 0 <= int(brightness) <= 100:
        clock.change_brightness(int(brightness))
    else:
        logging.warning("Tried to change brightness with invalid value [{}]".format(str(brightness)))
        abort(400, description="Brightness must be a valid numeric value between 0 and 100")


def kill_clock():
    logging.info("Killing clock thread..")
    global clock
    if clock is None:
        logging.warning("Tried to kill a non-existing clock thread..")
    else:
        clock.stop()
        clock.kill()
        clock.join()
        clock = None


def restart_clock():
    kill_clock()
    start_clock()

