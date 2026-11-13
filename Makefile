UV ?= uv

.PHONY: help fmt lint test

help: ## Show the available targets
	@grep -E '^[a-z]+:.*## ' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "%-8s %s\n", $$1, $$2}'

fmt: ## Format the code
	$(UV) run ruff format .

lint: ## Lint the code and check formatting
	$(UV) run ruff check .
	$(UV) run ruff format --check .

test: ## Run the test suite
	$(UV) run pytest
