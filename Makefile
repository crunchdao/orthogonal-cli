PYTHON=python
PIP=$(PYTHON) -m pip

init:
	$(PIP) install -r requirements.txt

install: init
	$(PIP) install -e .

uninstall:
	$(PIP) uninstall orthogonal-cli

build:
	rm -rf build *.egg-info dist
	python setup.py sdist bdist_wheel

.PHONY: init install uninstall build
