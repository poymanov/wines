init: docker-down docker-pull \
		docker-build copy-example-files \
		docker-up

up: docker-up
down: docker-down
restart: down up

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

docker-pull:
	docker-compose pull

docker-build:
	docker-compose build

copy-example-files:
	cp example/wine.xlsx src/wine.xlsx
	cp .env.example .env