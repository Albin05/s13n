# Post-Class Quiz: Create Generator Functions

## Q1: What keyword is used to create a generator function?
A) return
B) yield
C) generate

<details><summary>Answer</summary>
B) yield

Explanation: The `yield` keyword is used in generator functions to return values one at a time while maintaining the function's state between calls. `return` would end the function completely.
</details>

## Q2: What is the main advantage of generators over regular functions that return lists?
A) They run faster
B) They use less memory
C) They have simpler syntax

<details><summary>Answer</summary>
B) They use less memory

Explanation: Generators yield values one at a time (lazy evaluation) instead of creating and storing all values in memory at once. This makes them much more memory-efficient, especially for large datasets or infinite sequences.
</details>

## Q3: What happens when you call a generator function?
```python
def my_gen():
    yield 1
    yield 2

result = my_gen()
```
A) It returns a list [1, 2]
B) It returns a generator object
C) It executes and returns 1

<details><summary>Answer</summary>
B) It returns a generator object

Explanation: Calling a generator function doesn't execute it immediately. Instead, it returns a generator object that can be iterated over. The function body executes only when you iterate or call next() on the generator.
</details>

## Q4: How do you get the next value from a generator?
A) generator.next()
B) next(generator)
C) generator.get_next()

<details><summary>Answer</summary>
B) next(generator)

Explanation: The built-in `next()` function is used to get the next value from a generator. When the generator is exhausted, it raises a StopIteration exception.
</details>

## Q5: What happens after a generator is exhausted?
```python
def count_to_three():
    yield 1
    yield 2
    yield 3

gen = count_to_three()
list(gen)  # [1, 2, 3]
list(gen)  # What is this?
```
A) [1, 2, 3]
B) []
C) Raises an error

<details><summary>Answer</summary>
B) []

Explanation: Once a generator is exhausted (all values have been yielded), subsequent iterations return an empty result. Generators can only be iterated once. To iterate again, you need to create a new generator object.
</details>
