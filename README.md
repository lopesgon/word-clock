# Word Clock
> DIY Wordclock - A Python Flask based project

This is part of a diy project of building a wordclock with NeoPixels.

## Important about NeoPixels

This project works with Adafruit dependencies. Thus you may use compatible leds.

* “NeoPixel” is Adafruit’s brand for individually-addressable RGB color pixels and strips based on the WS2812, WS2811 and SK6812 LED/drivers, using a single-wire control protocol.

* NeoPixels don’t just light up on their own; they require a microcontroller (such as Arduino) and some programming.

## Important about electric power

Do not forget electrical projects imply working with 220v power that can be letal !

Each RGB Led requires approximately 5v 0.6a of power at full power (bright white).

E.g. wiring & power supply 

* 5v 10A Power supply
* Soldered wires to power up RaspberryPi & Leds with a single power supply

## Installing / Getting started

To start your server, execute Makefile command lines here above.

```shell
make install
make run-debug
```

Your server will start serving at http://127.0.0.1:5000 

### Initial Configuration

In order to install and run project, you must have these versions installed:
- python3.8
- pip3.8
- setuptools

If needed, you can install global environment requirements by running ```pip install -r requirements.txt```

Fill in with needed global dependencies [./requirements.txt](requirements.txt).

## Developing

Starting developing isn't currently available but be pleased to fork this project and open pull requests :)

```shell
git clone https://github.com/lopesgon/word-clock
cd word-clock/
make install
make run-debug
```

Just start coding.

### Building

If you need to rebuild your project, simply follow the steps below:
```shell
make clean
make install
make run-debug
```

Your application will be cleaned the started back again serving on port :5000.

### Deploying / Publishing

- Todo

## Features

What's all the bells and whistles this project can perform?
* Turn on/off LED ws2812b based on a matrice
* Some other stuff coming..

## Configuration

- Todo

#### Argument 1

- Todo

## Contributing

Be pleased to fork this project and build on top of it.

Do not hesitate to open pull-requests.

## Links

Even though this information can be found inside the project on machine-readable
format like in a .json file, it's good to include a summary of most useful
links to humans using your project. You can include links like:

- Project homepage: https://your.github.com/awesome-project/
- Repository: https://github.com/your/awesome-project/
- Issue tracker: https://github.com/your/awesome-project/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    my@email.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
- Related projects:
  - Your other project: https://github.com/your/other-project/
  - Someone else's project: https://github.com/someones/awesome-project/


## Licensing

One really important part: Give your project a proper license. Here you should
state what the license is and how to find the text version of the license.
Something like:

"The code in this project is licensed under MIT license."