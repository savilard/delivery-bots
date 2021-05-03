.PHONY: install
install:
		poetry install --no-dev

.PHONY: dev_install
dev_install:
		poetry install

.PHONY: lint
lint:
		poetry run mypy delivery_bots/
		poetry run isort delivery_bots/
		poetry run flake8 delivery_bots/
		poetry run black delivery_bots/ --skip-string-normalization --line-length 120

.PHONY: unit
unit:
	poetry run pytest .

.PHONY: test
test: lint unit
