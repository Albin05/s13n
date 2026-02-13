
# Editorials

## Q1
### Title
Data Efficiency Comparison

### Problem Description
Identify the concept illustrating the difference in sample size needed for learning.

### Objective
Understand the data-hungry nature of current ML.

### Hint
Humans are "efficient" with data; machines are not.

### Short Explanation
The scenario highlights **Data Efficiency**. Humans need few samples (High Efficiency); machines need many (Low Efficiency).

### Detailed Explanation
* **Data Efficiency:** The amount of data required to reach a certain level of performance.
* Current ML algorithms (especially Deep Learning) are notoriously data-inefficient compared to the human brain, which uses prior knowledge and reasoning to learn from sparse data.

---

## Q2
### Title
Weight Update Simulation

### Problem Description
Implement the basic math of a learning step (Gradient Descent conceptualization).

### Objective
Demonstrate how machines mathematically "learn".

### Hint
Apply the formula strictly.

### Short Explanation
$0.5 + (0.2 \times 0.1) = 0.5 + 0.02 = 0.52$.

### Detailed Explanation
```python
def update_weight(w, error, learning_rate):
    return w + (error * learning_rate)

```

This is the fundamental operation inside almost all neural network training loops (Backpropagation).

---

## Q3

### Title

Iterative Correction

### Problem Description

Calculate the new guess after one correction step.
Guess: 50, Target: 100, Rate: 10%.

### Objective

Simulate the "Error-Correction" loop.

### Hint

Error = Target - Guess. Correction = Error * 0.1.

### Short Explanation

Error = 50. Correction = 5. New Guess = 55.

### Detailed Explanation

1. **Calculate Error:** .
2. **Calculate Step:** .
3. **Update Guess:** .
The machine has "learned" and moved closer to the truth.

---

## Q4

### Title

Characteristics of ML

### Problem Description

Select features specific to Machine Learning.

### Objective

Distinguish biological constraints from algorithmic constraints.

### Hint

Machines deal with math and data, not feelings or stories.

### Short Explanation

A and C are true. B and D are human traits.

### Detailed Explanation

* **A (True):** Machines need a loss function to optimize.
* **B (False):** Machines do not have intuition; they have probability.
* **C (True):** More data usually reduces variance and improves the model.
* **D (False):** Abstraction from single instances is a human strength.

---

## Q5

### Title

Simulating Forgetting

### Problem Description

Implement a value decay function.

### Objective

Model the concept of "Catastrophic Forgetting" or simple decay.

### Hint

Multiply by 0.9 for decay.

### Short Explanation

Use a global or class variable to store the state.

### Detailed Explanation

```python
memory = 100

def passage_of_time():
    global memory
    memory = memory * 0.9
    return memory

def reinforce():
    global memory
    memory = 100
    return memory

```

---

## Q6

### Title

Context and Ambiguity

### Problem Description

Explain why humans handle homonyms ("Bat") better than machines.

### Objective

Discuss the limitation of machines in understanding context without vast data.

### Hint

Humans use "World Knowledge" (Caves have animals, Baseball has equipment).

### Short Explanation

Humans possess "World Models" and common sense. Machines only look at statistical co-occurrences of words.

### Detailed Explanation

* **Human Context:** We know caves are dark places where animals live, and baseball is a sport. We use this *external* knowledge to disambiguate the word "bat."
* **Machine Context:** A machine sees "bat" as a vector of numbers. Unless it has seen "bat" appearing near "cave" and "bat" appearing near "ball" thousands of times (in training data), it cannot distinguish the meanings. It lacks a fundamental understanding of the physical world.

```

```
