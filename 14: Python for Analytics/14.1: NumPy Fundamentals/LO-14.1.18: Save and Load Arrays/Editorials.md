## Editorials: Save and Load Arrays

### Q1 Solution: Save and Load Single Array

```python
import numpy as np

# Create random array
np.random.seed(42)
data = np.random.randint(10, 100, (3, 4))

print("Original array:")
print(data)

# Save to .npy file
np.save('random_data.npy', data)
print("\nArray saved to random_data.npy")

# Load from file
loaded = np.load('random_data.npy')
print("\nLoaded array:")
print(loaded)

# Verify
identical = np.array_equal(data, loaded)
print(f"\nArrays are identical: {identical}")
print(f"Original dtype: {data.dtype}")
print(f"Loaded dtype: {loaded.dtype}")
```

**Explanation:**
- `np.save()` saves array in NumPy's binary format
- File extension .npy added automatically if not provided
- `np.load()` loads the array back
- Binary format preserves exact dtype and values
- Use `np.array_equal()` to verify perfect match
- .npy is fastest format for NumPy arrays

---

### Q2 Solution: Save and Load Multiple Arrays

```python
import numpy as np
import os

# Create arrays
np.random.seed(123)
features = np.random.rand(100, 5)
labels = np.random.randint(0, 3, 100)
weights = np.random.rand(5)

print("Created arrays:")
print(f"features shape: {features.shape}")
print(f"labels shape: {labels.shape}")
print(f"weights shape: {weights.shape}")

# Save compressed
np.savez_compressed('dataset.npz',
                    features=features,
                    labels=labels,
                    weights=weights)

print("\nSaved to dataset.npz")

# Load
data = np.load('dataset.npz')

print("\nLoaded from dataset.npz:")
print(f"Arrays in file: {list(data.files)}")

print(f"\nfeatures shape: {data['features'].shape}")
print(f"labels shape: {data['labels'].shape}")
print(f"weights shape: {data['weights'].shape}")

# File size
file_size = os.path.getsize('dataset.npz')
print(f"\nFile size: {file_size / 1024:.1f} KB")

# Close
data.close()
```

**Explanation:**
- `np.savez_compressed()` saves multiple arrays with compression
- Arrays accessed by name (dictionary-like)
- `.files` attribute lists all array names
- Compression reduces file size significantly
- Always close .npz files or use context manager
- Useful for organizing related arrays together

---

### Q3 Solution: Text File Operations with Formatting

```python
import numpy as np

# Student scores
scores = np.array([[85, 90, 78, 88],
                   [92, 88, 95, 90],
                   [76, 85, 80, 82],
                   [88, 92, 87, 89]])

subjects = ['Math', 'Science', 'English', 'History']

print("Original scores:")
print(scores)

# Save as tab-delimited text with header
header = '\t'.join(subjects)
np.savetxt('scores.txt', scores,
           fmt='%d',
           delimiter='\t',
           header=header,
           comments='')

print("\nSaved to scores.txt (tab-delimited with header)")

# Save as CSV
np.savetxt('scores.csv', scores,
           fmt='%d',
           delimiter=',')

print("Saved to scores.csv (comma-delimited)")

# Load both
loaded_txt = np.loadtxt('scores.txt', delimiter='\t', skiprows=1)
loaded_csv = np.loadtxt('scores.csv', delimiter=',')

print("\nLoaded from scores.txt:")
print(loaded_txt)

print("\nLoaded from scores.csv:")
print(loaded_csv)

# Compare
match = np.allclose(scores, loaded_txt) and np.allclose(scores, loaded_csv)
print(f"\nText files match original: {match}")
print(f"Data type changed from {scores.dtype} to {loaded_txt.dtype}")
```

**Explanation:**
- `np.savetxt()` saves in human-readable format
- `fmt='%d'` specifies integer format
- `delimiter` sets column separator
- `header` adds column names (with `comments=''`)
- `np.loadtxt()` loads text files
- `skiprows=1` skips header when loading
- Text format converts to float by default
- Use for sharing with non-Python tools

---

### Q4 Solution: Model Checkpoint System

```python
import numpy as np
import os

# Training configuration
np.random.seed(456)
num_epochs = 6
checkpoint_interval = 2

# Initialize
weights_shape = (100, 10)
loss_history = []
val_acc_history = []

print("Training started...\n")

# Training loop
for epoch in range(num_epochs):
    # Simulate training
    weights = np.random.rand(*weights_shape)
    loss = 1.0 / (epoch + 1) + np.random.rand() * 0.2
    val_acc = 0.5 + (epoch / num_epochs) * 0.3 + np.random.rand() * 0.05
    
    loss_history.append(loss)
    val_acc_history.append(val_acc)
    
    print(f"Epoch {epoch}: loss={loss:.4f}, val_acc={val_acc:.4f}")
    
    # Save checkpoint
    if (epoch + 1) % checkpoint_interval == 0:
        checkpoint_file = f'checkpoint_epoch_{epoch}.npz'
        np.savez_compressed(checkpoint_file,
                           weights=weights,
                           loss_history=np.array(loss_history),
                           val_acc_history=np.array(val_acc_history),
                           epoch=np.array([epoch]))
        print(f"Checkpoint saved: {checkpoint_file}\n")

print("Training completed.\n")

# Find latest checkpoint
checkpoints = [f for f in os.listdir('.') if f.startswith('checkpoint_epoch_')]
latest = sorted(checkpoints)[-1]

print(f"Loading latest checkpoint: {latest}")

# Load checkpoint
checkpoint = np.load(latest)
resume_epoch = checkpoint['epoch'][0]
resume_weights = checkpoint['weights']
resume_loss = checkpoint['loss_history'][-1]
resume_val_acc = checkpoint['val_acc_history'][-1]

print(f"Resuming from epoch: {resume_epoch}")
print(f"Weights shape: {resume_weights.shape}")
print(f"Final loss: {resume_loss:.4f}")
print(f"Final validation accuracy: {resume_val_acc:.4f}")

print(f"\nContinuing training from epoch {resume_epoch + 1}...")

checkpoint.close()
```

