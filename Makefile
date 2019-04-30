help:
	@echo "clean        - remove build artifacts"
	@echo "sdist        - package"

clean:
	rm -rf .tox/ build dist *.egg-info
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~'find -exec rm -f {} +

test:
	tox

sdist:
	python setup.py sdist
	ls -l dist

