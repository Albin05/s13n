## Save and Load Arrays

### Hook (2 minutes)

**Scenario:**
You've spent hours processing a large dataset, creating computed features, and training a model. Your computer crashes. Do you lose all your work?

Or you're collaborating with a team member who needs your preprocessed data. How do you share a 1GB NumPy array efficiently?

Maybe you're running experiments and need to save intermediate results to analyze later.

Saving and loading arrays is fundamental for:
- Persisting work between sessions
- Sharing data with collaborators
- Creating data pipelines
- Checkpointing long computations
- Archiving results

**What You'll Learn:**
1. Save and load arrays in binary format (.npy, .npz)
2. Work with text files (.txt, .csv)
3. Handle multiple arrays efficiently
4. Compress arrays to save space
5. Load data from various sources
6. Choose the right format for your needs

---

### Section 1: Binary Format - .npy Files (4 minutes)

**Saving Single Array:**

```python
import numpy as np

# Create array
data = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

# Save to binary file
np.save('data.npy', data)
print("Array saved to data.npy")
```

**Loading .npy File:**

```python
# Load array
loaded = np.load('data.npy')
print("Loaded array:")
print(loaded)

# Verify it matches original
print(f"\nArrays equal: {np.array_equal(data, loaded)}")
```

**Advantages of .npy:**

```python
# Preserves dtype exactly
floats = np.array([1.5, 2.7, 3.9], dtype=np.float32)
np.save('floats.npy', floats)
loaded_floats = np.load('floats.npy')

print(f"Original dtype: {floats.dtype}")
print(f"Loaded dtype: {loaded_floats.dtype}")
# Both: float32 - preserved exactly!

# Fast for large arrays
large_array = np.random.rand(1000, 1000)

import time
start = time.time()
np.save('large.npy', large_array)
save_time = time.time() - start

start = time.time()
loaded_large = np.load('large.npy')
load_time = time.time() - start

print(f"\nSave time: {save_time:.4f}s")
print(f"Load time: {load_time:.4f}s")
```

**When to Use .npy:**
- Single array to save/load
- Need to preserve exact dtype
- Want fastest read/write
- Working with large arrays
- NumPy-to-NumPy workflow

---

### Section 2: Multiple Arrays - .npz Files (4 minutes)

**Saving Multiple Arrays (Uncompressed):**

```python
import numpy as np

# Multiple arrays
features = np.array([[1, 2], [3, 4], [5, 6]])
labels = np.array([0, 1, 0])
metadata = np.array(['train', 'test', 'train'])

# Save multiple arrays
np.savez('dataset.npz', 
         features=features,
         labels=labels,
         metadata=metadata)

print("Multiple arrays saved to dataset.npz")
```

**Loading .npz File:**

```python
# Load npz file
data = np.load('dataset.npz')

# Access arrays by name
loaded_features = data['features']
loaded_labels = data['labels']
loaded_metadata = data['metadata']

print("Features:")
print(loaded_features)
print("\nLabels:")
print(loaded_labels)
print("\nMetadata:")
print(loaded_metadata)

# List all arrays in file
print(f"\nArrays in file: {data.files}")

# Close when done
data.close()
```

**Compressed .npz Files:**

```python
# Large arrays
X_train = np.random.rand(10000, 100)
y_train = np.random.randint(0, 10, 10000)
X_test = np.random.rand(2000, 100)
y_test = np.random.randint(0, 10, 2000)

# Save uncompressed
np.savez('data_uncompressed.npz',
         X_train=X_train, y_train=y_train,
         X_test=X_test, y_test=y_test)

# Save compressed
np.savez_compressed('data_compressed.npz',
                    X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test)

# Compare file sizes
import os
size_uncompressed = os.path.getsize('data_uncompressed.npz')
size_compressed = os.path.getsize('data_compressed.npz')

print(f"Uncompressed: {size_uncompressed / 1024:.2f} KB")
print(f"Compressed: {size_compressed / 1024:.2f} KB")
print(f"Compression ratio: {size_uncompressed / size_compressed:.2f}x")
```

**Context Manager (Recommended):**

```python
# Automatically closes file
with np.load('dataset.npz') as data:
    features = data['features']
    labels = data['labels']
    print(f"Loaded {len(features)} samples")
# File automatically closed here
```

---

### Section 3: Text Files - .txt and .csv (3 minutes)

**Saving to Text File:**

