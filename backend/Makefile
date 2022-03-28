test:
	poetry run coverage run --source=src -m pytest -vv tests/

run_dev:
	poetry run uvicorn src.main:app --reload

install:
	poetry install

lint:
	poetry run black src tests

static_check:
	poetry run mypy src tests
