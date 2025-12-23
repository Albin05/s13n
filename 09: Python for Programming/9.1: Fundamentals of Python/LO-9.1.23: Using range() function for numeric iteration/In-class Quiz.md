# Post-class Quiz: Using Range() Function for Numeric Iteration

Test your understanding of the range() function in Python.

---

## Q1: What is the output?
```python
for i in range(5):
    print(i, end=" ")
```

A) 1 2 3 4 5
B) 0 1 2 3 4
C) 0 1 2 3 4 5
D) 1 2 3 4

<details><summary>Answer</summary>
**B) 0 1 2 3 4**

**Explanation:** `range(5)` with a single argument starts at 0 (default), stops before 5, and steps by 1 (default). It generates 5 numbers: 0, 1, 2, 3, 4. The stop value (5) is **exclusive** and not included.
</details>

---

## Q2: How do you generate numbers from 1 to 10 (inclusive)?

A) `range(10)`
B) `range(1, 10)`
C) `range(1, 11)`
D) `range(0, 10)`

<details><summary>Answer</summary>
**C) `range(1, 11)`**

**Explanation:** The stop value in range() is **exclusive** (never included). To get 1 through 10, you need to start at 1 and stop before 11. Think of it as: start at 1, while i < 11. This is the most common mistake with range()!
</details>

---

## Q3: What is the output?
```python
for i in range(2, 10, 2):
    print(i, end=" ")
```

A) 2 4 6 8 10
B) 2 4 6 8
C) 0 2 4 6 8
D) 2 3 4 5 6 7 8 9

<details><summary>Answer</summary>
**B) 2 4 6 8**

**Explanation:** `range(2, 10, 2)` means start at 2, stop before 10, step by 2. This generates: 2, 4, 6, 8. The value 10 is not included because the stop is exclusive. The step of 2 creates even numbers.
</details>

---

## Q4: What does the third argument in range() control?

A) The starting value
B) The stopping value
C) The step/increment value
D) The number of iterations

<details><summary>Answer</summary>
**C) The step/increment value**

**Explanation:** In `range(start, stop, step)`, the third argument controls how much to increment (or decrement) each iteration. Default step is 1. Step of 2 counts by twos, step of -1 counts backwards.
</details>

---

## Q5: What is the output?
```python
for i in range(10, 0, -1):
    print(i, end=" ")
```

A) 10 9 8 7 6 5 4 3 2 1
B) 10 9 8 7 6 5 4 3 2 1 0
C) 0 1 2 3 4 5 6 7 8 9 10
D) Error - range can't count backwards

<details><summary>Answer</summary>
**A) 10 9 8 7 6 5 4 3 2 1**

**Explanation:** Negative step (-1) makes range count backwards. Start at 10, stop before 0 (exclusive), decrement by 1. This gives 10, 9, 8, ..., 1. Zero is not included because stop is exclusive.
</details>

---

## Q6: What happens with `range(10, 1)`?

A) Generates 10, 9, 8, ..., 2
B) Generates 1, 2, 3, ..., 10
C) Generates an empty sequence (nothing)
D) Causes an error

<details><summary>Answer</summary>
**C) Generates an empty sequence (nothing)**

**Explanation:** When start (10) is greater than stop (1) with a positive step (default 1), range is empty. You can't count UP from 10 to 1. To count backwards, you MUST use negative step: `range(10, 1, -1)`.
</details>

---

## Q7: What is the default start value if not specified?

A) 1
B) 0
C) None
D) 10

<details><summary>Answer</summary>
**B) 0**

**Explanation:** `range(5)` is equivalent to `range(0, 5)`. The default start is 0, which aligns with Python's zero-based indexing. This is why `range(5)` gives 0, 1, 2, 3, 4 (five numbers starting from 0).
</details>

---

## Q8: What is the default step value if not specified?

A) 0
B) 1
C) 2
D) -1

<details><summary>Answer</summary>
**B) 1**

**Explanation:** If the step isn't specified, it defaults to 1. `range(1, 10)` is equivalent to `range(1, 10, 1)`, which counts 1, 2, 3, 4, 5, 6, 7, 8, 9.
</details>

---

## Q9: How many numbers does `range(10)` generate?

A) 9
B) 10
C) 11
D) 0

<details><summary>Answer</summary>
**B) 10**

**Explanation:** `range(10)` generates exactly 10 numbers: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. The single-argument form `range(n)` generates n numbers starting from 0. This is useful when you need exactly n iterations.
</details>

---

## Q10: What is the output?
```python
for i in range(1, 10, 3):
    print(i, end=" ")
```

A) 1 2 3 4 5 6 7 8 9
B) 1 4 7
C) 1 4 7 10
D) 3 6 9

<details><summary>Answer</summary>
**B) 1 4 7**

