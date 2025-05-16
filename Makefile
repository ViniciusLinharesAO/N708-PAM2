# Variáveis
APP_NAME=user-api

# Build e setup
build:
	docker-compose build

up:
	docker-compose up

upd:
	docker-compose up -d

down:
	docker-compose down

restart:
	docker-compose down && docker-compose up

# Gerenciamento do banco de dados (via Flask-Migrate)
db-init:
	docker-compose exec api flask db init

db-migrate:
	docker-compose exec api flask db migrate -m "migration"

db-upgrade:
	docker-compose exec api flask db upgrade

db-downgrade:
	docker-compose exec api flask db downgrade

# Shell e logs
bash:
	docker-compose exec api bash

logs:
	docker-compose logs -f

# Limpar tudo (containers e volumes)
clean:
	docker-compose down -v --remove-orphans

# Teste do app (você pode personalizar com pytest ou similar depois)
test:
	docker-compose exec api python -m unittest discover

dev:
	python run.py
