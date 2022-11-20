test:
	pytest ./tests --cov --diff-width=60

install:
	pip install -r requirements.txt

dev-setup:
	pip install -r requirements_dev.txt
	pre-commit install

precommit:
	cd docs && nbdev_export && nbdev_clean
