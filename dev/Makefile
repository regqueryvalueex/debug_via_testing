include .env

clean_py_cache:
	docker-compose -f compose-app.yml exec debug_via_testing find /app -name \*.pyc -delete
	docker-compose -f compose-app.yml exec debug_via_testing find /app -path '*/__pycache__/*' -delete
	docker-compose -f compose-app.yml exec debug_via_testing find /app -type d -name '__pycache__' -delete
	docker-compose -f compose-app.yml exec debug_via_testing find /app -path '*/.pytest_cache/*' -delete
	docker-compose -f compose-app.yml exec debug_via_testing find /app -type d -name '.pytest_cache' -delete

up:
	docker-compose up

stop:
	docker-compose stop

down:
	docker-compose down

build:
	docker-compose up --build

test:
	docker-compose exec debug_via_testing pytest tests
