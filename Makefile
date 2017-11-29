run: $(wildcard monkey/*.py)
	monkey/repl.py

test: $(wildcard monkey/*.py) $(wildcard test/*.py)
	export PYTHONPATH=".:$$PYTHONHOME:$$PYTHONPATH"; pytest
