# Makefile for  Sort Two Numbers solution

# Variables
PYTHON = python
SUBMIT_SCRIPT = submit
KATTIS = kattis
SOLUTION = convexpolygonarea.py
TEST_SCRIPT1 = test_polygons.py

# Default target
all: test

# Test the solution
test:
	$(PYTHON) $(TEST_SCRIPT1)


# Clean up generated files
clean:
	rm -f *.pyc
	rm -f *__pycache__*

# Submit the solution to Kattis
submit:
	$(KATTIS) $(SUBMIT_SCRIPT)

.PHONY: all test clean submit