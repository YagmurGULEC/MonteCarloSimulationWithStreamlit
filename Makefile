install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt


test:
	python test_run.py

all: install lint test
