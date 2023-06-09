install:
	poetry install
	
test:
	poetry run pytest

lint:
	@echo
	poetry run ruff ./src

fix:
	@echo
	poetry run ruff --fix ./src

build:
	poetry build

docs:
	poetry run mkdocs build

serve:
	poetry run mkdocs serve