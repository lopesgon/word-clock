HOST=127.0.0.1
PORT=9000

install: create-venv
	. venv/bin/activate && \
	pip install -e .
	# pip install -r requirements.txt

run-debug: install
	. venv/bin/activate && \
	export FLASK_APP=src && \
	export FLASK_ENV=development && \
	flask run

run: install
	. venv/bin/activate && \
	export FLASK_APP=src/word-clock && \
	flask run

clean: clean-vm clean-pyc clean-build
clean-vm:
	rm -rf venv/
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
clean-build:
	rm -rf build/
	rm -rf dist/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -rf {} +

versions:
	python --version
	pip --version

create-venv:
	pip3.8 install virtualenv;
	python3.8 -m venv venv;
