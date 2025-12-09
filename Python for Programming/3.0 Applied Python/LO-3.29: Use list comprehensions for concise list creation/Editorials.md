# Editorials: Use List Comprehensions

## Problem 1: Square Numbers

```python
# Create list of squares from 1 to 10
squares = [i ** 2 for i in range(1, 11)]
print(squares)
```

### Explanation
This list comprehension iterates through numbers 1 to 10 (inclusive) and squares each number. The expression `i ** 2` is applied to each value of `i` from `range(1, 11)`.

**Time Complexity:** O(n) where n is 10
**Space Complexity:** O(n) for the output list

---

## Problem 2: Extract Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Extract only even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)
```

### Explanation
The list comprehension filters the numbers list by including only those where `n % 2 == 0` (even numbers). The condition `if n % 2 == 0` acts as a filter.

**Time Complexity:** O(n) where n is the length of numbers
**Space Complexity:** O(k) where k is the number of even numbers

---

## Problem 3: Temperature Converter

```python
fahrenheit = [32, 68, 86, 104, 122, 140]

# Convert Fahrenheit to Celsius
celsius = [round((f - 32) * 5/9, 1) for f in fahrenheit]
print(celsius)
```

### Explanation
Each Fahrenheit temperature is converted using the formula `(F - 32) * 5/9`. The `round()` function rounds the result to 1 decimal place. The list comprehension applies this conversion to each temperature in the list.

**Time Complexity:** O(n) where n is the number of temperatures
**Space Complexity:** O(n) for the output list

---

## Problem 4: Word Length Filter

```python
import string

sentence = "The quick brown fox jumps over the lazy dog!"

# Split into words, remove punctuation, lowercase, and filter by length
words = sentence.split()
filtered_words = [word.strip(string.punctuation).lower() for word in words
                  if len(word.strip(string.punctuation)) > 4]
print(filtered_words)
```

### Explanation
1. Split the sentence into words using `split()`
2. For each word, strip punctuation using `strip(string.punctuation)`
3. Convert to lowercase with `.lower()`
4. Filter to include only words with length > 4
5. The condition checks length after stripping punctuation

**Alternative approach:**
```python
import string

sentence = "The quick brown fox jumps over the lazy dog!"
words = sentence.split()
cleaned = [word.strip(string.punctuation).lower() for word in words]
filtered_words = [word for word in cleaned if len(word) > 4]
print(filtered_words)
```

**Time Complexity:** O(n*m) where n is number of words and m is average word length
**Space Complexity:** O(k) where k is the number of filtered words

---

## Problem 5: Matrix Diagonal Sum

```python
# Create 5x5 matrix using nested list comprehension
matrix = [[i + j for j in range(5)] for i in range(5)]

# Print the matrix
for row in matrix:
    print(row)

# Calculate diagonal sum
diagonal_sum = sum(matrix[i][i] for i in range(5))
print(f"Diagonal sum: {diagonal_sum}")
```

### Explanation
1. **Creating the matrix:** The nested list comprehension creates a 5x5 matrix where each element at position (i, j) equals i + j
   - Outer comprehension: `for i in range(5)` - creates rows
   - Inner comprehension: `for j in range(5)` - creates columns
   - Expression: `i + j` - value at each position

2. **Diagonal sum:** Uses a generator expression `matrix[i][i] for i in range(5)` to get diagonal elements and `sum()` to calculate the total
   - Diagonal elements: matrix[0][0], matrix[1][1], matrix[2][2], matrix[3][3], matrix[4][4]
   - Values: 0, 2, 4, 6, 8
   - Sum: 20

**Alternative approach for diagonal sum:**
```python
# Using list comprehension
diagonal_elements = [matrix[i][i] for i in range(5)]
diagonal_sum = sum(diagonal_elements)
print(f"Diagonal sum: {diagonal_sum}")
```

**Time Complexity:** O(n²) for creating the matrix, O(n) for diagonal sum
**Space Complexity:** O(n²) for the matrix

**Matrix visualization:**
```
Position values:
(0,0)=0  (0,1)=1  (0,2)=2  (0,3)=3  (0,4)=4
(1,0)=1  (1,1)=2  (1,2)=3  (1,3)=4  (1,4)=5
(2,0)=2  (2,1)=3  (2,2)=4  (2,3)=5  (2,4)=6
(3,0)=3  (3,1)=4  (3,2)=5  (3,3)=6  (3,4)=7
(4,0)=4  (4,1)=5  (4,2)=6  (4,3)=7  (4,4)=8

Diagonal (marked with *):
0*  1   2   3   4
1   2*  3   4   5
2   3   4*  5   6
3   4   5   6*  7
4   5   6   7   8*
```
