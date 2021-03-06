# convenience makefile to boostrap & run buildout
# use `make options=-v` to run buildout with extra options

version = 2.7
python = bin/python
options =

all: docs tests

coverage: htmlcov/index.html

htmlcov/index.html: src/plone/hud/*.py bin/coverage
	@bin/coverage run --source=./src/plone/hud/ --branch bin/test
	@bin/coverage html -i
	@touch $@
	@echo "Coverage report was generated at '$@'."

docs: docs/html/index.html

docs/html/index.html: docs/*.rst src/plone/hud/*.py src/plone/hud/browser/*.py src/plone/hud/tests/*.py bin/sphinx-build
	bin/sphinx-build docs docs/html
	@touch $@
	@echo "Documentation was generated at '$@'."

bin/sphinx-build: .installed.cfg
	@touch $@

.installed.cfg: bin/buildout buildout.cfg buildout.d/*.cfg setup.py
	bin/buildout $(options)

bin/buildout: $(python) buildout.cfg bootstrap.py
	$(python) bootstrap.py -d --version 1.7.1
	@touch $@

$(python):
	virtualenv -p python$(version) --no-site-packages --no-setuptools .
	@touch $@

tests: .installed.cfg
	@bin/test --color
	@bin/flake8 setup.py
	@bin/flake8 src/plone/hud
	@for pt in `find src/plone/hud -name "*.pt"` ; do bin/zptlint $$pt; done
	@for xml in `find src/plone/hud -name "*.xml"` ; do bin/zptlint $$xml; done
	@for zcml in `find src/plone/hud -name "*.zcml"` ; do bin/zptlint $$zcml; done

clean:
	@rm -rf .coverage .installed.cfg .mr.developer.cfg bin docs/html htmlcov parts develop-eggs \
		src/plone.hud.egg-info lib include .Python

.PHONY: all docs tests clean
