PYLINT = flake8

FORCE:

dev_env: FORCE 
	pip3 install -r requirements-dev.txt

tests: FORCE
	$(PYLINT) *.py
	nosetests --exe --with-coverage --verbose --cover-package=SoftEng

prod: tests
	git commit -a
	git push origin main

%.py: FORCE
	nosetests tests.test_$* --nocapture
