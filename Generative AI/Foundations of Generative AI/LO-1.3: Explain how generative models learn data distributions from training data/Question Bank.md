# **Question Bank for LO-1.3: Explain how generative models learn data distributions**

**Categories:** MCQ, Short Answer, Long Answer, Implementation
**Bloom Levels Covered:** Remember, Understand, Apply, Analyze, Evaluate, Create

---

# **1. MCQs**

### **Q1.** What does a "data distribution" represent in the context of Generative AI?

a) The way data is stored on a hard drive
b) The probability of different data points occurring in a dataset
c) The speed at which data is processed
d) The distribution of labels in a classification task
**Answer:** b

### **Q2.** If a generative model has perfectly learned the data distribution, which of the following is true?

a) It can only reproduce the exact training examples
b) It can generate new samples that are indistinguishable from the real data
c) It will always output the average of the training data
d) It becomes a discriminative model
**Answer:** b

### **Q3.** What is the role of "sampling" in a generative model?

a) To select the best model architecture
b) To pick a random point from the learned distribution to create a new output
c) To compress the training data
d) To filter out bad data points
**Answer:** b

---

# **2. Short Answer**

### **Q4.** Define "data distribution" in simple terms using a real-world example.

### **Q5.** Explain the relationship between $P_{data}$ (true distribution) and $P_{model}$ (learned distribution).

### **Q6.** Why is it important for a generative model to learn the *structure* of data (e.g., face geometry) rather than just memorizing pixels?

### **Q7.** What happens if a model's learned distribution ($P_{model}$) is very different from the real distribution ($P_{data}$)?

---

# **3. Long Answer**

### **Q8.** Describe the two main phases of generative learning (Training and Generation) in detail. Explain what happens to the model's parameters in the training phase.

### **Q9.** Use the "Art Student" analogy to explain how a generative model learns to create new content without copying. Map the student's actions to technical terms (Training, Distribution, Sampling).

### **Q10.** Compare how a Discriminative Model and a Generative Model view the same dataset. How does their goal regarding the data distribution differ?

---

# **4. Implementation Questions**

### **Q11.** Visualize a simple 1D distribution.
*   Generate 1000 random numbers following a Normal Distribution (mean=0, std=1).
*   Plot a histogram of these numbers.
*   Explain how this histogram represents the "distribution" of your data.

### **Q12.** Sampling from a distribution.
*   Use the same Normal Distribution from Q11.
*   "Sample" 5 new points.
*   Explain why these points are likely to be close to 0 but rarely exactly 0. Relate this to how a model generates "likely" images.

### **Q13.** Gaussian Mixture Model (Conceptual Implementation).
*   Create a dataset that combines two different Normal Distributions (e.g., one centered at -2, one at +2).
*   Plot the histogram.
*   Explain how a generative model would need to learn *both* peaks to generate realistic data for this dataset.
