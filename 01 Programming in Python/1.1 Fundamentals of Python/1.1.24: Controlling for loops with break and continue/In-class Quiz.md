# Post-class Quiz: Controlling For Loops with Break and Continue

## Question 1

What will be the output of this code?

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

A) 0 1 2 3
B) 0 1 2
C) 0 1 2 3 4
D) 1 2 3

**Answer: B) 0 1 2**

**Explanation:** The loop prints values 0, 1, and 2. When i becomes 3, the if condition is True and break executes, immediately exiting the loop. The number 3 is never printed because break occurs before the print statement for that iteration.

---

## Question 2

What does the continue statement do in a for loop?

A) Stops the entire program
B) Exits the loop completely
C) Skips the rest of the current iteration and moves to the next one
D) Restarts the loop from the beginning

**Answer: C) Skips the rest of the current iteration and moves to the next one**

**Explanation:** The continue statement causes the loop to skip all remaining code in the current iteration and immediately proceed to the next iteration. It does NOT exit the loop entirely (that's what break does).

---

## Question 3

What will this code print?

```python
for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(num, end=' ')
```

A) 1 2 3 4 5
B) 2 4
C) 1 3 5
D) 1 2 3 4

**Answer: C) 1 3 5**

**Explanation:** The loop iterates from 1 to 5. When num is even (2 or 4), continue skips the print statement. Only odd numbers (1, 3, 5) are printed.

---

## Question 4

What is the output of this code?

```python
for i in range(3):
    if i == 5:
        break
    print(i)
```

A) 0 1 2
B) Nothing
C) 0 1 2 3 4
D) Error

**Answer: A) 0 1 2**

**Explanation:** The range(3) produces values 0, 1, 2. The condition `i == 5` is never True since i never reaches 5. Therefore, break never executes and all three values are printed normally.

---

## Question 5

When does the else clause of a for loop execute?

A) Always after the loop
B) Only if the loop encounters a break statement
C) Only if the loop completes without encountering a break
D) Never

**Answer: C) Only if the loop completes without encountering a break**

**Explanation:** The for-else clause is a special Python feature where the else block executes only when the loop completes its normal iteration without encountering a break statement. If break executes, the else block is skipped.

---

## Question 6

What will be the output?

```python
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i, end=' ')
```

A) 0 1 3
B) 0 1 2 3
C) 0 1 3 4
D) 0 1 2 3 4

**Answer: A) 0 1 3**

**Explanation:**
- i=0: No conditions met, print 0
- i=1: No conditions met, print 1
- i=2: First if is True, continue skips print
- i=3: No conditions met, print 3
- i=4: Second if is True, break exits loop
Result: 0 1 3

---

## Question 7

Which statement is TRUE about break in nested loops?

A) Break exits all nested loops
B) Break exits only the innermost loop containing it
C) Break exits the outermost loop
D) Break is not allowed in nested loops

**Answer: B) Break exits only the innermost loop containing it**

**Explanation:** In nested loops, a break statement only exits the loop it's directly inside of (the innermost one). To break out of outer loops, you need additional logic like flag variables or function returns.

---

## Question 8

What will this code output?

```python
numbers = [1, 2, 3, 4]
for num in numbers:
    if num == 5:
        print("Found")
        break
else:
    print("Not found")
```

A) Found
B) Not found
C) Nothing
D) Error

**Answer: B) Not found**

**Explanation:** The number 5 is not in the list, so the break never executes. The loop completes normally, and therefore the else clause executes, printing "Not found". This is a common pattern for search operations with for-else.

---

## Question 9

What is the main difference between break and continue?

A) There is no difference
B) break exits the loop, continue skips to the next iteration
C) break skips to the next iteration, continue exits the loop
D) break can only be used in while loops

**Answer: B) break exits the loop, continue skips to the next iteration**

**Explanation:** break completely terminates the loop and continues execution after the loop. continue skips the remaining code in the current iteration but continues with the next iteration of the loop.

---

## Question 10

What will be printed?

```python
for i in range(1, 4):
    for j in range(1, 3):
        if j == 2:
            break
        print(f"{i},{j}", end=' ')
```

A) 1,1 2,1 3,1
B) 1,1 1,2 2,1 2,2 3,1 3,2
C) 1,1 2,1
D) 1,1

**Answer: A) 1,1 2,1 3,1**

**Explanation:** The outer loop runs for i=1,2,3. The inner loop starts with j=1 (print i,j), then j=2 triggers break, exiting the inner loop. This pattern repeats for each i value. Result: 1,1  2,1  3,1

---

## Question 11

How many times will "Hello" be printed?

```python
for i in range(10):
    if i % 3 == 0:
        continue
    if i > 5:
        break
    print("Hello")
```

A) 3 times
B) 4 times
C) 5 times
D) 6 times

**Answer: A) 3 times**

**Explanation:**
- i=0: divisible by 3, continue (skip)
- i=1: print "Hello"
- i=2: print "Hello"
- i=3: divisible by 3, continue (skip)
- i=4: print "Hello"
- i=5: print "Hello" (5 is NOT > 5)
- i=6: 6 > 5, break
Total printed: 1, 2, 4, 5 = 4 times

Wait, let me recount:
- i=0: 0 % 3 == 0, continue
- i=1: 1 % 3 != 0, 1 > 5? No, print "Hello"
- i=2: 2 % 3 != 0, 2 > 5? No, print "Hello"
- i=3: 3 % 3 == 0, continue
- i=4: 4 % 3 != 0, 4 > 5? No, print "Hello"
- i=5: 5 % 3 != 0, 5 > 5? No, print "Hello"
- i=6: 6 % 3 == 0, continue
- i=7: 7 % 3 != 0, 7 > 5? Yes, break

