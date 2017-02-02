init:
	pip install -r requirements.txt

test:
	pytest

clean:
	# Remove all bytecode files
	find . -type f -name "*.py[co]" -delete
