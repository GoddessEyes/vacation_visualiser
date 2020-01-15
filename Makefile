lint:
	isort -y
	flake8 --config=.flake8
	mypy src/
	pylint src


    - name: flake8
      run: |
        pip install flake8
        flake8 --config=.flake8
    - name: pylint
      run: |
        pip install pylint
        pylint src
    - name: isort
      run: |
        pip install isort
        isort --check
    - name: mypy
      run: |
        pip install mypy
        mypy src/
