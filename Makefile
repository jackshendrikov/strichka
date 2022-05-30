runserver:
	python main/manage.py runserver 0.0.0.0:8080

runserver_gunicorn:
	python main/manage.py collectstatic --noinput && \
	export PYTHONPATH=main:$$PYTHONPATH; \
 	gunicorn -b :8080 entrypoint:app --timeout 600 --workers=5 --threads=2

migrate:
	python main/manage.py makemigrations && \
 	python main/manage.py migrate --run-syncdb

install_hooks:
	pip install -r requirements.txt; \
	pre-commit install

run_hooks_on_all_files:
	pre-commit run --all-files

style:
	flake8 main

types:
	mypy --namespace-packages \
		 -p "config" \
		 --disable-error-code=no-redef \
		 --config-file setup.cfg && \
 	cd ../
