.PHONY: start-server stop-server check-style install-cli run stop

start-server: ## Start container for dataset server
	@echo Starting dataset server
	docker-compose build
	docker-compose up -d

stop-server: ## Stop container for dataset server
	@echo Stopping dataset server
	docker-compose down

check-style: ## Run multiple linters against all modules
	@echo Running lint
	sh scripts/lint.sh || exit 1
	@echo success

install-cli: ## Install dataset-cli to interact with server
	pip install -r cli/requirements.txt
	pip install --editable cli/.

run: start-server install-cli

stop: stop-server



