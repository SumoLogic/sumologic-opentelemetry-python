.PHONY: install
install: install-lint


.PHONY: install-lint
install-lint:
	python3 -m pip install -r requirements-lint.txt

.PHONY: lint
lint:
	flake8 .
	black --check .
	isort --check .

.PHONY: format
format:
	black .
	isort .

# https://packaging.python.org/tutorials/packaging-projects/
.PHONY: build
build:
	rm -rf dist
	python3 -m pip install virtualenv
	python3 -m pip install --upgrade build
	python3 setup.py sdist bdist_wheel


.PHONY: push-test
push-test:
	python3 -m pip install --upgrade twine
	python3 -m twine upload --repository testpypi dist/*

.PHONY: push
push:
	python3 -m pip install --upgrade twine
	python3 -m twine upload dist/*
