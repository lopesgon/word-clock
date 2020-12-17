class Led():
    """ Led class represents a and defines a letter and its position in the circuit"""
    def __init__(self, letter, position):
        self.letter = letter
        self.position = position
        self.color = (0,0,0)
    
    def __str__(self):
        return self.letter + ' at position ' + self.position


class Word():
    """ Word class is defined by an array of Leds"""

    def __init__(self, word, leds = []):
        self.word = word
        self.leds = leds
