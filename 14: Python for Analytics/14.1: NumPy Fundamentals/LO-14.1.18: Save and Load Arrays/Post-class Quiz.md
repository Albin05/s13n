## Post-class Quiz: Save and Load Arrays

### Question 1
Which format preserves NumPy array dtypes exactly?

A) .txt files
B) .csv files
C) .npy files
D) JSON files

**Correct Answer: C**
*Explanation: .npy is NumPy's binary format that preserves exact dtypes, shapes, and values. Text formats like .txt and .csv convert data (often to float) and may lose precision*

---

### Question 2
What is the advantage of `np.savez_compressed()` over `np.savez()`?

A) Faster loading
B) Smaller file size
C) Can save more arrays
D) Better data precision

**Correct Answer: B**
*Explanation: np.savez_compressed() compresses the data, resulting in smaller file sizes (typically 3-4x reduction). Loading might be slightly slower due to decompression, but storage savings are significant*

---

### Question 3
How do you access arrays from a loaded .npz file?

A) By index: data[0], data[1]
B) By name: data['array_name']
C) Using .get() method only
D) Arrays are automatically unpacked

**Correct Answer: B**
*Explanation: .npz files store arrays with names. Access them like a dictionary: data['features'], data['labels']. Use data.files to see all available names*

---

### Question 4
What does `delimiter=','` do in `np.savetxt()`?

A) Splits the array into parts
B) Separates columns with commas
C) Adds commas to all values
D) Compresses the file

**Correct Answer: B**
*Explanation: delimiter parameter specifies the character used to separate columns. delimiter=',' creates CSV format, delimiter='\t' creates tab-separated*

---

### Question 5
When should you use memory-mapped files (`np.memmap()`)?

A) For small arrays that fit in RAM
B) When you need compression
C) For arrays too large to fit in RAM
D) For text file operations

**Correct Answer: C**
*Explanation: np.memmap() creates a memory-mapped array that stays on disk and loads portions on demand. Use it when arrays are too large to fit in RAM but you need random access*
