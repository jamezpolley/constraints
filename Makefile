.PHONY: clean install virtualenv-clean test doc

ACTIVATE = . bin/activate

all: test doc

virtualenv: lib/python2.7/site.py

distclean: virtualenv-clean clean

virtualenv-clean:
	rm -rf bin include lib lib64 share .pipped build

clean:
	find . \( -name \*\.pyc -o -name \*\.dot -o -name \*\.svg -o -name \*\.png \) -delete
	hg clean

lib/python2.7/site.py:
	virtualenv --python=python2.7 --no-site-packages .

freeze:
	pip freeze -E . > requirements.txt

.pipped: requirements.txt
	$(ACTIVATE) && pip install -E . -r requirements.txt
	touch -r $^ -m $@

install: virtualenv .pipped

test: install
	$(ACTIVATE) && python -m testtools.run discover
	#$(ACTIVATE) && cd doc && $(MAKE) doctest

edit:
	$(EDITOR) *.py tests/*.py tests/*.yaml rules/*.yaml

doc: install
	$(ACTIVATE) && cd doc && $(MAKE)

