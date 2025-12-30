## Create Random Arrays

### Introduction to Random Arrays

**Why random arrays?**
- Testing algorithms with sample data
- Simulations (Monte Carlo, physics)
- Machine learning (weight initialization, data augmentation)
- Statistics (sampling, hypothesis testing)

**NumPy's random module:**
- `np.random` provides functions for random number generation
- Pseudo-random: determined by seed value
- Various distributions: uniform, normal, etc.

### Generate Random Floats: np.random.rand()

**Purpose:**
Generates random floats in [0, 1) from uniform distribution

**Syntax:**
```python
np.random.rand(d0, d1, d2, ...)
```

**Examples:**
```python
import numpy as np

# Single random number
num = np.random.rand()

# 1D array of 5 numbers
arr1d = np.random.rand(5)

# 2D array: 3×4 matrix
arr2d = np.random.rand(3, 4)
```

**Use cases:**
- Random probabilities
- Initialize weights
- Generate coefficients

### Generate Random Integers: np.random.randint()

**Purpose:**
Generates random integers from specified range

**Syntax:**
```python
np.random.randint(low, high=None, size=None)
```
- **low**: Minimum value (inclusive)
- **high**: Maximum value (exclusive)
- **size**: Shape of output array

**Examples:**
```python
import numpy as np

# Single integer 0-9
num = np.random.randint(10)

# Integer from 5 to 14
num = np.random.randint(5, 15)

# Array of 10 integers from 0-99
arr = np.random.randint(0, 100, size=10)

# 3×3 dice rolls (1-6)
dice = np.random.randint(1, 7, size=(3, 3))
```

**Use cases:**
- Dice rolls, card games
- Random indices
- Test data generation

### Generate from Normal Distribution: np.random.randn()

**Purpose:**
Generates from standard normal distribution (mean=0, std=1)

**Syntax:**
```python
np.random.randn(d0, d1, d2, ...)
```

**Examples:**
```python
import numpy as np

# Single number from normal distribution
num = np.random.randn()

# 1D array
arr = np.random.randn(5)

# 2D array
matrix = np.random.randn(3, 3)
```

**Custom mean and std:**
```python
# Formula: mean + std * randn()
mean = 100
std = 15
scores = mean + std * np.random.randn(1000)
```

**Use cases:**
- Realistic measurements (heights, weights)
- Test scores simulation
- Add Gaussian noise

### Set Random Seed: np.random.seed()

**Purpose:**
Ensures reproducible random numbers

**Usage:**
```python
import numpy as np

# Set seed
np.random.seed(42)
arr1 = np.random.rand(3)

# Reset to same seed
np.random.seed(42)
arr2 = np.random.rand(3)

# arr1 and arr2 are identical
print(np.array_equal(arr1, arr2))  # True
```

**When to use:**
- Testing (consistent results)
- Debugging (reproduce errors)
- Research (reproducible experiments)
- Collaboration (same results for team)

**When NOT to use:**
- Production systems needing true randomness
- Security applications

### Other Useful Functions

**random.choice() - Random sampling:**
```python
colors = np.array(['red', 'blue', 'green'])
sample = np.random.choice(colors, size=2)
```

**random.shuffle() - Shuffle array:**
```python
arr = np.arange(10)
np.random.shuffle(arr)  # Modifies in-place
```

**random.uniform() - Random floats in range:**
```python
arr = np.random.uniform(10, 20, size=5)
```

### Function Comparison

| Function | Purpose | Range/Distribution |
|----------|---------|-------------------|
| `rand()` | Random floats | [0, 1) uniform |
| `randint()` | Random integers | [low, high) |
| `randn()` | Normal distribution | mean=0, std=1 |
| `uniform()` | Floats in range | [low, high) |

### Key Takeaways

1. **rand(d0, d1, ...)**: Random floats [0, 1) from uniform distribution
2. **randint(low, high, size)**: Random integers in [low, high)
3. **randn(d0, d1, ...)**: Standard normal distribution (mean=0, std=1)
4. **seed(value)**: Set seed for reproducible results
5. **choice()**, **shuffle()**, **uniform()**: Specialized random operations
6. Use seeds for testing/debugging, avoid for production randomness
7. Transform randn() with formula: mean + std × randn()
