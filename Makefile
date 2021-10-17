
.DEFAULT_TARGET: all

all: fetch report

workdir:
	mkdir -p workdir

setup:
	@poetry run pip install --upgrade pip; \
	poetry install

fetch: workdir
	@echo
	@echo "Fetching the data"
	@echo
	@poetry run scripts/fetch.py

report: workdir
	@echo
	@echo "Generating the report"
	@echo
	@poetry run scripts/report.py
