user:
	python manage.py createsuperuser --username admin --email 'admin@email.com'

shell:
	python manage.py shell

runserver:
	python manage.py runserver 0.0.0.0:8080

runserver_gunicorn:
	python manage.py collectstatic --noinput && \
	export PYTHONPATH=main:$$PYTHONPATH; \
 	gunicorn -b :8080 entrypoint:app --timeout 600 --workers=5 --threads=2

migrate:
	python manage.py makemigrations && \
 	python manage.py migrate --run-syncdb

install_hooks:
	pip install -r requirements.txt; \
	pre-commit install

run_hooks_on_all_files:
	pre-commit run --all-files

style:
	flake8 main

types:
	mypy --namespace-packages \
		 -p "common" \
		 -p "movies" \
		 --disable-error-code=no-redef \
		 --config-file setup.cfg && \
 	cd ../
