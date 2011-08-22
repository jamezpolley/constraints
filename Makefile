.PHONY: clean virtualenv virtualenv-clean test

all: virtualenv test

clean:
	find . -name \*.pyc -print0 | xargs -0 rm
	find . -name \*.dot -print0 | xargs -0 rm
	find . -name \*.svg -print0 | xargs -0 rm
	find . -name \*.png -print0 | xargs -0 rm
	rm -rf bin/ include/ lib/ man/ share/

bin/activate:
	virtualenv --no-site-packages --distribute .

virtualenv: bin/activate

virtualenv-clean:
	rm -rf bin include lib lib64 share

freeze:
	pip freeze -E . > requirements.txt

lib: bin/activate
	source bin/activate; pip install -E . -r requirements.txt
	touch -r bin/activate lib

test: bin/activate lib
	source bin/activate; unit2 discover -v
