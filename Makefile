restart: stop start

start:
	docker-compose up -d

stop:
	docker-compose down

logs:
	docker-compose logs -f

flush:
	docker-compose down -v

build:
	docker-compose build