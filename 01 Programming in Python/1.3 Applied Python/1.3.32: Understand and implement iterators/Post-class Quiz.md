# Post-Class Quiz: Understand Iterators

## Q1: Which methods must a class implement to be an iterator?
A) `__init__()` and `__str__()`
B) `__iter__()` and `__next__()`
C) `__len__()` and `__getitem__()`

<details><summary>Answer</summary>
B) `__iter__()` and `__next__()`

Explanation: The iterator protocol requires two methods: `__iter__()` which returns the iterator object itself, and `__next__()` which returns the next value and raises StopIteration when done.
</details>

## Q2: What should the `__iter__()` method return?
A) The first element
B) A list of all elements
C) The iterator object (usually self)

<details><summary>Answer</summary>
C) The iterator object (usually self)

Explanation: The `__iter__()` method should return the iterator object itself, which is typically `self` for iterator classes. This allows the object to be used in for loops and with the iter() function.
</details>

## Q3: What happens when an iterator is exhausted?
A) It resets automatically
B) The `__next__()` method raises StopIteration
C) It returns None

<details><summary>Answer</summary>
B) The `__next__()` method raises StopIteration

Explanation: When an iterator has no more items to return, the `__next__()` method should raise the StopIteration exception. This signals to Python that the iteration is complete.
</details>

## Q4: What's the difference between an iterable and an iterator?
A) There is no difference
B) Iterables can be looped multiple times; iterators are consumed once
C) Iterators are faster

<details><summary>Answer</summary>
B) Iterables can be looped multiple times; iterators are consumed once

Explanation: An iterable is an object that can return an iterator (like lists, strings). An iterator is an object with `__next__()` that gets consumed during iteration. You can iterate over an iterable multiple times, but an iterator can only be used once.
</details>

## Q5: What does the built-in `next()` function do?
A) Creates a new iterator
B) Calls the `__next__()` method of an iterator
C) Reverses an iterable

<details><summary>Answer</summary>
B) Calls the `__next__()` method of an iterator

Explanation: The `next()` function is used to manually retrieve the next item from an iterator by calling its `__next__()` method. If there are no more items, it raises StopIteration (or returns a default value if provided).
</details>