```python
import numpy as np

# Simple array
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Save as text
np.savetxt('data.txt', data)
print("Saved to data.txt")

# Save as CSV
np.savetxt('data.csv', data, delimiter=',')
print("Saved to data.csv")

# With formatting
np.savetxt('data_formatted.txt', data, 
           fmt='%d',  # Integer format
           delimiter='\t',  # Tab-separated
           header='Col1\tCol2\tCol3',  # Header
           comments='')  # No comment char
```

**Loading from Text File:**

```python
# Load from text
loaded_txt = np.loadtxt('data.txt')
print("From .txt:")
print(loaded_txt)

# Load from CSV
loaded_csv = np.loadtxt('data.csv', delimiter=',')
print("\nFrom .csv:")
print(loaded_csv)

# With data types
mixed_data = np.loadtxt('data.csv', 
                        delimiter=',',
                        dtype=int)
print("\nAs integers:")
print(mixed_data)
```

**When to Use Text Files:**
- Human-readable format needed
- Sharing with non-Python tools
- Small datasets
- Need to inspect data manually
- Compatibility with spreadsheets

**Limitations:**
```python
# Text files lose precision
precise = np.array([1.123456789123456789])
np.savetxt('precise.txt', precise)
loaded_precise = np.loadtxt('precise.txt')

print(f"Original: {precise[0]:.20f}")
print(f"Loaded:   {loaded_precise[0]:.20f}")
# Some precision lost!

# Binary preserves exact values
np.save('precise.npy', precise)
loaded_binary = np.load('precise.npy')
print(f"Binary:   {loaded_binary[0]:.20f}")
# Exact match!
```

---

### Section 4: Advanced Loading Options (3 minutes)

**Loading with genfromtxt (Handles Missing Data):**

```python
import numpy as np

# Create CSV with missing values
data_str = """1,2,3
4,,6
7,8,"""

with open('missing.csv', 'w') as f:
    f.write(data_str)

# Load with genfromtxt
data = np.genfromtxt('missing.csv', 
                     delimiter=',',
                     filling_values=0)  # Replace missing with 0

print("Data with filled missing values:")
print(data)

# Or mark as NaN
data_nan = np.genfromtxt('missing.csv', 
                         delimiter=',')

print("\nData with NaN:")
print(data_nan)
```

**Loading Specific Columns:**

```python
# Create data file
full_data = np.array([[1, 2, 3, 4, 5],
                      [6, 7, 8, 9, 10],
                      [11, 12, 13, 14, 15]])

np.savetxt('full_data.csv', full_data, delimiter=',', fmt='%d')

# Load only columns 0, 2, 4
selected = np.loadtxt('full_data.csv', 
                      delimiter=',',
                      usecols=[0, 2, 4])

print("Selected columns [0, 2, 4]:")
print(selected)
```

**Skipping Rows:**

```python
# Create file with header
with open('with_header.csv', 'w') as f:
    f.write('# This is a header\n')
    f.write('# Another comment\n')
    f.write('1,2,3\n4,5,6\n7,8,9\n')

# Skip first 2 rows
data = np.loadtxt('with_header.csv', 
                  delimiter=',',
                  skiprows=2)

print("Data (header skipped):")
print(data)
```

---

### Section 5: Memory-Mapped Files (2 minutes)

**For Very Large Arrays:**

```python
import numpy as np

# Create large array on disk without loading into memory
large = np.memmap('large_array.dat', 
                  dtype='float32',
                  mode='w+',  # Write mode
                  shape=(10000, 10000))

# Fill data (only loads needed portions)
large[0:100, 0:100] = np.random.rand(100, 100)

# Flush to disk
large.flush()
print("Large array created on disk")

# Load memory-mapped array
loaded_mmap = np.memmap('large_array.dat',
                        dtype='float32',
                        mode='r',  # Read-only
                        shape=(10000, 10000))

# Access data (loads on demand)
subset = loaded_mmap[0:100, 0:100]
print(f"Subset shape: {subset.shape}")
print(f"First value: {subset[0, 0]:.6f}")
```

**When to Use Memory Mapping:**
- Arrays too large for RAM
- Need random access to large data
- Sharing data between processes
- Efficient partial reading

---

### Section 6: Practical Applications and Best Practices (3 minutes)

**Application 1: Checkpointing Training**

