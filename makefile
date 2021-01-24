PORT=5000
PYTHON_VERSION=python3.9
PIP_VERSION=pip3.9

install: create-venv versions
	@echo #
	@echo Installing project dependencies
	. venv/bin/activate && \
	$(PIP_VERSION) install -e .

run-debug:
	@echo #
	@echo Running debug mode
	. venv/bin/activate && \
	export FLASK_APP=src/wordclock && \
	export FLASK_ENV=development && \
	flask run -p $(PORT)

run:
	@echo # 
	@echo Running
	. venv/bin/activate && \
	export FLASK_APP=src/wordclock && \
	export FLASK_ENV=production && \
	flask run -p $(PORT)

build:
	@echo Building setup.py...
	. venv/bin/activate && \
	$(PYTHON_VERSION) setup.py install
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
	$(PIP_VERSION) install virtualenv
	$(PYTHON_VERSION) -m venv venv

versions:
	@echo #
	@echo Libaries versions
	. venv/bin/activate && \
	$(PYTHON_VERSION) --version && $(PIP_VERSION) --version
