
.PHONY: lint, pytest, localserver

lint:
	flake8

test:
	./manage.py test

localserver:
	docker-compose build
	docker-compose up -d
