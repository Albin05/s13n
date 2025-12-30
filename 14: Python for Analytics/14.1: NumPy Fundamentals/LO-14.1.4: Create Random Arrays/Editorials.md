## Editorials: Create Random Arrays

### Q1 Solution: Generate Random Float Array

```python
import numpy as np

# Set seed for reproducibility
np.random.seed(10)

# Generate 8 random floats
arr = np.random.rand(8)
print(arr)
```

**Explanation:**
- `np.random.seed(10)` ensures same random numbers every time
- `np.random.rand(8)` generates 8 random floats in [0, 1)
- Without seed, you'd get different numbers each run

---

### Q2 Solution: Generate Random Integer Array

```python
import numpy as np

# Set seed
np.random.seed(42)

# Simulate 20 dice rolls (1 to 6)
dice_rolls = np.random.randint(1, 7, size=20)
print(f"Dice rolls: {dice_rolls}")

# Count occurrences of 6
count_sixes = np.sum(dice_rolls == 6)
print(f"Number of 6s: {count_sixes}")
```

**Explanation:**
- `np.random.randint(1, 7, size=20)` generates 20 integers from 1 to 6 (7 is exclusive)
- `dice_rolls == 6` creates boolean array: [False, True, False, ...]
- `np.sum()` counts True values (True=1, False=0)

**Alternative counting method:**
```python
count_sixes = (dice_rolls == 6).sum()
# or
count_sixes = len(dice_rolls[dice_rolls == 6])
```

---

### Q3 Solution: Create 2D Random Array

```python
import numpy as np

# Set seed
np.random.seed(1)

# Create 5x5 matrix
matrix = np.random.rand(5, 5)

# Print matrix
print("Matrix:")
print(matrix)

# Find maximum and minimum
max_val = matrix.max()
min_val = matrix.min()

print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")
```

**Explanation:**
- `np.random.rand(5, 5)` creates 5×5 matrix (dimensions as separate args)
- `.max()` finds largest value in entire array
- `.min()` finds smallest value in entire array

**Alternative methods:**
```python
max_val = np.max(matrix)
min_val = np.min(matrix)
```

---

### Q4 Solution: Simulate Test Scores

```python
import numpy as np

# Set seed
np.random.seed(5)

# Generate scores: mean + std * randn()
mean = 75
std = 10
scores = mean + std * np.random.randn(100)

# Calculate statistics
mean_score = scores.mean()
std_score = scores.std()
above_85 = np.sum(scores > 85)

# Print results
print(f"Mean score: {mean_score:.2f}")
print(f"Standard deviation: {std_score:.2f}")
print(f"Scores above 85: {above_85}")
```

**Explanation:**
- `np.random.randn(100)` generates 100 values from standard normal (mean=0, std=1)
- Formula `mean + std * randn()` transforms to custom mean and std
- `.mean()` calculates average of scores
- `.std()` calculates standard deviation
- `scores > 85` creates boolean array, `np.sum()` counts True values

**Why the formula works:**
- randn() gives mean=0, std=1
- Multiply by std: mean=0, std=10
- Add mean: mean=75, std=10

---

### Q5 Solution: Random Sampling and Shuffling

```python
import numpy as np

# Student list
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve',
            'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']

# Set seed
np.random.seed(20)

# Random selection (without replacement)
selected = np.random.choice(students, size=3, replace=False)
print(f"Selected students: {selected}")

# Create array and shuffle
students_arr = np.array(students)
np.random.shuffle(students_arr)
print(f"Shuffled students: {students_arr}")
```

**Explanation:**
- `np.random.choice(students, size=3, replace=False)`:
  - `students`: source array to sample from
  - `size=3`: number of samples to draw
  - `replace=False`: no repeats (each student can be selected once)
- `np.random.shuffle()` shuffles array **in-place** (modifies original)
- Seed ensures reproducibility

**Important notes:**
- `shuffle()` modifies the array directly (returns None)
- For a copy, use: `shuffled = np.random.permutation(students_arr)`
- With `replace=True`, same element can be selected multiple times

**Key Concepts Covered:**
1. Using seeds for reproducible random generation
2. Generating random floats with rand()
3. Generating random integers with randint()
4. Creating normally distributed data with custom mean/std
5. Random sampling with choice() and shuffling arrays
6. Using boolean arrays for counting and filtering
