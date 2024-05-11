# Makefile for  Sort Two Numbers solution

# Variables
PYTHON = python
SUBMIT_SCRIPT = submit
KATTIS = kattis
SOLUTION = sorttwonumbers.py
TEST_SCRIPT1 = test_main.py
TEST_SCRIPT2 = test_unittests.py

# Default target
all: test

# Test the solution
test:
	$(PYTHON) $(TEST_SCRIPT1)

	$(PYTHON) $(TEST_SCRIPT2)

# Clean up generated files
clean:
	rm -f *.pyc
	rm -f *__pycache__*

# Submit the solution to Kattis
submit:
	$(KATTIS) $(SUBMIT_SCRIPT)

.PHONY: all test clean submit