**Explanation:** Start at 1, stop before 10, step by 3. Sequence: 1, 1+3=4, 4+3=7, 7+3=10 (but 10 is excluded). Result: 1, 4, 7. The step controls the increment between values.
</details>

---

## Q11: Can range() accept float (decimal) arguments?

A) Yes, any number type works
B) No, only integers are allowed
C) Yes, but it rounds them
D) Only the step can be a float

<details><summary>Answer</summary>
**B) No, only integers are allowed**

**Explanation:** range() only accepts integer arguments. `range(1.5, 5.5)` causes a TypeError. If you need float ranges, you'd need to use numpy.arange() or create your own solution with a while loop.
</details>

---

## Q12: What is the difference between range() and a list?

A) No difference, they're the same
B) range() is memory-efficient and generates on demand
C) Lists are faster
D) range() stores all values in memory

<details><summary>Answer</summary>
**B) range() is memory-efficient and generates on demand**

**Explanation:** range() is a "lazy" sequence - it generates values one at a time as needed, not all at once. `range(1000000)` uses tiny memory. `list(range(1000000))` creates a huge list in memory. This makes range very efficient for large sequences.
</details>

---

## Q13: What is the output?
```python
print(list(range(3, 8)))
```

A) [3, 4, 5, 6, 7]
B) [3, 4, 5, 6, 7, 8]
C) [4, 5, 6, 7]
D) [3, 8]

<details><summary>Answer</summary>
**A) [3, 4, 5, 6, 7]**

**Explanation:** `range(3, 8)` starts at 3 and stops before 8 (exclusive). Converting to a list with `list()` shows all generated values: [3, 4, 5, 6, 7]. The stop value (8) is never included.
</details>

---

## Q14: Which generates odd numbers from 1 to 9?

A) `range(1, 9, 2)`
B) `range(1, 10, 2)`
C) `range(0, 9, 2)`
D) `range(2, 10, 2)`

<details><summary>Answer</summary>
**B) `range(1, 10, 2)`**

**Explanation:** Start at 1 (first odd), stop before 10, step by 2. Generates: 1, 3, 5, 7, 9. Option A would give 1, 3, 5, 7 (missing 9 because 9 < 10 but 9 is not < 9). The step of 2 from an odd start gives odd numbers.
</details>

---

## Q15: What is the output?
```python
for i in range(5, 5):
    print(i)
print("Done")
```

A) 5
   Done
B) Error
C) Done
D) Nothing

<details><summary>Answer</summary>
**C) Done**

**Explanation:** `range(5, 5)` has start equal to stop, creating an empty range. The loop body never executes (zero iterations). The program continues and prints "Done". This is valid - range can be empty without causing an error.
</details>

---

## Score Interpretation

- **13-15 correct**: Excellent! You've mastered the range() function.
- **10-12 correct**: Good work! Review exclusive stop and step parameters.
- **7-9 correct**: Fair. Practice more with different range forms.
- **Below 7**: Review the lesson on range() function carefully.

## Key Concepts to Remember

1. **Three forms**: `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
2. **Exclusive stop**: Stop value is NEVER included (like < operator)
3. **Default start**: 0 if not specified
4. **Default step**: 1 if not specified
5. **Negative step**: Counts backwards, requires start > stop
6. **Integer only**: No float arguments allowed
7. **Memory efficient**: Lazy generation, not stored as list
8. **Empty ranges**: Valid when start >= stop (with positive step)
9. **Common pattern**: `range(1, n+1)` for 1 to n inclusive
10. **Iteration count**: `range(n)` gives exactly n iterations

## Common Mistakes to Avoid

1. **Forgetting exclusive stop**: `range(10)` goes 0-9, not 0-10
2. **Wrong direction**: `range(10, 1)` is empty, need `range(10, 1, -1)`
3. **Off-by-one errors**: For 1-10, use `range(1, 11)` not `range(1, 10)`
4. **Float arguments**: range doesn't accept decimals
5. **Inclusive thinking**: Stop is always exclusive
6. **Missing negative step**: Can't count down without it
7. **Step of 0**: Causes error (infinite loop)

## Quick Reference

```python
# Basic patterns
range(5)           # 0, 1, 2, 3, 4 (5 numbers)
range(1, 6)        # 1, 2, 3, 4, 5
range(0, 10, 2)    # 0, 2, 4, 6, 8 (evens)
range(1, 10, 2)    # 1, 3, 5, 7, 9 (odds)

# Backwards
range(10, 0, -1)   # 10, 9, 8, ..., 1
range(5, -1, -1)   # 5, 4, 3, 2, 1, 0

# Useful formulas
range(n)           # n iterations (0 to n-1)
range(1, n+1)      # 1 to n inclusive
range(len(list))   # All valid indices of list
range(a, b+1)      # a to b inclusive
```
