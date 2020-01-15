lint:
	isort -y
	flake8 --config=.flake8
	mypy src/
	pylint src
