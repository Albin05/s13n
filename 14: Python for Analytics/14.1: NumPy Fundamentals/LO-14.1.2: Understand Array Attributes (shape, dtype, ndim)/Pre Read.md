## Pre-Read: Understand Array Attributes (shape, dtype, ndim)

### What You'll Learn

In this lesson, you'll learn how to inspect and understand NumPy array properties using key attributes like shape, dtype, and ndim.

### Prerequisites

Before starting this lesson, make sure you have:
- Completed LO-14.1.1: Install NumPy and Create Arrays
- Understanding of how to create NumPy arrays
- Familiarity with basic Python data types
- Python 3.x and NumPy installed

### Why Array Attributes Matter

**Real-world scenario:**

Imagine you're working with image data. An RGB image might be stored as a 3D array with shape (height, width, 3), where:
- First dimension = image height (rows)
- Second dimension = image width (columns)
- Third dimension = color channels (R, G, B)

Without understanding array attributes, you could:
- Apply operations to wrong dimensions
- Waste memory by using unnecessarily large data types
- Encounter dimension mismatch errors

**Benefits of understanding attributes:**
1. **Debug faster**: Identify shape mismatches before operations fail
2. **Optimize memory**: Choose appropriate data types for your data range
3. **Write robust code**: Validate array structure programmatically
4. **Performance**: Understand memory layout for efficient computations

### Key Concepts to Understand

**1. Array Shape**

The shape describes the size of each dimension:
- 1D array: `(n,)` where n is the number of elements
- 2D array: `(rows, columns)`
- 3D array: `(depth, rows, columns)`

Think of shape as answering: "How is this data organized?"

**2. Data Type (dtype)**

The dtype determines:
- How much memory each element uses
- What values can be stored
- How operations are performed

Common dtypes:
- **int32**: Integers from -2,147,483,648 to 2,147,483,647 (4 bytes)
- **int64**: Larger integers (8 bytes)
- **float32**: Decimal numbers with ~7 decimal digits precision (4 bytes)
- **float64**: Decimal numbers with ~15 decimal digits precision (8 bytes)
- **bool**: True/False values (1 byte)

**3. Number of Dimensions (ndim)**

The ndim tells you the dimensionality:
- **1D (vector)**: A list of values (e.g., temperature readings over time)
- **2D (matrix)**: A table of values (e.g., student scores by subject)
- **3D**: Volume data (e.g., video frames, medical scans)

### What to Expect

In this lesson, you will learn about:

1. **shape attribute**: Understanding and extracting array dimensions
2. **dtype attribute**: Identifying and working with data types
3. **ndim attribute**: Determining the number of dimensions
4. **size attribute**: Calculating total number of elements
5. **itemsize and nbytes**: Understanding memory consumption

### Preparation Tasks

Before the lesson:
1. Review how to create 1D, 2D, and 3D arrays
2. Understand the difference between tuples and lists
3. Refresh your knowledge of basic data types (int, float, bool)
4. Have NumPy installed and ready to use

### Questions to Think About

As you prepare for this lesson, consider:
1. Why might knowing the shape of an array prevent errors?
2. When would you choose int32 over int64?
3. How could you verify if two arrays have compatible shapes for multiplication?
4. What's the relationship between ndim and the length of the shape tuple?

### Visual Example

Consider a 2D array representing student test scores:

```
Array: [[85, 90, 78],
        [92, 88, 95]]

shape: (2, 3)     → 2 students, 3 test scores each
ndim: 2           → 2-dimensional (matrix)
dtype: int64      → Integer data type
size: 6           → Total of 6 values
```

Understanding these attributes helps you:
- Know you have 2 students and 3 tests
- Confirm the data is stored as integers
- Calculate statistics correctly across the right dimension

### Resources

If you want to read ahead:
- NumPy Array Attributes: https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-attributes
- Data Types in NumPy: https://numpy.org/doc/stable/user/basics.types.html

### Coming Up Next

After mastering array attributes, you'll learn:
- Creating arrays with specialized functions (zeros, ones, arange, linspace)
- Generating random arrays for testing and simulation
- Creating identity and diagonal matrices for linear algebra
- Reshaping arrays to change their dimensions

Understanding attributes is foundational - they'll be essential in every NumPy operation you perform!
