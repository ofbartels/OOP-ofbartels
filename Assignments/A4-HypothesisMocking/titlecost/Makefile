# Makefile for  Morse Code Palindromes solution

# Variables
PYTHON = python
SUBMIT_SCRIPT = submit
KATTIS = kattis
SOLUTION = titlecost.py
TEST_SCRIPT1 = test_title_cost_calculator.py
TEST_SCRIPT2 = test_input_handler.py
TEST_SCRIPT3 = test_integration.py
TEST_SCRIPT4 = test_titlecost.py

TEST = python -m pytest 
TEST_ARGS = -s --verbose --color=yes --cov=. --cov-report=term-missing
TYPE_CHECK = mypy --strict --allow-untyped-decorators --ignore-missing-imports --exclude /docs/
STYLE_CHECK = flake8
STYLE_FIX = autopep8 --in-place --recursive --aggressive --aggressive

.PHONY: all
all: check-style check-type run-test

.PHONY: check-type
check-type:
	$(TYPE_CHECK) .

.PHONY: check-style
check-style:
	$(STYLE_CHECK) .

# discover and run all tests
.PHONY: run-test
run-test:
	$(TEST) $(TEST_ARGS) .

.PHONY: fix-style
fix-style:
	$(STYLE_FIX) .

# Clean up generated files
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis
	rm -rf .coverage

# Submit the solution to Kattis
submit:
	$(KATTIS) $(SUBMIT_SCRIPT)

.PHONY: all test clean submit