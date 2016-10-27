
.PHONY: lint

lint:
	flake8

localserver:
	docker-compose build
	docker-compose up -d
