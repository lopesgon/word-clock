import logging

verbose = True

class Controller():
    name = 'MOCK_WS2812'
    color = [0, 255, 0]

    def __init__(self, ledsCount, color, brightness):
        logging.debug("Init " + self.name + " with values")
        logging.debug("ledsCount="+str(ledsCount)+"; color="+str(color)+"; brightness="+str(brightness))
        pass

    def change_color(self, color):
        logging.debug(self.name + ' - Change color to: ' + str(color))

    def change_brightness(self, brightness):
        value = abs(brightness / 100)
        logging.debug(self.name + ' - Set brightness to : ' + str(value))

    def set_pixels(self, leds, colors=[]):
        if verbose:
            logging.debug(self.name + ' - Turn on leds: ' + str(leds))

    def set_pixel(self, led, color=[]):
        if verbose:
            logging.debug(self.name + ' - Turn on led: ' + str(led))

    def show_pixels(self):
        if verbose:
            logging.debug(self.name + ' - Show pixels')

    def clear_pixels(self):
        if verbose:
            logging.debug(self.name + ' - Clear pixels')

    def turn_off(self):
        logging.debug(self.name + ' - Turn off leds')

    def turn_on(self):
        logging.debug(self.name + " - Turn on leds")
