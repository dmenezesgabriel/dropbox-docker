build:
	docker-compose build

shell:
	docker-compose run --rm dropbox /bin/sh

run:
	docker-compose up