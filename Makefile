lint:
	isort -y
	flake8 --config=.flake8
	mypy src/
	pylint src

run:
	@python src/manage.py ${ARGS}

run-dev:
	@python src/manage.py runserver
