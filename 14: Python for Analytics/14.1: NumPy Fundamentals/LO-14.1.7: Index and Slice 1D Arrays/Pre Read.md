## Pre-Read: Index and Slice 1D Arrays

### What You'll Learn

In this session, you'll master array indexing and slicing - the fundamental operations for accessing and extracting data from NumPy arrays. These skills are essential for data manipulation and analysis.

### Why It Matters

Indexing and slicing are among the most frequently used operations in data analysis. You'll need them to:

1. **Extract specific elements**: Get individual values or ranges of data
2. **Analyze subsets**: Work with portions of large datasets efficiently
3. **Transform data**: Reverse, sample, or reorganize array elements
4. **Time-series analysis**: Extract specific time periods from data

### Key Concepts Preview

**Indexing:**
- Access single elements using `arr[index]`
- Positive indices start from 0
- Negative indices count from the end (-1 is last)

**Slicing:**
- Extract portions using `arr[start:stop:step]`
- start: where to begin (inclusive)
- stop: where to end (exclusive)
- step: increment between elements

**Examples:**
```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]      # 10 (first element)
arr[-1]     # 50 (last element)
arr[1:4]    # [20 30 40] (indices 1, 2, 3)
arr[::-1]   # [50 40 30 20 10] (reversed)
```

### What to Expect

You'll learn:
1. Basic indexing with positive and negative indices
2. Slicing syntax and patterns
3. Using the step parameter for advanced extraction
4. Common slicing patterns (first n, last n, reverse, etc.)
5. Important differences from Python lists

### Prepare

Make sure you have:
- NumPy installed (`pip install numpy`)
- Basic familiarity with NumPy arrays
- Understanding of Python list indexing (helpful but not required)

### Quick Exercise

Try to predict what these operations return:
```python
arr = np.array([5, 10, 15, 20, 25, 30])

arr[2]      # ?
arr[-2]     # ?
arr[1:4]    # ?
arr[::2]    # ?
arr[::-1]   # ?
```

Answers: 15, 25, [10 15 20], [5 15 25], [30 25 20 15 10 5]

Understanding these patterns will make working with data much more efficient!
