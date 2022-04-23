install: 
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	
format:
	black *.py

test:
	python -m pytest -vv test_app.py -W ignore::DeprecationWarning -W ignore::RuntimeWarning