import datetime
import logging
import threading
import time
from colorutils import Color
from configurations.configuration import isProduction, getClockConfiguration

# from transition import simple, matrix, fade, drop
# import utils
# from timing import timing

# import mock if environment is not prod/production
if isProduction():
    logging.info("Running leds GPIO controller!")
    from clock.leds_controller import Controller
else:
    logging.info("Running mocked leds...")
    from clock.leds_controller_mock import Controller


class Clock(threading.Thread):
    new_word_leds = []
    new_corner_leds = []

    led_ctrl = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.stopped = False
        self.end_thread = False
        self.config = getClockConfiguration()
        self.stop_cond = threading.Condition(threading.Lock())
        self.led_ctrl = Controller(
            self.config.pixelCount,
            Color(hex=self.config.color).rgb,
            self.config.brightness)
        logging.debug("Clock init with default configuration")
        logging.debug(self.led_ctrl)
        self.generate_leds()

    def run(self):
        """
        Method to run the clock
        """
        while True:
            if self.end_thread:
                break
            with self.stop_cond:
                while self.stopped:
                    self.stop_cond.wait()
                self.tick()
            time.sleep(self.config.interval)

    # Kill Thread, this requires to create a new Clock
    def kill(self):
        self.end_thread = True

    # Stops clock and turns off all lights
    def stop(self):
        logging.debug('Stopping clock')
        # If in sleep, we acquire immediately, otherwise we wait for thread
        # to release condition. In race, worker will still see self.stoped
        # and begin waiting until it's set back to False
        self.stop_cond.acquire()
        self.stopped = True
        self.led_ctrl.turn_off()
        self.stop_cond.notify()
        self.stop_cond.release()

    # Pauses clock in the current state
    def pause(self):
        logging.debug('Clock paused')
        self.stop_cond.acquire()
        self.stopped = True
        self.stop_cond.notify()
        self.stop_cond.release()

    # Resumes clock with its current state
    def resume(self):
        logging.debug('Clock resumed')
        self.stop_cond.acquire()
        self.stopped = False
        self.led_ctrl.turn_on()
        # Notify so thread will wake after lock released
        self.stop_cond.notify()
        # Now release the lock
        self.stop_cond.release()

    def clear(self):
        logging.debug('Clock clear color')
        self.active_word_leds = []
        self.active_corner_leds = []
        self.last_special = datetime.datetime(1970, 1, 1)
        self.led_ctrl.turn_off()

    def change_color(self, color):
        logging.debug('Clock changing color')
        self.config.color = color
        self.led_ctrl.change_color(color)

    def change_brightness(self, brightness):
        logging.debug("Clock changing brightness")
        self.led_ctrl.change_brightness(brightness)

    def refresh(self):
        logging.debug('Clock refreshing')
        self.clear()
        self.display_words()
        self.display_corner()

    def tick(self):
        """
        Clock Tick Method
        """
        logging.debug("ticking...")
        self.generate_leds()

    def generate_leds(self):
        """
        Method to generate word and corner leds
        """
        logging.debug("generating leds")
        # self.led_ctrl.set_pixels()
        time = datetime.datetime.now()
        # words = getWords()
        # text, self.new_word_leds, self.new_corner_leds = utils.time_to_text(words, time)
        # print(name + ' - ' + text)

    def display_words(self):
        """
        Method to display word leds
        """
        transition = self.config['transition']
        if transition == "matrix":
            matrix.start(self.led_ctrl, self.active_word_leds, self.new_word_leds)
        elif transition == "fade":
            fade.start(self.led_ctrl, self.active_word_leds, self.new_word_leds)
        elif transition == "drop":
            drop.start(self.led_ctrl, self.active_word_leds, self.new_word_leds)
        else:
            simple.start(self.led_ctrl, self.new_word_leds)

    def display_corner(self):
        """
        Method to display corner leds
        """
        for led in self.new_corner_leds:
            self.led_ctrl.set_pixel(led)
        self.led_ctrl.show_pixels()
