# Editorials: Create Generator Functions

## Problem 1: Simple Number Generator

```python
def generate_evens(n):
    """Generator that yields even numbers from 0 to n"""
    for i in range(0, n + 1, 2):
        yield i

# Test
for num in generate_evens(10):
    print(num, end=" ")
# Output: 0 2 4 6 8 10
```

### Explanation
The generator uses `range(0, n + 1, 2)` to iterate through even numbers. The step of 2 ensures we only get even numbers. The `yield` keyword returns each number one at a time without storing all values in memory.

**Alternative solution:**
```python
def generate_evens(n):
    current = 0
    while current <= n:
        yield current
        current += 2
```

**Time Complexity:** O(n/2) = O(n)
**Space Complexity:** O(1) - generator uses constant memory

---

## Problem 2: Countdown Generator

```python
def countdown(n):
    """Generator that counts down from n to 1"""
    while n > 0:
        yield n
        n -= 1

# Test
for num in countdown(5):
    print(num, end=" ")
# Output: 5 4 3 2 1
```

### Explanation
The generator uses a while loop that continues as long as n is greater than 0. Each iteration yields the current value of n, then decrements it. The loop stops when n reaches 0.

**Alternative solution using range:**
```python
def countdown(n):
    for i in range(n, 0, -1):
        yield i
```

**Time Complexity:** O(n)
**Space Complexity:** O(1) - generator uses constant memory

---

## Problem 3: Fibonacci Generator

```python
def fibonacci(n):
    """Generator that yields first n Fibonacci numbers"""
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Test
for num in fibonacci(8):
    print(num, end=" ")
# Output: 0 1 1 2 3 5 8 13
```

### Explanation
1. Initialize `a` and `b` to the first two Fibonacci numbers (0 and 1)
2. Use a counter to track how many numbers have been generated
3. Yield the current value of `a`
4. Update `a` and `b` using simultaneous assignment: `a` becomes `b`, and `b` becomes `a + b`
5. Increment the counter
6. Continue until n numbers have been yielded

**How the update works:**
- Initially: a=0, b=1
- After 1st yield: a=1, b=1 (0+1)
- After 2nd yield: a=1, b=2 (1+1)
- After 3rd yield: a=2, b=3 (1+2)
- And so on...

**Time Complexity:** O(n)
**Space Complexity:** O(1) - only stores two numbers at a time

---

## Problem 4: Batch Data Generator

```python
def batch_data(items, batch_size):
    """Generator that yields items in batches"""
    batch = []

    for item in items:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []

    # Yield remaining items if any
    if batch:
        yield batch

# Test
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for batch in batch_data(data, 3):
    print(batch)
# Output:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# [10]
```

### Explanation
1. Initialize an empty batch list
2. Iterate through each item in the input items
3. Add each item to the current batch
4. When the batch reaches the specified size, yield it and reset to empty list
5. After the loop, check if there are remaining items in the batch
6. If yes, yield the final (possibly incomplete) batch

**Alternative solution using slicing:**
```python
def batch_data(items, batch_size):
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]
```

**Time Complexity:** O(n) where n is the number of items
**Space Complexity:** O(batch_size) for storing each batch

---

## Problem 5: Prime Number Generator with Limit

```python
def prime_generator(limit):
    """Generator that yields prime numbers up to limit"""

    def is_prime(n):
        """Helper function to check if a number is prime"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        # Check odd divisors up to sqrt(n)
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    # Start from 2 (first prime)
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

# Test
for prime in prime_generator(30):
    print(prime, end=" ")
# Output: 2 3 5 7 11 13 17 19 23 29
```

### Explanation

**Helper function `is_prime(n)`:**
1. Numbers less than 2 are not prime
2. 2 is prime (the only even prime)
3. All other even numbers are not prime
4. For odd numbers, check divisibility by odd numbers from 3 to √n
5. If any divisor is found, the number is not prime
6. If no divisors found, the number is prime

**Main generator:**
1. Iterate through all numbers from 2 to limit (inclusive)
2. For each number, check if it's prime using the helper function
3. If prime, yield it

**Why check only up to √n?**
If n has a divisor greater than √n, it must also have a divisor smaller than √n. So checking up to √n is sufficient.

**More efficient solution using Sieve of Eratosthenes:**
```python
def prime_generator(limit):
    """More efficient using Sieve of Eratosthenes"""
    if limit < 2:
        return

    # Create boolean array "prime[0..limit]"
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            # Mark multiples of p as not prime
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1

    # Yield all numbers marked as prime
    for num in range(2, limit + 1):
        if is_prime[num]:
            yield num
```

**Time Complexity:**
- Simple approach: O(n * √n) where n is the limit
- Sieve approach: O(n log log n)

**Space Complexity:**
- Simple approach: O(1)
- Sieve approach: O(n) for the boolean array
