THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: help build up stop restart  destroy log shell manage makemigrations migrate test

help:
	make -pRrq  -f $(THIS_FILE) : 2>/dev/null |	awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

build:
	docker-compose -f docker-compose.yml build $(c)
run:
	docker-compose -f docker-compose.yml up -d $(c)
stop:
	docker-compose -f docker-compose.yml stop $(c)
restart:
	docker-compose -f docker-compose.yml stop $(c)
	docker-compose -f docker-compose.yml up -d $(c)
destroy:
	docker-compose -f docker-compose.yml down -v $(c)
log:
	docker-compose -f docker-compose.yml logs --tail=150 -f theatre-app
shell:
	docker-compose -f docker-compose.yml exec theatre-app /bin/bash
manage:
	docker-compose -f docker-compose.yml exec theatre-app python manage.py $(c)
makemigrations:
	docker-compose -f docker-compose.yml exec theatre-app python manage.py makemigrations
migrate:
	docker-compose -f docker-compose.yml exec theatre-app python manage.py migrate
test:
	docker-compose -f docker-compose.yml exec theatre-app python manage.py test
