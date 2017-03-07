.PHONY:	build clean


init:
	pip install -r requirements.txt


test:
	py.test


manualtest:
	python tests/manual.py


coverage:
# pytest --cov=tengri
	py.test --cov=tengri --cov-report term-missing 


# Remove all bytecode files
bytecode: 
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete


build:
	python setup.py bdist_wheel


publish:
	pip install twine
	twine upload dist/*


clean:
	-rm -R dist
	-rm -R build
