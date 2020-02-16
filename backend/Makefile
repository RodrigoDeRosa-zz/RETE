.PHONY: prepare run

install-core-libraries:
	apt-get install -y python3.8 python3.8-venv

prepare:
	python3.8 -m venv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt;

run:
	. venv/bin/activate; \
	export PYTHONPATH=$PYTHONPATH:$(pwd); \
	python3.8 app.py