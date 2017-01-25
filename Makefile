init:
	pip install -r requirements.txt

test:
	pytest
	# python -m unittest discover -v
	# nosetests -v --pdb
