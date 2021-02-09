CXX = g++
CXXFLAGS = -Wall -Werror -Wextra -pedantic -std=c++17 -g -fsanitize=address
LDFLAGS =  -fsanitize=address

EXEC = Makefile

ROOT:=./
VENV_BIN_DIR:="venv/bin"

PIP:="$(VENV_BIN_DIR)/pip"
TEST:="$(VENV_BIN_DIR)/pytest"

VIRTUALENV:=$(shell which virtualenv)
APP_NAME=pylexitext

clean:
	@find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	@find . -type d -name .pytest_cache -delete
	@rm -rf venv

# DEVELOPMENT

define create-venv
virtualenv venv -p python3
endef

venv:
	$(create-venv)
	@$(PIP) install --no-cache-dir -r $(REQUIREMENTS) | grep -v 'already satisfied' || true

test: venv 
	@$(TEST) -v

freeze:
	@$(PIP) freeze > requirements.txt

.PHONY: help stack clean venv test test-simple run docker-run docker-build up