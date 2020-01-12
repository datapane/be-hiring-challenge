.PHONY: start-server stop-server check-style

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

