## In-class Quiz: Create Random Arrays

### Question 1
Which function generates random floats in the range [0, 1)?

A) `np.random.randint()`
B) `np.random.rand()`
C) `np.random.randn()`
D) `np.random.uniform()`

**Correct Answer: B**

---

### Question 2
What is the purpose of `np.random.seed()`?

A) To generate faster random numbers
B) To ensure reproducible random numbers
C) To create truly random numbers
D) To set the range of random numbers

**Correct Answer: B**

---

### Question 3
What will `np.random.randint(1, 10, size=5)` generate?

A) 5 random integers from 1 to 10 (including 10)
B) 5 random integers from 1 to 9 (excluding 10)
C) 5 random floats from 1 to 10
D) A 5×10 matrix of random integers

**Correct Answer: B**
*Explanation: The high parameter (10) is exclusive, so values range from 1 to 9*

---

### Question 4
How do you generate random numbers from a normal distribution with mean=50 and std=5?

A) `np.random.rand(50, 5)`
B) `np.random.randint(50, 5)`
C) `50 + 5 * np.random.randn()`
D) `np.random.randn(50, 5)`

**Correct Answer: C**
*Explanation: Use formula: mean + std × randn() to transform standard normal*

---

### Question 5
What does `np.random.shuffle()` return?

A) A new shuffled array
B) The indices of the shuffled array
C) None (it shuffles in-place)
D) A boolean array

**Correct Answer: C**
*Explanation: shuffle() modifies the array in-place and returns None*
