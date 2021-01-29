import logging
import board
from neopixel import NeoPixel

# See NeoPixel Library
# https://adafruit.github.io/Adafruit_NeoPixel/html/class_adafruit___neo_pixel.html
class Controller():

    def __init__(self, ledsCount, color, brightness):
        self.pixels = NeoPixel(board.D18, ledsCount, auto_write=False, brightness=brightness)

        self.color = color
        self.brightness = brightness
        self.pixels.fill(self.color)
        self.show_pixels()

    def change_color(self, color):
        self.color = color
        self.pixels.fill(self.color)
        self.show_pixels()

    def change_brightness(self, brightness):
        self.brightness = abs(brightness / 100)
        self.pixels.brightness = self.brightness
        self.show_pixels()

    def set_pixels(self, leds, colors = []):
        self.clear_pixels()
        if len(colors) <= 0:
            for led in leds:
                self.set_pixel(led, self.color)
        else:
            for i, led in enumerate(leds):
                self.set_pixel(led, colors[i])
        self.pixels.show()

    def set_pixel(self, led, color):
        self.pixels[led] = color
        
    def show_pixels(self):
        self.pixels.show()

    def clear_pixels(self):
        self.pixels.fill((0,0,0))

    def turn_off(self):
        self.clear_pixels()
        self.show_pixels()
    
    def turn_on(self):
        self.pixels.fill(self.color)
        self.show_pixels()