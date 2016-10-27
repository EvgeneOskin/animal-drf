
.PHONY: lint, pytest, localserver

lint:
	flake8

test:
	pytest

localserver:
	docker-compose build
	docker-compose up -d
