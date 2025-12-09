# **Predictive (Discriminative) vs Generative Models**

## **1. What Are Discriminative (Predictive) Models?**

<img src="https://coding-platform.s3.amazonaws.com/dev/lms/tickets/d9f12751-5f18-447c-8e38-de1f3b22cf9d/dpEsUMHyg2CwmoDX.png" />

* Focus on **predicting labels or outcomes**
* Learn the boundary between classes
* Model **P(y | x)** → Probability of label *y* given input *x*
* Common algorithms:

  * Logistic Regression
  * Support Vector Machines (SVM)
  * Random Forest
  * Gradient Boosting

### **Examples**

* Predicting if an email is spam
* Classifying sentiment as positive or negative
* Forecasting house prices

---

## **2. What Are Generative Models?**

<img src="https://coding-platform.s3.amazonaws.com/dev/lms/tickets/4850a740-b60f-4704-8e51-e9e61ac2a6d4/yDtoeR0zsJuhhfeQ.png" />

* Focus on **creating new data** similar to training data
* Learn the **joint distribution** of data
* Model **P(x, y)** or **P(x)**
* Can generate:

  * Text
  * Images
  * Audio
  * Synthetic data

### **Popular generative models**

* Variational Autoencoders (VAEs)
* Generative Adversarial Networks (GANs)
* Diffusion Models
* Large Language Models (LLMs)

### **Examples**

* Generating realistic images
* Producing new text responses
* Creating music or code snippets

---

## **3. Core Difference Explained**

### **What they learn**

| Model Type         | Learns          | Meaning                   |                           |
| ------------------ | --------------- | ------------------------- | ------------------------- |
| **Discriminative** | P(y             | x)                        | Predict the correct label |
| **Generative**     | P(x) or P(x, y) | Generate or recreate data |                           |

---

### **Nature of Output**

* **Discriminative Models → Predict**
  Output is fixed: class label, number, or category.

* **Generative Models → Create**
  Output is variable: sentences, images, designs, answers.

---

### **Example to Understand the Difference**

#### Scenario: Emails about job interviews

* **Discriminative Model:**
  Predicts whether the email is *important* or *not important*

* **Generative Model:**
  Generates a **reply** to the email

One **classifies**, one **creates**.

---

## **4. Why This Matters**

* Discriminative models are excellent for:

  * Accurate predictions
  * Classification and regression tasks

* Generative models are powerful for:

  * Creative tasks
  * Content generation
  * Simulation and synthetic data creation

Understanding the difference helps you:

* Choose the right model for the right use-case
* Design better AI workflows
* Explain AI behavior clearly in real-world scenarios

