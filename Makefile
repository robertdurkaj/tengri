init:
	pip install -r requirements.txt

test:
	pytest
	# python -m unittest discover -v
	# nosetests -v --pdb

clean:
	# Remove all bytecode files
	find . -type f -name "*.py[co]" -delete
