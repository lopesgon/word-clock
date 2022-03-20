PORT=5000
PYTHON_VERSION=python3
PIP_VERSION=pip3
VENV_FOLDER=mvenv

install: create-venv versions
	@echo #
	@echo Installing project dependencies
	. $(VENV_FOLDER)/bin/activate && \
	$(PIP_VERSION) install -e .

run-debug:
	@echo #
	@echo Running debug mode
	. $(VENV_FOLDER)/bin/activate && \
	export FLASK_APP=app/main.py && \
	export FLASK_ENV=development && \
	flask run -p $(PORT)

run:
	@echo # 
	@echo Running
	. $(VENV_FOLDER)/bin/activate && \
	export FLASK_APP=src && \
	export FLASK_ENV=production && \
	flask run -p $(PORT)

build:
	@echo Building setup.py...
	. $(VENV_FOLDER)/bin/activate && \
	$(PYTHON_VERSION) setup.py install
	@echo ...building ended.

clean: clean-vm clean-pyc clean-build
clean-vm:
	rm -rf $(VENV_FOLDER)/
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
	$(PYTHON_VERSION) -m venv $(VENV_FOLDER)

versions:
	@echo #
	@echo Libaries versions
	. $(VENV_FOLDER)/bin/activate && \
	$(PYTHON_VERSION) --version && $(PIP_VERSION) --version
