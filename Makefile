test:
	pytest . -v

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

precommit:
	cd docs && nbdev_export && nbdev_clean