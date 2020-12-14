# Word Clock
Word-Clock is Flask Python project to run in a pi-zero.

# Prerequesites
- python3.9
- pip3.9

# Getting started

Run ```make run-debug``` will automatically `setup virtual environment`, `install dependencies` and start your Flask server.

## Setup virtual environment
From project folder create a virtual environment

```bash
python3.9 -m venv venv
```

Activate your virtual environment ```source venv/bin/activate``` and validate virtual environment is correctly setup.

## Install dependencies
Install dependencies by running ```make install``` will install in your virtual environment automatically.

## Clean project
Run ```make clean``` will clean up all project

## Global dependencies (not required)
If needed, you can install global environment requirements by running ```pip install -r requirements.txt```

Fill in with needed global dependencies [./requirments.txt](requirements.txt).
