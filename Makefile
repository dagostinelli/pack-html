.PHONY: clean build lint install test

default: test

venv_directory = ./venv

clean:
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *.egg-info
	@rm -rf src/*.egg-info
	@rm -rf $(venv_directory)/
	@rm -rf .eggs/
	@rm -rf .pytest_cache/
	@find . -iname '*.py[co]' -delete
	@find . -iname '__pycache__' -delete

prep: $(venv_directory)

$(venv_directory):
	@python3 -m venv venv
	$(venv_directory)/bin/pip install --upgrade pip
	$(venv_directory)/bin/pip install flake8
	@$(venv_directory)/bin/python3 setup.py install

lint:
	@$(venv_directory)/bin/flake8

test: prep lint
	@python3 setup.py test
	cat example-data/index.html | $(venv_directory)/bin/python3 -m pack_html --root-dir example-data/ -
	# > x.html

build: prep
	@python3 setup.py sdist
	@python3 setup.py bdist
	@python3 setup.py bdist_wheel

dev-run:
	@echo Do this
	@echo python3 -m venv venv
	@echo source venv/bin/activate
	@echo python3 setup.py install
	@echo python3 -m src.pack-html
	@echo deactivate
