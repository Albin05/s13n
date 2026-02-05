## Post-class Quiz: Read Text Files in Python

---

### Question 1
What is the advantage of using `with open()` over `open()`?

A) It reads faster
B) It automatically closes the file when done
C) It creates the file if it doesn't exist
D) It reads in binary mode

**Correct Answer: B**

*Explanation: The `with` statement ensures the file is properly closed when the block exits, even if an exception occurs. Without it, you must manually call `file.close()`.*

---

### Question 2
What does `file.readlines()` return?

A) A single string
B) A list of strings, one per line
C) A list of words
D) The number of lines

**Correct Answer: B**

*Explanation: `readlines()` returns a list where each element is a line from the file (including the trailing newline character `\n`).*

---

### Question 3
Why should you use `.strip()` when reading lines?

A) To remove file metadata
B) To convert to uppercase
C) To remove trailing newline characters and whitespace
D) To split the line into words

**Correct Answer: C**

*Explanation: Lines read from files include `\n` at the end. `.strip()` removes leading and trailing whitespace including newlines, giving you clean text.*

---

### Question 4
Which approach is most memory-efficient for reading large files?

A) `content = f.read()`
B) `lines = f.readlines()`
C) `for line in f:`
D) All are the same

**Correct Answer: C**

*Explanation: Iterating with `for line in f:` reads one line at a time, using minimal memory. `read()` and `readlines()` load the entire file into memory, which fails for very large files.*

---

### Question 5
What exception should you handle for missing files?

A) `IOError`
B) `FileNotFoundError`
C) `ValueError`
D) `OSError`

**Correct Answer: B**

*Explanation: `FileNotFoundError` is raised when trying to open a file that doesn't exist. While `OSError` is its parent class and would also catch it, `FileNotFoundError` is more specific and preferred.*

---
