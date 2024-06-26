TEST = python -m pytest 
TEST_ARGS = -s --verbose --color=yes
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

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis
	rm -rf .coverage
	
.PHONY: test-all
test-all:
	make -C Assignments/A0/sorttwonumbers test
	make -C Assignments/A2/convexpolygonarea test

.PHONY: clean-all
test-all:
	make -C Assignments/A0/sorttwonumbers clean
	make -C Assignments/A2-OOD/convexpolygonarea clean