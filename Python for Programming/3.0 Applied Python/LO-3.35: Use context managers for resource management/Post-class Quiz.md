# Post-Class Quiz: Use Context Managers

## Q1: What is the main purpose of context managers?
A) To make code run faster
B) To ensure proper resource cleanup
C) To handle errors

<details><summary>Answer</summary>
B) To ensure proper resource cleanup

Explanation: Context managers guarantee that setup and cleanup code (like closing files) is executed, even if errors occur.
</details>

## Q2: Which methods must a class implement to be a context manager?
A) `__init__()` and `__del__()`
B) `__enter__()` and `__exit__()`
C) `__start__()` and `__stop__()`

<details><summary>Answer</summary>
B) `__enter__()` and `__exit__()`

Explanation: The context manager protocol requires `__enter__()` (called when entering the with block) and `__exit__()` (called when exiting).
</details>

## Q3: What does `__enter__()` return?
A) True or False
B) The resource/object to be used in the with block
C) Nothing (None)

<details><summary>Answer</summary>
B) The resource/object to be used in the with block

Explanation: `__enter__()` returns the value that gets assigned to the variable after `as` in the with statement.
</details>

## Q4: How can `__exit__()` suppress an exception?
A) By raising a different exception
B) By returning True
C) By calling sys.exit()

<details><summary>Answer</summary>
B) By returning True

Explanation: If `__exit__()` returns True, the exception is suppressed. Returning False (or None) allows the exception to propagate.
</details>

## Q5: What decorator can simplify creating context managers?
A) @contextmanager from contextlib
B) @property
C) @staticmethod

<details><summary>Answer</summary>
A) @contextmanager from contextlib

Explanation: The @contextmanager decorator from contextlib allows you to create context managers using generator functions with yield, simplifying the process.
</details>
