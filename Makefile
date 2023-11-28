install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt


test:
	python test_run.py
	python run_test_percolation.py

all: install lint test
