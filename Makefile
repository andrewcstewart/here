test:
	poetry run pytest

lint:
	@echo
	poetry run ruff ./src

fix:
	@echo
	poetry run ruff --fix ./src