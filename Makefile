install:
	uv sync

format:
	uv run black .

lint:
	uv run pylint mylib cli api
test:
	uv run pytest -q --cov=mylib --cov=cli --cov=api --cov-report=term-missing

refactor: format lint

all: install format lint test
