# run homework
.PHONY: homework-i-run
homework-i-run:
	@python manage.py runserver

# install requirements
.PHONY: init-dev
init-dev:
	@python -m pip install --upgrade pip
	pip -requirement requirements.txt

# Run tools for files from commit.
.PHONY: pre-commit-run
pre-commit-run:
	@pre-commit run

# Run tools for all files.
.PHONY: pre-commit-run-all
pre-commit-run-all:
	@pre-commit run --all-files

# Init superuser (admin)
.PHONY: init-dev-i-create-superuser
init-dev-i-create-superuser:
	@DJANGO_SUPERUSER_PASSWORD=admin1234 python manage.py createsuperuser --user admin1 --email admin@gmail.com --no-input