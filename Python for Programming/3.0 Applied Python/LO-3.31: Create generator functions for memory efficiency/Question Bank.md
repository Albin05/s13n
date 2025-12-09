# Question Bank: Create Generator Functions

## Problem 1 (Easy)

**Title:** Simple Number Generator

**Problem Statement:**
Create a generator function called `generate_evens(n)` that yields even numbers from 0 to n (inclusive).

**Input Format:**
An integer n is provided.

**Output Format:**
Yield even numbers one at a time.

**Sample Input:**
```python
for num in generate_evens(10):
    print(num, end=" ")
```

**Sample Output:**
```
0 2 4 6 8 10
```

**Constraints:**
- Use yield keyword
- n will be a positive integer
- Include n if it's even

---

## Problem 2 (Easy)

**Title:** Countdown Generator

**Problem Statement:**
Create a generator function `countdown(n)` that counts down from n to 1, yielding each number.

**Input Format:**
An integer n is provided.

**Output Format:**
Yield numbers from n down to 1.

**Sample Input:**
```python
for num in countdown(5):
    print(num, end=" ")
```

**Sample Output:**
```
5 4 3 2 1
```

**Constraints:**
- Use yield keyword
- Count down to 1 (inclusive)
- n will be a positive integer

---

## Problem 3 (Medium)

**Title:** Fibonacci Generator

**Problem Statement:**
Create a generator function `fibonacci(n)` that yields the first n Fibonacci numbers. The Fibonacci sequence starts with 0, 1, and each subsequent number is the sum of the previous two.

**Input Format:**
An integer n representing how many Fibonacci numbers to generate.

**Output Format:**
Yield the first n Fibonacci numbers.

**Sample Input:**
```python
for num in fibonacci(8):
    print(num, end=" ")
```

**Sample Output:**
```
0 1 1 2 3 5 8 13
```

**Constraints:**
- Use yield keyword
- n >= 1
- First two numbers are 0 and 1

---

## Problem 4 (Medium)

**Title:** Batch Data Generator

**Problem Statement:**
Create a generator function `batch_data(items, batch_size)` that takes a list and yields items in batches of the specified size. The last batch may have fewer items if the list length is not evenly divisible by batch_size.

**Input Format:**
A list of items and an integer batch_size.

**Output Format:**
Yield lists (batches) of the specified size.

**Sample Input:**
```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for batch in batch_data(data, 3):
    print(batch)
```

**Sample Output:**
```
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
[10]
```

**Constraints:**
- Use yield keyword
- batch_size >= 1
- Handle remaining items in final batch

---

## Problem 5 (Hard)

**Title:** Prime Number Generator with Limit

**Problem Statement:**
Create a generator function `prime_generator(limit)` that yields prime numbers up to and including the limit. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

**Input Format:**
An integer limit.

**Output Format:**
Yield all prime numbers up to and including the limit.

**Sample Input:**
```python
for prime in prime_generator(30):
    print(prime, end=" ")
```

**Sample Output:**
```
2 3 5 7 11 13 17 19 23 29
```

**Constraints:**
- Use yield keyword
- limit >= 2
- Yield primes in ascending order
- Include the limit if it's prime

**Hint:**
Create a helper function to check if a number is prime. A number n is prime if it's not divisible by any number from 2 to sqrt(n).
