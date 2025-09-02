PYTHON=.venv/bin/python
PIP=.venv/bin/pip
REQUIREMENTS=requirements.txt

# === Targets ===
.PHONY: help run install test clean

help:
	@echo "Usage: make <target>"
	@echo "Available targets:"
	@echo "  run                 Run the application (FastAPI via Uvicorn)"
	@echo "  install             Install dependencies"
	@echo "  test                Run unit tests"
	@echo "  clean               Remove *.pyc and __pycache__"

run:
	@echo "Starting microservice in development mode..."
	PYTHONPATH=$(PWD) $(PYTHON) -m app.main


install:
	$(PIP) install --no-cache-dir -r $(REQUIREMENTS) --only-binary=:all:

test:
	$(PYTHON) -m unittest discover -s tests

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.pyc' -delete

