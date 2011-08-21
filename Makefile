.PHONY: clean virtualenv virtualenv-clean

all: virtualenv install test

virtualenv: bin/activate

virtualenv-clean:
	rm -rf bin include lib lib64 share

clean:
	find . -name \*.pyc -print0 | xargs -r0 rm
	find . -name \*.dot -print0 | xargs -r0 rm
	find . -name \*.svg -print0 | xargs -r0 rm
	find . -name \*.png -print0 | xargs -r0 rm

bin/activate:
	virtualenv --no-site-packages --distribute .

freeze:
	pip freeze -E . > requirements.txt

install: virtualenv
	pip install -E . -r requirements.txt

bin: install

test: bin
	source bin/activate; unit2 discover -v
