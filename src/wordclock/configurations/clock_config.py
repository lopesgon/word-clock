import yaml, importlib
from wordclock.models.clock import Led, Word

CLOCK_PROPS_FILE="src/resources/clock-properties.yml"

letters = []
words = []

def getWords():
    return words

def loadProperties():
    try:
        stream = open(CLOCK_PROPS_FILE, "r")
        dictionary = yaml.load_all(stream, Loader=yaml.FullLoader)
        parseClockProperties(dictionary)
    except yaml.YAMLError as exception:
        print(exception)
    except OSError as exception:
        print(exception)
        raise exception

def parseClockProperties(dictionary):
    for doc in dictionary:
        setLetters(doc["letters"])
        parseWords(doc["words"].items())

def setLetters(values):
    i = 0
    while(i < len(values)):
        letters.append(Led(i, values[i]))
        i += 1

def parseWords(items):
    for key, value in items:
        word = getWord(Word(key), value)

def getWord(word, leds):
    print(word, ': ', leds)
    return word