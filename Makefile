docker_build:
	docker-compose up -d --build

docker_up:
	docker-compose up -d

docker_start:
	docker-compose start

docker_down:
	docker-compose down

docker_destroy:
	docker-compose down -v

docker_stop:
	docker-compose stop

docker_restart:
	docker-compose stop
	docker-compose up -d

docker_logs:
	docker-compose logs --tail=100 -f

docker_remove_dangling_images:
	docker rmi $(docker images --filter "dangling=true" -q --no-trunc)

user:
	python manage.py createsuperuser --username admin --email 'admin@email.com'

shell:
	python manage.py shell

shell_prod:
	python manage.py shell --settings=config.settings.production

runserver:
	python manage.py runserver 0.0.0.0:8080

runserver_dev:
	python manage.py runserver 0.0.0.0:8080 --settings=config.settings.development

runserver_prod:
	python manage.py runserver 0.0.0.0:8080 --settings=config.settings.production

runserver_gunicorn:
	python manage.py collectstatic --noinput && \
 	gunicorn -b :8080 entrypoint:app --timeout 600 --workers=5 --threads=2

migrate:
	python manage.py makemigrations && \
 	python manage.py migrate --run-syncdb

migrate_prod:
	python manage.py migrate --settings=config.settings.production

install_hooks:
	pip install -r requirements.txt; \
	pre-commit install

run_hooks_on_all_files:
	pre-commit run --all-files

flake:
	flake8 accounts common movies

isort:
	isort accounts common movies --diff

black:
	 black accounts common movies --check

types:
	mypy --namespace-packages \
		 -p "accounts" \
		 -p "common" \
		 -p "movies" \
		 --disable-error-code=no-redef \
		 --config-file setup.cfg

lint:
	make flake
	make isort
	make black
