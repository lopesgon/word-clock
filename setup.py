"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib
import os

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

dependencies = [
    'wheel==0.37.1',
    'setuptools==60.10.0',
    'flask==2.0.3',
    'adafruit-circuitpython-neopixel==6.2.4',
    'colorutils==0.3.0',
]

if os.uname().nodename == 'raspberrypi':
    dependencies.append('rpi_ws281x')

setup(
    name='word-clock',
    package_dir={'': 'app'},
    packages=find_packages(where='app'),
    version='1.0.0-SNAPSHOT',
    description='A Word-Clock Project with some extra features',
    url='https://github.com/lopesgon/word-clock',
    author='Frederic Lopes Goncalves Magalhaes',
    python_requires='>=3.8, <4',
    install_requires=dependencies,
    # Whats the purpose as Flask specifies it ?
    include_package_data=True,

    # extras_require={  # Optional
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    # },

    # long_description=long_description,  # Optional
    # long_description_content_type='text/markdown',  # Optional (see note above)
    # author_email='anonymous@gmail.com',  # Optional

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    # package_data={  # Optional
    #    'sample': [],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={  # Optional
    #    'console_scripts': [
    #        'sample=sample:main',
    #    ],
    # },
)
