# Post-Class Quiz: Apply Decorators

## Q1: What does the @ symbol do in Python?
A) It's a comment marker
B) It applies a decorator to a function
C) It creates a class

<details><summary>Answer</summary>
B) It applies a decorator to a function

Explanation: The @ symbol is syntactic sugar for applying decorators. `@decorator` before a function is equivalent to `function = decorator(function)`.
</details>

## Q2: What must a decorator function return?
A) The original function
B) A wrapper function
C) None

<details><summary>Answer</summary>
B) A wrapper function

Explanation: A decorator must return a function (typically a wrapper) that will replace the original function. This wrapper usually calls the original function with additional behavior.
</details>

## Q3: How do you create a decorator that takes parameters?
A) Add parameters to the wrapper function
B) Create a decorator factory (function that returns a decorator)
C) Use global variables

<details><summary>Answer</summary>
B) Create a decorator factory (function that returns a decorator)

Explanation: To create a decorator with parameters, you need three levels of functions: the outermost takes the parameters, the middle is the decorator, and the innermost is the wrapper.
</details>

## Q4: What is the purpose of *args and **kwargs in decorator wrappers?
A) They're required by Python
B) They allow the decorator to work with any function signature
C) They improve performance

<details><summary>Answer</summary>
B) They allow the decorator to work with any function signature

Explanation: Using `*args` and `**kwargs` in the wrapper function allows the decorator to handle functions with any number of positional and keyword arguments.
</details>

## Q5: When multiple decorators are applied, in what order are they executed?
```python
@decorator1
@decorator2
def func():
    pass
```
A) Top to bottom (decorator1 then decorator2)
B) Bottom to top (decorator2 then decorator1)
C) Randomly

<details><summary>Answer</summary>
B) Bottom to top (decorator2 then decorator1)

Explanation: Decorators are applied from bottom to top. The decorator closest to the function is applied first, then the one above it, and so on.
</details>
