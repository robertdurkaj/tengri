init:
	pip install -r requirements.txt

test:
	pytest
	# pytest --cov=tengri

clean:
	# Remove all bytecode files
	find . -type f -name "*.py[co]" -delete
