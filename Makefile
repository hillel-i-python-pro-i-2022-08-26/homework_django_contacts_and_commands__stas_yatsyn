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