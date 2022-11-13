test:
	pytest . -v

precommit:
	cd docs && nbdev_export && nbdev_clean