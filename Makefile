export ROOT_DIR=${PWD}

run:
	-docker stop mariadb && docker rm mariadb
	docker-compose -f docker-compose.yml up
build:
	docker-compose -f docker-compose.yml build
test:
	-docker stop mariadb && docker rm mariadb
	docker-compose -f docker-compose.yml -p 'testing' run api bash ./test.sh $(filter-out $@,$(MAKECMDGOALS))
deploy:
	-docker stop mariadb && docker rm mariadb
	docker-compose -f docker-compose-db.yml up -d
	sh deploy.sh
teardown:
	docker-compose -f docker-compose.yml down
	sh teardown.sh
