## Question Bank: Save and Load Arrays

### Q1: Save and Load Single Array (3 minutes, Low Difficulty)

**Problem:**
Create an array with random integers, save it to a .npy file, load it back, and verify they are identical.

**Expected Output:**
```
Original array:
[[45 67 23 89]
 [12 56 78 34]
 [90 45 67 23]]

Array saved to random_data.npy

Loaded array:
[[45 67 23 89]
 [12 56 78 34]
 [90 45 67 23]]

Arrays are identical: True
Original dtype: int64
Loaded dtype: int64
```

**Category:** Implementation  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q2: Save and Load Multiple Arrays (3 minutes, Low Difficulty)

**Problem:**
Create three arrays (features, labels, and weights). Save them together in a compressed .npz file. Load them back and display all array names and shapes.

**Expected Output:**
```
Created arrays:
features shape: (100, 5)
labels shape: (100,)
weights shape: (5,)

Saved to dataset.npz

Loaded from dataset.npz:
Arrays in file: ['features', 'labels', 'weights']

features shape: (100, 5)
labels shape: (100,)
weights shape: (5,)

File size: 4.2 KB
```

**Category:** Implementation  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q3: Text File Operations with Formatting (5 minutes, Medium Difficulty)

**Problem:**
Create a 2D array of student scores. Save it as:
1. A .txt file with tab delimiters and column headers
2. A .csv file with comma delimiters
Then load both files and compare them with the original.

**Input:**
```python
scores = np.array([[85, 90, 78, 88],
                   [92, 88, 95, 90],
                   [76, 85, 80, 82],
                   [88, 92, 87, 89]])
subjects = ['Math', 'Science', 'English', 'History']
```

**Expected Output:**
```
Original scores:
[[85 90 78 88]
 [92 88 95 90]
 [76 85 80 82]
 [88 92 87 89]]

Saved to scores.txt (tab-delimited with header)
Saved to scores.csv (comma-delimited)

Loaded from scores.txt:
[[85. 90. 78. 88.]
 [92. 88. 95. 90.]
 [76. 85. 80. 82.]
 [88. 92. 87. 89.]]

Loaded from scores.csv:
[[85. 90. 78. 88.]
 [92. 88. 95. 90.]
 [76. 85. 80. 82.]
 [88. 92. 87. 89.]]

Text files match original: True
Data type changed from int64 to float64
```

**Category:** Implementation  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q4: Model Checkpoint System (5 minutes, Medium Difficulty)

**Problem:**
Simulate a training loop that saves checkpoints every 2 epochs. Each checkpoint should include:
- Model weights (random array)
- Training loss history
- Validation accuracy history
- Epoch number

Then load the latest checkpoint and resume training from that point.

**Expected Output:**
```
Training started...

Epoch 0: loss=0.8234, val_acc=0.6543
Epoch 1: loss=0.7123, val_acc=0.7012
Checkpoint saved: checkpoint_epoch_1.npz

Epoch 2: loss=0.6234, val_acc=0.7456
Epoch 3: loss=0.5543, val_acc=0.7823
Checkpoint saved: checkpoint_epoch_3.npz

Epoch 4: loss=0.4987, val_acc=0.8123
Epoch 5: loss=0.4456, val_acc=0.8334
Checkpoint saved: checkpoint_epoch_5.npz

Training completed.

Loading latest checkpoint: checkpoint_epoch_5.npz
Resuming from epoch: 5
Weights shape: (100, 10)
Final loss: 0.4456
Final validation accuracy: 0.8334

Continuing training from epoch 6...
```

**Category:** Application  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Q5: Data Pipeline with Compression Analysis (5 minutes, Medium Difficulty)

**Problem:**
Create a data processing pipeline that:
1. Generates raw data (10000 samples, 50 features)
2. Normalizes the data
3. Splits into train/validation/test sets (70/15/15)
4. Saves at each stage
5. Compares file sizes between uncompressed and compressed formats
6. Measures save/load times

**Expected Output:**
```
Data Pipeline Started
=====================

Step 1: Generate raw data
  Created: (10000, 50)
  Saved to: 01_raw_data.npy
  File size: 3906.3 KB
  Save time: 0.0234s

Step 2: Normalize data
  Loaded: 01_raw_data.npy
  Normalized: mean=0.00, std=1.00
  Saved to: 02_normalized.npy
  File size: 3906.3 KB

Step 3: Train/Val/Test split
  Train: (7000, 50)
  Val: (1500, 50)
  Test: (1500, 50)
  
  Uncompressed save: 03_split.npz
  File size: 3906.5 KB
  Save time: 0.0456s
  
  Compressed save: 03_split_compressed.npz
  File size: 1234.2 KB
  Save time: 0.1234s
  
  Compression ratio: 3.17x
  Space saved: 2672.3 KB

Step 4: Verify integrity
  Loading 03_split_compressed.npz
  Load time: 0.0345s
  Train data matches: True
  Val data matches: True
  Test data matches: True

Pipeline completed successfully!

Summary:
- Total uncompressed size: 11719.1 KB
- Total compressed size: 5140.5 KB
- Total space saved: 6578.6 KB (56.1%)
- Compression overhead: 0.0778s (worthwhile for storage)
```

**Category:** Application  
**Prerequisite LOs:** 14.1.1, 14.1.2

---

### Additional Practice Problems

**Challenge 1: Incremental Saving**
Implement a system that saves data incrementally (appending to file) for streaming applications.

**Challenge 2: Versioned Data Storage**
Create a system that saves multiple versions of data with timestamps and metadata, allowing rollback to previous versions.

**Challenge 3: Custom File Format**
Design a custom binary format that includes metadata, compression, and checksums for data integrity.

**Challenge 4: Distributed Storage**
Save large arrays across multiple files for distributed processing, then load and combine them back.