```python
import numpy as np

# Simulate training
epochs = 5
for epoch in range(epochs):
    # Simulate model state
    weights = np.random.rand(100, 10)
    losses = np.random.rand(100)
    
    # Save checkpoint
    np.savez(f'checkpoint_epoch_{epoch}.npz',
             weights=weights,
             losses=losses,
             epoch=np.array([epoch]))
    
    print(f"Epoch {epoch} checkpoint saved")

# Resume from checkpoint
checkpoint = np.load('checkpoint_epoch_4.npz')
resume_epoch = checkpoint['epoch'][0]
resume_weights = checkpoint['weights']

print(f"\nResuming from epoch {resume_epoch}")
print(f"Weights shape: {resume_weights.shape}")
```

**Application 2: Data Pipeline**

```python
# Step 1: Process and save raw data
raw_data = np.random.rand(1000, 50)
np.save('01_raw_data.npy', raw_data)

# Step 2: Load, transform, save
raw = np.load('01_raw_data.npy')
normalized = (raw - raw.mean(axis=0)) / raw.std(axis=0)
np.save('02_normalized.npy', normalized)

# Step 3: Load, split, save
data = np.load('02_normalized.npy')
train = data[:800]
test = data[800:]
np.savez_compressed('03_train_test_split.npz',
                    train=train, test=test)

print("Data pipeline completed")
```

**Application 3: Archiving Results**

```python
import datetime

# Experiment results
results = {
    'accuracy': np.array([0.85, 0.87, 0.89, 0.90, 0.91]),
    'loss': np.array([0.45, 0.38, 0.32, 0.28, 0.25]),
    'predictions': np.random.rand(100, 10),
    'timestamp': np.array([str(datetime.datetime.now())])
}

# Save with timestamp
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'experiment_{timestamp}.npz'
np.savez_compressed(filename, **results)

print(f"Results archived to {filename}")
```

**Best Practices:**

```python
# 1. Use compression for storage
np.savez_compressed('data.npz', X=X, y=y)  # ✓

# 2. Use context managers
with np.load('data.npz') as data:  # ✓
    X = data['X']

# 3. Add metadata
np.savez('model.npz',
         weights=weights,
         version=np.array(['v1.0']),
         date=np.array([str(datetime.datetime.now())]))

# 4. Verify after saving
saved_data = np.array([1, 2, 3])
np.save('verify.npy', saved_data)
loaded = np.load('verify.npy')
assert np.array_equal(saved_data, loaded), "Save/load mismatch!"

# 5. Clean up old files
import os
if os.path.exists('old_data.npy'):
    os.remove('old_data.npy')
```

---

### Summary (1 minute)

**Key Functions Covered:**

1. **Binary Format (.npy):**
   - `np.save(file, arr)` - save single array
   - `np.load(file)` - load array
   - Fast, preserves dtype, efficient

2. **Multiple Arrays (.npz):**
   - `np.savez(file, arr1=arr1, arr2=arr2)` - uncompressed
   - `np.savez_compressed(file, ...)` - compressed
   - `np.load(file)` returns dict-like object

3. **Text Format:**
   - `np.savetxt(file, arr, delimiter=',')` - save
   - `np.loadtxt(file, delimiter=',')` - load
   - Human-readable but slower, less precise

4. **Advanced:**
   - `np.genfromtxt()` - handles missing data
   - `np.memmap()` - memory-mapped files
   - Column selection, row skipping

**Quick Reference:**

```python
# Single array (binary)
np.save('data.npy', arr)
arr = np.load('data.npy')

# Multiple arrays (binary)
np.savez_compressed('data.npz', X=X, y=y)
data = np.load('data.npz')
X, y = data['X'], data['y']

# Text file
np.savetxt('data.csv', arr, delimiter=',')
arr = np.loadtxt('data.csv', delimiter=',')
```

**Choosing Format:**

| Format | Use When | Pros | Cons |
|--------|----------|------|------|
| .npy | Single array | Fast, exact | One array only |
| .npz | Multiple arrays | Organized, compressed | Slight overhead |
| .txt/.csv | Human needs to read | Readable | Slow, less precise |
| memmap | Too large for RAM | Efficient access | Complex |

**Remember:**
- Use .npy/.npz for NumPy workflows
- Use compression for storage
- Use text for sharing/inspection
- Always verify critical saves
- Add metadata for experiments

**Next Steps:**
- Practice saving/loading workflows
- Build data pipelines
- Implement checkpointing
- Optimize storage vs speed

Proper data persistence prevents lost work and enables collaboration!
