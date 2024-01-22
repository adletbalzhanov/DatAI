api:
	uvicorn src.main:app --reload

run_linters:
	black . && isort . && bandit . && mypy . && flake8 .