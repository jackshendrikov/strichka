user:
	python manage.py createsuperuser --username admin --email 'admin@email.com'

shell:
	python manage.py shell

shell_prod:
	python manage.py shell --settings=config.settings.production

runserver:
	python manage.py runserver 0.0.0.0:8080

runserver_dev:
	python main/manage.py runserver 0.0.0.0:8080 --settings=config.settings.development

runserver_prod:
	python main/manage.py runserver 0.0.0.0:8080 --settings=config.settings.production

runserver_gunicorn:
	python manage.py collectstatic --noinput && \
	export PYTHONPATH=main:$$PYTHONPATH; \
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

style:
	flake8 main

types:
	mypy --namespace-packages \
		 -p "accounts" \
		 -p "common" \
		 -p "movies" \
		 --disable-error-code=no-redef \
		 --config-file setup.cfg && \
 	cd ../
