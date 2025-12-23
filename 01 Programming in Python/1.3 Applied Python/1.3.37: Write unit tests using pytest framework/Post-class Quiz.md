# Post-Class Quiz: Write Unit Tests with pytest

## Q1: What naming convention must test functions follow for pytest to discover them?
A) start_test_*
B) test_*
C) *_test

<details><summary>Answer</summary>
B) test_*

Explanation: pytest automatically discovers test functions that start with `test_`. Test files should also start with `test_` or end with `_test.py`.
</details>

## Q2: How do you test that a function raises an exception?
A) try-except block
B) pytest.raises context manager
C) assert raises()

<details><summary>Answer</summary>
B) pytest.raises context manager

Explanation: Use `with pytest.raises(ExceptionType):` to test that code raises a specific exception.
</details>

## Q3: What is the purpose of fixtures in pytest?
A) To fix bugs
B) To provide reusable test setup code
C) To mark tests as skipped

<details><summary>Answer</summary>
B) To provide reusable test setup code

Explanation: Fixtures provide a way to set up common test data or resources that can be reused across multiple test functions.
</details>

## Q4: How do you run tests in verbose mode?
A) pytest -v
B) pytest --verbose
C) Both A and B

<details><summary>Answer</summary>
C) Both A and B

Explanation: Both `pytest -v` and `pytest --verbose` run tests in verbose mode, showing each test function result individually.
</details>

## Q5: What does @pytest.mark.parametrize do?
A) Marks a test to be skipped
B) Allows running the same test with different inputs
C) Creates a test fixture

<details><summary>Answer</summary>
B) Allows running the same test with different inputs

Explanation: `@pytest.mark.parametrize` enables running the same test function with multiple sets of parameters, reducing code duplication.
</details>
