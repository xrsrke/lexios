test:
	pytest ./tests --cov --diff-width=60

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt
	pre-commit install

precommit:
	cd docs && nbdev_export && nbdev_clean
