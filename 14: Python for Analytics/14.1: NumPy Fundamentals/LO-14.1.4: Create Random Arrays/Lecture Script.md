### Create Random Arrays

### Hook (2 minutes)

"Imagine you're testing a machine learning algorithm and need 10,000 sample data points, or running a Monte Carlo simulation with millions of random trials. Generating random data is essential for testing, simulation, and machine learning. NumPy provides powerful random number generators that can create arrays of random values instantly. Let's learn how to harness randomness for data science!"

### Section 1: Introduction to Random Arrays (3 minutes)

**Why do we need random arrays?**

Random arrays are crucial for:
- **Testing algorithms**: Generate sample data for unit tests
- **Simulations**: Monte Carlo methods, physics simulations
- **Machine Learning**: Initialize weights, create training data, data augmentation
- **Statistics**: Sampling, bootstrapping, hypothesis testing
- **Game Development**: Generate random events, procedural content

**NumPy's random module:**

NumPy provides `np.random` module with functions to generate random numbers:
- Uniform distribution (all values equally likely)
- Normal/Gaussian distribution (bell curve)
- Integer ranges
- Custom distributions

**Important note:**
- Random numbers are actually "pseudo-random" (determined by a seed)
- Setting a seed ensures reproducibility

### Section 2: Generate Random Floats with np.random.rand() (3 minutes)

**What is rand()?**

`np.random.rand()` generates random floats in the range [0, 1) from a uniform distribution.

**Syntax:**
```python
np.random.rand(d0, d1, d2, ...)
```
- Parameters are dimensions (not a tuple)

**Examples:**

```python
import numpy as np

# Single random number
num = np.random.rand()
print(num)  # e.g., 0.5488135039273248

# 1D array of 5 random numbers
arr1d = np.random.rand(5)
print(arr1d)  # e.g., [0.71518937 0.60276338 0.54488318 0.4236548  0.64589411]

# 2D array: 3 rows, 4 columns
arr2d = np.random.rand(3, 4)
print(arr2d)
# [[0.43758721 0.891773   0.96366276 0.38344152]
#  [0.79172504 0.52889492 0.56804456 0.92559664]
#  [0.07103606 0.0871293  0.0202184  0.83261985]]

# 3D array
arr3d = np.random.rand(2, 3, 2)
print(arr3d.shape)  # (2, 3, 2)
```

**Use cases:**
- Generate random probabilities
- Initialize neural network weights (scaled to appropriate range)
- Create random coefficients

### Section 3: Generate Random Integers with np.random.randint() (3 minutes)

**What is randint()?**

`np.random.randint()` generates random integers from a specified range.

**Syntax:**
```python
np.random.randint(low, high=None, size=None)
```
- **low**: Lowest integer (inclusive)
- **high**: Highest integer (exclusive)
- **size**: Output shape (tuple or int)

**Examples:**

```python
import numpy as np

# Single random integer from 0 to 9
num = np.random.randint(10)
print(num)  # e.g., 7

# Single integer from 5 to 15 (15 exclusive)
num = np.random.randint(5, 15)
print(num)  # e.g., 12

# 1D array of 10 integers from 0 to 99
arr = np.random.randint(0, 100, size=10)
print(arr)  # e.g., [44 47 64 67 67  9 83 21 36 87]

# 2D array: 3x3 matrix of integers from 1 to 6 (dice rolls)
dice = np.random.randint(1, 7, size=(3, 3))
print(dice)
# [[6 1 4]
#  [4 8 4]
#  [6 3 5]]
```

**Use cases:**
- Simulate dice rolls, card draws
- Generate random indices for sampling
- Create test data with integer values

### Section 4: Generate Random Numbers from Normal Distribution (4 minutes)

**What is randn()?**

`np.random.randn()` generates random numbers from a **standard normal distribution** (mean=0, std=1).

**Syntax:**
```python
np.random.randn(d0, d1, d2, ...)
```

**Examples:**

```python
import numpy as np

# Single random number from normal distribution
num = np.random.randn()
print(num)  # e.g., 0.12453567 (can be negative)

# 1D array
arr = np.random.randn(5)
print(arr)  # e.g., [ 0.12697  1.08608 -1.96063  0.79064  0.75697]

# 2D array
matrix = np.random.randn(3, 3)
print(matrix)
# [[ 0.63364  -0.90675   1.42789]
#  [-2.15181   0.37292   1.52574]
#  [-1.12927   0.04513   0.57043]]
```

**Custom mean and standard deviation:**

```python
# General formula: mean + std * randn()
mean = 100
std = 15
scores = mean + std * np.random.randn(1000)
print(f"Mean: {scores.mean():.2f}")  # ~100
print(f"Std: {scores.std():.2f}")    # ~15
```

**Use cases:**
- Generate realistic measurements with natural variation
- Simulate test scores, heights, weights (normally distributed data)
- Add Gaussian noise to data

### Section 5: Set Random Seed for Reproducibility (3 minutes)

**Why set a seed?**

Random number generators are "pseudo-random" - they follow a deterministic algorithm starting from a seed value. Setting the seed ensures you get the same random numbers every time.

**Setting the seed:**

```python
import numpy as np

# Set seed
np.random.seed(42)

# Generate random numbers
arr1 = np.random.rand(3)
print(arr1)  # [0.37454012 0.95071431 0.73199394]

# Reset seed to same value
np.random.seed(42)

# Get same random numbers again
arr2 = np.random.rand(3)
print(arr2)  # [0.37454012 0.95071431 0.73199394]

print(np.array_equal(arr1, arr2))  # True
```

**When to use seeds:**
- **Testing**: Ensure tests produce same results every time
- **Debugging**: Reproduce bugs involving random data
- **Research**: Make experiments reproducible
- **Collaboration**: Team members get identical results

**When NOT to use seeds:**
- Production systems requiring true randomness
- Security applications (use `secrets` module instead)

### Section 6: Other Useful Random Functions (2 minutes)

**random.choice() - Random Sampling:**

```python
# Random selection from array
colors = np.array(['red', 'blue', 'green', 'yellow'])
sample = np.random.choice(colors, size=3)
print(sample)  # e.g., ['green' 'red' 'blue']
```

**random.shuffle() - Shuffle Array:**

```python
# Shuffle array in-place
arr = np.arange(10)
np.random.shuffle(arr)
print(arr)  # e.g., [2 8 4 9 1 6 7 3 0 5]
```

**random.uniform() - Random Floats in Range:**

```python
# Random floats between 10 and 20
arr = np.random.uniform(10, 20, size=5)
print(arr)  # e.g., [15.73 11.28 19.45 12.67 18.92]
```

### Summary (1 minute)

**Key Takeaways:**

1. **np.random.rand(d0, d1, ...)**: Random floats [0, 1) from uniform distribution
2. **np.random.randint(low, high, size)**: Random integers in range [low, high)
3. **np.random.randn(d0, d1, ...)**: Random numbers from standard normal distribution (mean=0, std=1)
4. **np.random.seed(value)**: Set seed for reproducible random numbers
5. **Other functions**: choice(), shuffle(), uniform() for specialized needs

**Remember:**
- Use `rand()` for probabilities and weights between 0 and 1
- Use `randint()` for discrete random values
- Use `randn()` for normally distributed data
- Always set seed when reproducibility matters (testing, debugging, research)

**Next Steps:**
In the next lesson, we'll learn how to create identity and diagonal matrices - essential for linear algebra and matrix operations!
