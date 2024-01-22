api:
	uvicorn src.main:app --reload

run_linters:
	black . && isort . && bandit . && mypy . --check-untyped-defs && flake8 . --max-line-length=99