Wait, that's still 4 times (1, 2, 4, 5).

Let me recalculate:
- i=0: 0 % 3 == 0 → continue
- i=1: 1 % 3 = 1 (not 0) → 1 > 5? No → print
- i=2: 2 % 3 = 2 (not 0) → 2 > 5? No → print
- i=3: 3 % 3 == 0 → continue
- i=4: 4 % 3 = 1 (not 0) → 4 > 5? No → print
- i=5: 5 % 3 = 2 (not 0) → 5 > 5? No → print
- i=6: 6 % 3 == 0 → continue
- i=7: 7 % 3 = 1 (not 0) → 7 > 5? Yes → break

So it prints at i = 1, 2, 4, 5 = 4 times

Actually, I need to change the answer. Let me update it.

Actually, the order matters! Let me trace again carefully:
```python
for i in range(10):  # i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    if i % 3 == 0:   # Check if divisible by 3
        continue
    if i > 5:        # Check if greater than 5
        break
    print("Hello")
```

- i=0: 0%3==0 True → continue (skip rest)
- i=1: 1%3==0 False → 1>5 False → print "Hello"
- i=2: 2%3==0 False → 2>5 False → print "Hello"
- i=3: 3%3==0 True → continue (skip rest)
- i=4: 4%3==0 False → 4>5 False → print "Hello"
- i=5: 5%3==0 False → 5>5 False → print "Hello"
- i=6: 6%3==0 True → continue (skip rest)
- i=7: 7%3==0 False → 7>5 True → break

Printed at: i=1, 2, 4, 5 = 4 times

So the answer should be B) 4 times. Let me fix this.

**Answer: B) 4 times**

**Explanation:**
- i=0: 0 % 3 == 0, continue (skip)
- i=1: Not divisible by 3, 1 ≤ 5, print "Hello"
- i=2: Not divisible by 3, 2 ≤ 5, print "Hello"
- i=3: 3 % 3 == 0, continue (skip)
- i=4: Not divisible by 3, 4 ≤ 5, print "Hello"
- i=5: Not divisible by 3, 5 ≤ 5, print "Hello"
- i=6: 6 % 3 == 0, continue (skip)
- i=7: Not divisible by 3, but 7 > 5, break
Total: 4 times (at i=1, 2, 4, 5)

---

## Question 12

What makes for-else useful?

A) It always executes after a for loop
B) It provides a clean way to handle "not found" scenarios in searches
C) It executes only when break is encountered
D) It makes loops run faster

**Answer: B) It provides a clean way to handle "not found" scenarios in searches**

**Explanation:** The for-else clause is particularly useful for search operations. If the item is found, you break (and else doesn't execute). If the loop completes without finding the item, the else clause can handle that "not found" case cleanly without needing extra flag variables.

---

## Question 13

Can you use both break and continue in the same loop?

A) No, Python will raise an error
B) Yes, but only in while loops
C) Yes, they can be used together in the same loop
D) No, you must choose one or the other

**Answer: C) Yes, they can be used together in the same loop**

**Explanation:** You can use both break and continue in the same loop. They serve different purposes: continue skips to the next iteration, while break exits the loop. However, only one of them will execute in any given iteration. Order matters when checking conditions.

---

## Question 14

What will this code output?

```python
text = "Python"
for char in text:
    if char == 'o':
        break
    if char in 'aeiou':
        continue
    print(char, end='')
```

A) Pythn
B) Pyth
C) Pyt
D) Python

**Answer: B) Pyth**

**Explanation:**
- 'P': Not a vowel, print 'P'
- 'y': Not a vowel, print 'y'
- 't': Not a vowel, print 't'
- 'h': Not a vowel, print 'h'
- 'o': Equals 'o', break (exit loop)
- 'n': Never reached
Result: "Pyth"

---

## Question 15

Which scenario is break MOST useful for?

A) Processing all items in a list
B) Filtering out unwanted values
C) Stopping when a target is found or condition is met
D) Counting items in a collection

**Answer: C) Stopping when a target is found or condition is met**

**Explanation:** Break is most useful for early exit scenarios, such as:
- Searching for an item and stopping when found
- Stopping when a threshold is reached
- Exiting when an error condition occurs
- Stopping when a goal is achieved

For filtering, continue is more appropriate. For processing all items, no control flow modification is needed.

---

## Summary

### Key Concepts Tested:

1. **Break Statement**: Exits loop immediately when executed
2. **Continue Statement**: Skips remaining code in current iteration, moves to next
3. **For-Else Clause**: Executes only if loop completes without break
4. **Nested Loops**: Break/continue only affect innermost loop
5. **Combined Usage**: Both can be used in same loop with different conditions
6. **Use Cases**:
   - Break: Search, early exit, threshold detection
   - Continue: Filtering, skipping invalid data
   - For-else: Search completion detection

### Common Patterns:

```python
# Search pattern with break
for item in items:
    if item == target:
        print("Found!")
        break

# Filter pattern with continue
for num in numbers:
    if num < 0:
        continue
    process(num)

# For-else pattern
for item in items:
    if item == target:
        break
else:
    print("Not found")

# Combined usage
for num in range(100):
    if num % 5 == 0:
        continue  # Skip multiples of 5
    if num > 50:
        break  # Stop after 50
    print(num)
```

### Best Practices:

1. **Use break** when you need to stop processing early
2. **Use continue** when you need to skip certain items
3. **Use for-else** instead of flag variables when possible
4. **Order matters** when combining break and continue
5. **Comment your intent** to make code clear
6. **Consider readability** - sometimes restructuring is better than complex break/continue logic
