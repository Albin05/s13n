## Pre-Read: Save and Load Arrays

### What You'll Learn

In this session, you'll master saving and loading NumPy arrays - essential skills for persisting work, sharing data, building pipelines, and preventing data loss.

### Why It Matters

File I/O is crucial for:

1. **Persistence**: Save work between sessions
2. **Collaboration**: Share data with team members
3. **Pipelines**: Build reproducible workflows
4. **Checkpointing**: Save progress in long computations
5. **Archiving**: Store experiment results

Real-world examples:
- Saving trained model weights
- Checkpointing during 12-hour training runs
- Sharing preprocessed datasets (avoiding recomputation)
- Archiving experiment results for later analysis
- Building data processing pipelines

### Key Concepts Preview

**Binary Format (.npy/.npz):**
- Fast and efficient
- Preserves exact data
- NumPy native format

**Text Format (.txt/.csv):**
- Human-readable
- Share with other tools
- Slower but compatible

**Compression:**
- Reduce file size 3-4x
- Minimal performance impact
- Essential for storage

**Basic examples:**
```python
import numpy as np

# Save single array
data = np.array([1, 2, 3, 4, 5])
np.save('data.npy', data)

# Load it back
loaded = np.load('data.npy')
# Perfect copy!

# Save multiple arrays
np.savez_compressed('dataset.npz',
                    X=X_train,
                    y=y_train)

# Load multiple
with np.load('dataset.npz') as data:
    X = data['X']
    y = data['y']
```

### What to Expect

You'll learn:
1. Save/load single arrays with .npy
2. Save/load multiple arrays with .npz
3. Use compression to save space
4. Work with text files (.txt, .csv)
5. Handle missing data
6. Build data pipelines
7. Implement checkpointing

### Prepare

Make sure you have:
- NumPy installed
- Understanding of arrays
- Basic file system knowledge
- Familiarity with file paths

### Quick Examples

**Binary Save/Load:**
```python
import numpy as np

# Create and save
scores = np.array([[85, 90, 78],
                   [92, 88, 95]])

np.save('scores.npy', scores)

# Load
loaded = np.load('scores.npy')
print(loaded)
# [[85 90 78]
#  [92 88 95]]

# Exact match!
print(np.array_equal(scores, loaded))  # True
```

**Multiple Arrays:**
```python
# Training data
X_train = np.array([[1, 2], [3, 4]])
y_train = np.array([0, 1])
X_test = np.array([[5, 6]])
y_test = np.array([1])

# Save all together
np.savez_compressed('data.npz',
                    X_train=X_train,
                    y_train=y_train,
                    X_test=X_test,
                    y_test=y_test)

# Load
data = np.load('data.npz')
print(data.files)
# ['X_train', 'y_train', 'X_test', 'y_test']

X_train = data['X_train']
y_train = data['y_train']
```

**Text Files:**
```python
# Save as CSV
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

np.savetxt('data.csv', arr, delimiter=',')

# Creates:
# 1.0,2.0,3.0
# 4.0,5.0,6.0

# Load
loaded = np.loadtxt('data.csv', delimiter=',')
```

### File Formats

**Binary (.npy):**
```python
np.save('data.npy', arr)
arr = np.load('data.npy')
```
- ✓ Fast
- ✓ Exact precision
- ✓ Preserves dtype
- ✗ Not human-readable

**Compressed (.npz):**
```python
np.savez_compressed('data.npz', X=X, y=y)
data = np.load('data.npz')
X = data['X']
```
- ✓ Multiple arrays
- ✓ 3-4x smaller
- ✓ Fast
- ✗ Slight save overhead

**Text (.csv):**
```python
np.savetxt('data.csv', arr, delimiter=',')
arr = np.loadtxt('data.csv', delimiter=',')
```
- ✓ Human-readable
- ✓ Excel-compatible
- ✗ Slower
- ✗ Less precise

### Compression Benefits

```python
# Large dataset
X = np.random.rand(10000, 100)

# Uncompressed
np.savez('data.npz', X=X)
# File size: ~7.6 MB

# Compressed
np.savez_compressed('data_compressed.npz', X=X)
# File size: ~2.4 MB

# 3.2x smaller!
# Saves disk space and network transfer time
```

### Try to Predict

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Save and load
np.save('test.npy', arr)
loaded = np.load('test.npy')

# Will this be True or False?
result = np.array_equal(arr, loaded)  # ?

# What about this?
arr2 = np.array([1.1, 2.2, 3.3])
np.savetxt('test.txt', arr2)
loaded2 = np.loadtxt('test.txt')
result2 = np.array_equal(arr2, loaded2)  # ?
```

Answers:
- result: True (binary preserves exactly)
- result2: Probably True, but subject to floating-point precision in text format

### Common Patterns

**Checkpoint System:**
```python
# During training
for epoch in range(100):
    train()
    
    if epoch % 10 == 0:
        np.savez_compressed(
            f'checkpoint_{epoch}.npz',
            weights=model_weights,
            epoch=epoch,
            loss=loss_history
        )
```

**Data Pipeline:**
```python
# Stage 1: Load raw
raw = load_raw_data()
np.save('01_raw.npy', raw)

# Stage 2: Preprocess
raw = np.load('01_raw.npy')
processed = preprocess(raw)
np.save('02_processed.npy', processed)

# Stage 3: Split
data = np.load('02_processed.npy')
train, test = split(data)
np.savez_compressed('03_final.npz',
                    train=train,
                    test=test)
```

**Always Verify:**
```python
# Save important data
np.save('critical.npy', important_array)

# Immediately verify
loaded = np.load('critical.npy')
assert np.array_equal(important_array, loaded)
print("Save verified successfully!")
```

### Best Practices

1. **Use compression:** `savez_compressed` not `savez`
2. **Use context managers:** `with np.load(...) as data:`
3. **Add metadata:** Save version, date, description
4. **Verify saves:** Load immediately to check
5. **Clean up:** Remove temporary files

Proper file I/O prevents lost work and enables collaboration!