**Explanation:**
- Checkpoints save model state periodically
- Include all necessary info to resume
- Use epoch number in filename for tracking
- Load latest checkpoint to resume training
- Prevents losing work from crashes
- Essential for long-running experiments
- Compress to save disk space

---

### Q5 Solution: Data Pipeline with Compression Analysis

```python
import numpy as np
import os
import time

print("Data Pipeline Started")
print("=" * 21)

# Step 1: Generate raw data
print("\nStep 1: Generate raw data")
np.random.seed(789)
raw_data = np.random.rand(10000, 50)
print(f"  Created: {raw_data.shape}")

start = time.time()
np.save('01_raw_data.npy', raw_data)
save_time = time.time() - start
size_raw = os.path.getsize('01_raw_data.npy')

print(f"  Saved to: 01_raw_data.npy")
print(f"  File size: {size_raw / 1024:.1f} KB")
print(f"  Save time: {save_time:.4f}s")

# Step 2: Normalize
print("\nStep 2: Normalize data")
loaded_raw = np.load('01_raw_data.npy')
normalized = (loaded_raw - loaded_raw.mean(axis=0)) / loaded_raw.std(axis=0)
print(f"  Loaded: 01_raw_data.npy")
print(f"  Normalized: mean={normalized.mean():.2f}, std={normalized.std():.2f}")

np.save('02_normalized.npy', normalized)
size_norm = os.path.getsize('02_normalized.npy')
print(f"  Saved to: 02_normalized.npy")
print(f"  File size: {size_norm / 1024:.1f} KB")

# Step 3: Split
print("\nStep 3: Train/Val/Test split")
train = normalized[:7000]
val = normalized[7000:8500]
test = normalized[8500:]

print(f"  Train: {train.shape}")
print(f"  Val: {val.shape}")
print(f"  Test: {test.shape}")

# Uncompressed
start = time.time()
np.savez('03_split.npz', train=train, val=val, test=test)
save_time_uncomp = time.time() - start
size_uncomp = os.path.getsize('03_split.npz')

print(f"\n  Uncompressed save: 03_split.npz")
print(f"  File size: {size_uncomp / 1024:.1f} KB")
print(f"  Save time: {save_time_uncomp:.4f}s")

# Compressed
start = time.time()
np.savez_compressed('03_split_compressed.npz', 
                   train=train, val=val, test=test)
save_time_comp = time.time() - start
size_comp = os.path.getsize('03_split_compressed.npz')

print(f"\n  Compressed save: 03_split_compressed.npz")
print(f"  File size: {size_comp / 1024:.1f} KB")
print(f"  Save time: {save_time_comp:.4f}s")

ratio = size_uncomp / size_comp
space_saved = size_uncomp - size_comp

print(f"\n  Compression ratio: {ratio:.2f}x")
print(f"  Space saved: {space_saved / 1024:.1f} KB")

# Step 4: Verify
print("\nStep 4: Verify integrity")
start = time.time()
data = np.load('03_split_compressed.npz')
load_time = time.time() - start

print(f"  Loading 03_split_compressed.npz")
print(f"  Load time: {load_time:.4f}s")

train_match = np.array_equal(train, data['train'])
val_match = np.array_equal(val, data['val'])
test_match = np.array_equal(test, data['test'])

print(f"  Train data matches: {train_match}")
print(f"  Val data matches: {val_match}")
print(f"  Test data matches: {test_match}")

data.close()

print("\nPipeline completed successfully!")

# Summary
total_uncomp = size_raw + size_norm + size_uncomp
total_comp = size_raw + size_norm + size_comp
total_saved = total_uncomp - total_comp

print("\nSummary:")
print(f"- Total uncompressed size: {total_uncomp / 1024:.1f} KB")
print(f"- Total compressed size: {total_comp / 1024:.1f} KB")
print(f"- Total space saved: {total_saved / 1024:.1f} KB ({total_saved / total_uncomp * 100:.1f}%)")
print(f"- Compression overhead: {save_time_comp - save_time_uncomp:.4f}s (worthwhile for storage)")
```

**Explanation:**
- Pipeline stages: generate → normalize → split → save
- Save at each stage for reproducibility
- Compare compressed vs uncompressed formats
- Measure time and space tradeoffs
- Verify data integrity after compression
- Compression worthwhile for storage (3-4x reduction)
- Slight save time increase, but fast load
- Best practice for production pipelines

---

### Key Concepts Demonstrated:

1. **Binary vs Text:**
   - Binary: fast, exact, efficient
   - Text: readable, shareable, slower

2. **Single vs Multiple:**
   - .npy: one array, simplest
   - .npz: multiple arrays, organized

3. **Compression:**
   - Reduces storage significantly (3-4x)
   - Small save time increase
   - Essential for large datasets

4. **Checkpointing:**
   - Save training state periodically
   - Enables recovery from failures
   - Track experiments over time

5. **Best Practices:**
   - Verify saves with loads
   - Use compression for storage
   - Add metadata to .npz files
   - Build reproducible pipelines
   - Clean up temporary files
