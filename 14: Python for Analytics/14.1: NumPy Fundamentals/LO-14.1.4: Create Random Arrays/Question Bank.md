## Question Bank: Create Random Arrays

### Q1: Generate Random Float Array (3 minutes, Low Difficulty)

**Problem:**
Use `np.random.rand()` to create a 1D array of 8 random floats between 0 and 1. Set the random seed to 10 before generating the array. Print the array.

**Expected Output:**
```
[0.77132064 0.02075195 0.63364823 0.74880388 0.49850701 0.22479665
 0.19806286 0.76053071]
```

---

### Q2: Generate Random Integer Array (3 minutes, Low Difficulty)

**Problem:**
Use `np.random.randint()` to simulate 20 dice rolls (integers from 1 to 6 inclusive). Set seed to 42. Print the array and count how many times 6 appears.

**Expected Output:**
```
Dice rolls: [6 4 4 5 4 5 1 2 5 6 5 4 3 6 1 4 1 5 2 5]
Number of 6s: 3
```

---

### Q3: Create 2D Random Array (5 minutes, Medium Difficulty)

**Problem:**
Create a 5x5 matrix of random floats between 0 and 1 using `np.random.rand()`. Set seed to 1. Then:
1. Print the matrix
2. Find and print the maximum value in the matrix
3. Find and print the minimum value in the matrix

**Expected Output:**
```
Matrix:
[[4.17022005e-01 7.20324493e-01 1.14374817e-04 3.02332573e-01
  1.46755891e-01]
 [9.23385948e-02 1.86260211e-01 3.45560727e-01 3.96767474e-01
  5.38816734e-01]
 [4.19194514e-01 6.85219500e-01 2.04452250e-01 8.78117436e-01
  0.27325513e-01]
 [6.70467510e-01 4.17304802e-01 5.58689828e-01 1.40386939e-01
  1.98101489e-01]
 [8.00744569e-01 9.68261576e-01 3.13424178e-01 6.92322616e-01
  8.76389152e-01]]
Maximum value: 0.9682615757193975
Minimum value: 0.00011437481734488664
```

---

### Q4: Simulate Test Scores (5 minutes, Medium Difficulty)

**Problem:**
Generate 100 test scores that follow a normal distribution with mean=75 and standard deviation=10 using `np.random.randn()`. Set seed to 5. Calculate and print:
1. The mean of the generated scores (round to 2 decimals)
2. The standard deviation of the generated scores (round to 2 decimals)
3. How many scores are above 85

**Expected Output:**
```
Mean score: 74.61
Standard deviation: 9.68
Scores above 85: 14
```

---

### Q5: Random Sampling and Shuffling (5 minutes, Medium Difficulty)

**Problem:**
You have a list of 10 students: `['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']`

1. Set seed to 20
2. Use `np.random.choice()` to randomly select 3 students (without replacement)
3. Create a NumPy array from the original list
4. Use `np.random.shuffle()` to shuffle the array
5. Print the 3 selected students and the shuffled array

**Expected Output:**
```
Selected students: ['Grace' 'Bob' 'Jack']
Shuffled students: ['Frank' 'Charlie' 'Alice' 'Eve' 'David' 'Grace' 'Ivy' 'Jack' 'Henry' 'Bob']
```
