PORT=5000

install: create-venv versions
	@echo #
	@echo Installing project dependencies
	. venv/bin/activate && \
	pip install -e .

run-debug:
	@echo #
	@echo Running debug mode
	. venv/bin/activate && \
	export FLASK_APP=src && \
	export FLASK_ENV=development && \
	flask run -p $(PORT)

run: install
	@echo # 
	@echo Running
	. venv/bin/activate && \
	export FLASK_APP=src && \
	flask run -p $(PORT)

build:
	@echo Building setup.py...
	. venv/bin/activate && \
	python setup.py install
	@echo ...building ended.

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

create-venv:
	@echo #
	@echo Installing and creating python virtual environment
	pip3.9 install virtualenv;
	python3.9 -m venv venv;

versions:
	@echo #
	@echo Libaries versions
	. venv/bin/activate && \
	python --version && pip --version
