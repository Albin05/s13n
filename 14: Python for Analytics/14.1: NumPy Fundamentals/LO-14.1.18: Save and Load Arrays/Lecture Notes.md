## Save and Load Arrays

### Binary Format (.npy)

**Single Array:**
```python
import numpy as np

# Save
data = np.array([[1, 2, 3], [4, 5, 6]])
np.save('data.npy', data)

# Load
loaded = np.load('data.npy')
```

**Advantages:**
- Fast read/write
- Preserves exact dtype
- Efficient for large arrays
- NumPy native format

---

### Multiple Arrays (.npz)

**Uncompressed:**
```python
np.savez('data.npz', X=X, y=y, weights=w)

data = np.load('data.npz')
X = data['X']
y = data['y']
data.close()
```

**Compressed:**
```python
np.savez_compressed('data.npz', X=X, y=y)

# Typical 3-4x size reduction
```

**Context Manager:**
```python
with np.load('data.npz') as data:
    X = data['X']
# Auto-closes
```

---

### Text Files

**Save:**
```python
# CSV
np.savetxt('data.csv', arr, delimiter=',')

# Tab-delimited with header
np.savetxt('data.txt', arr,
           delimiter='\t',
           header='Col1\tCol2',
           comments='',
           fmt='%d')
```

**Load:**
```python
# CSV
data = np.loadtxt('data.csv', delimiter=',')

# Skip header
data = np.loadtxt('data.txt', 
                  delimiter='\t',
                  skiprows=1)

# Select columns
data = np.loadtxt('data.csv',
                  delimiter=',',
                  usecols=[0, 2, 4])
```

**When to Use:**
- Human needs to read
- Sharing with Excel/spreadsheets
- Non-Python tools
- Small datasets

---

### Advanced Loading

**Handle Missing Data:**
```python
data = np.genfromtxt('data.csv',
                     delimiter=',',
                     filling_values=0)

# Or mark as NaN
data = np.genfromtxt('data.csv', delimiter=',')
```

**Memory-Mapped Files:**
```python
# Create
large = np.memmap('large.dat',
                  dtype='float32',
                  mode='w+',
                  shape=(10000, 10000))

# Load (on-demand access)
loaded = np.memmap('large.dat',
                   dtype='float32',
                   mode='r',
                   shape=(10000, 10000))
```

**Use When:**
- Array too large for RAM
- Need random access
- Shared memory between processes

---

### Practical Patterns

**Checkpointing:**
```python
# Save training state
np.savez_compressed(f'checkpoint_{epoch}.npz',
                   weights=weights,
                   loss=loss_history,
                   epoch=epoch)

# Resume
data = np.load('checkpoint_5.npz')
weights = data['weights']
epoch = data['epoch']
```

**Data Pipeline:**
```python
# Step 1
np.save('01_raw.npy', raw_data)

# Step 2
raw = np.load('01_raw.npy')
processed = transform(raw)
np.save('02_processed.npy', processed)

# Step 3
data = np.load('02_processed.npy')
train, test = split(data)
np.savez_compressed('03_split.npz',
                   train=train, test=test)
```

**Verification:**
```python
# Always verify important saves
np.save('critical.npy', data)
loaded = np.load('critical.npy')
assert np.array_equal(data, loaded)
```

---

### Quick Reference

**Save:**
```python
np.save('file.npy', arr)              # Single
np.savez('file.npz', a=a, b=b)        # Multiple
np.savez_compressed('file.npz', ...)  # Compressed
np.savetxt('file.csv', arr, delimiter=',')  # Text
```

**Load:**
```python
arr = np.load('file.npy')                    # Binary
data = np.load('file.npz'); x = data['x']    # .npz
arr = np.loadtxt('file.csv', delimiter=',')  # Text
```

---

### Format Comparison

| Format | Speed | Size | Precision | Readable |
|--------|-------|------|-----------|----------|
| .npy | ⚡⚡⚡ | Medium | ✓ Exact | ✗ |
| .npz | ⚡⚡ | Small (compressed) | ✓ Exact | ✗ |
| .txt/.csv | ⚡ | Large | ≈ Approx | ✓ |

---

### Best Practices

1. **Use compression for storage:**
   ```python
   np.savez_compressed('data.npz', X=X, y=y)
   ```

2. **Use context managers:**
   ```python
   with np.load('data.npz') as data:
       X = data['X']
   ```

3. **Add metadata:**
   ```python
   np.savez('model.npz',
            weights=w,
            version='v1.0',
            date=str(datetime.now()))
   ```

4. **Verify saves:**
   ```python
   loaded = np.load('data.npy')
   assert np.array_equal(original, loaded)
   ```

5. **Clean up:**
   ```python
   if os.path.exists('temp.npy'):
       os.remove('temp.npy')
   ```

---

### Key Takeaways

1. **Choose format wisely:**
   - .npy for single arrays
   - .npz for multiple/compressed
   - .txt for sharing/inspection

2. **Compression is free:**
   - 3-4x size reduction
   - Minimal time overhead
   - Always use for storage

3. **Build pipelines:**
   - Save at each stage
   - Enable reproducibility
   - Checkpoint long processes

4. **Verify critical data:**
   - Check saves immediately
   - Compare before/after
   - Prevent data loss
