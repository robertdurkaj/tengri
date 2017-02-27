init:
	pip install -r requirements.txt

test:
	pytest
	# pytest --cov=tengri
	# pytest --cov=tengri --cov-report term-missing 

clean:
	# Remove all bytecode files
	find . -type f -name "*.py[co]" -delete

build:
	python setup.py bdist_wheel
