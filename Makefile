run: *.py
	./monkey.py

test: *.py *_test.py
	export PYTHONPATH=".:$$PYTHONHOME:$$PYTHONPATH"; pytest
