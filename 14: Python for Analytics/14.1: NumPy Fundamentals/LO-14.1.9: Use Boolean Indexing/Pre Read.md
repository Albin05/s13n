## Pre-Read: Use Boolean Indexing

### What You'll Learn

In this session, you'll master boolean indexing - one of the most powerful features in NumPy for filtering and selecting data based on conditions. This technique eliminates the need for loops when working with conditional data selection.

### Why It Matters

Boolean indexing is essential for:

1. **Data filtering**: Select records meeting specific criteria
2. **Data cleaning**: Remove or fix invalid values
3. **Analysis**: Find patterns, outliers, or trends
4. **Conditional updates**: Modify only elements that match criteria

Real-world examples:
- Find all sales above target
- Filter temperatures below freezing
- Select students who passed
- Identify outliers in datasets

### Key Concepts Preview

**Boolean Indexing:**
- Use comparison operators to create boolean masks
- Filter arrays based on True/False conditions
- Combine multiple conditions logically

**Basic syntax:**
```python
arr = np.array([10, 25, 30, 15, 40])

# Filter values > 20
result = arr[arr > 20]  # [25, 30, 40]

# Combined conditions
result = arr[(arr >= 15) & (arr <= 30)]  # [25, 30, 15]
```

**Logical operators:**
- `&` for AND (both conditions must be True)
- `|` for OR (at least one condition must be True)
- `~` for NOT (inverts condition)

### What to Expect

You'll learn:
1. Creating boolean arrays with comparisons
2. Using boolean masks to filter data
3. Combining multiple conditions
4. Modifying values through boolean indexing
5. Practical applications in data analysis

### Prepare

Make sure you have:
- NumPy installed
- Understanding of comparison operators (`>`, `<`, `==`, etc.)
- Completed previous array indexing lessons

### Quick Example

Try to predict the output:
```python
scores = np.array([85, 92, 67, 78, 95, 88])

# Which students passed (>= 75)?
passed = scores[scores >= 75]  # ?

# Which got A grades (>= 90)?
a_grades = scores[scores >= 90]  # ?

# Which are between 80-90?
range_80_90 = scores[(scores >= 80) & (scores <= 90)]  # ?
```

Answers:
- passed: [85, 92, 78, 95, 88]
- a_grades: [92, 95]
- range_80_90: [85, 88]

Boolean indexing makes data filtering incredibly simple and efficient!
