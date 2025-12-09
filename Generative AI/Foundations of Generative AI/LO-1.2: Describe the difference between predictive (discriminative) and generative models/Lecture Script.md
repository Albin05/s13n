# **Lecture Script (Duration: 10 Minutes)**

### **Title: Predictive (Discriminative) Models vs Generative Models**

---

## **1. Introduction (1 minute)**

“Today we are going to understand one of the most important distinctions in modern AI — the difference between *predictive/discriminative models* and *generative models*.
This difference is at the core of how systems like spam detectors, recommendation engines, and LLMs behave.”

---

## **2. What Are Discriminative (Predictive) Models? (2 minutes)**

“Discriminative models focus on **predicting labels** or **classifying data**.
They learn the **boundary** that separates one class from another.”

Examples students already know:

* Spam vs Not Spam → Classification
* Good vs Bad Review → Sentiment analysis
* Cat vs Dog → Image classification
* Predicting house price → Regression

Key characteristics:

* Learn **P(y | x)** → probability of label *y* given input *x*
* Output is fixed: a number, label, or category
* They *cannot* create new data
* Their goal is: “Given this input, what’s the correct output?”

Analogy:
“Think of discriminative models as exam checkers — they decide which category an answer belongs to.”

<img src="https://coding-platform.s3.amazonaws.com/dev/lms/tickets/4850a740-b60f-4704-8e51-e9e61ac2a6d4/yDtoeR0zsJuhhfeQ.png" />

---

## **3. What Are Generative Models? (2.5 minutes)**

“Generative models don’t classify; they **create**.”

They can generate:

* Text
* Images
* Music
* Code
* Audio
* Synthetic datasets

Examples:

* ChatGPT generating explanations
* Stable Diffusion creating images
* Copilot writing functions

Key characteristics:

* Learn the **distribution of data**
* Model **P(x)** or **P(x, y)**
* Can produce variations or completely new content
* Outputs are not fixed — they are creative, dynamic, and probabilistic

Analogy:
“Generative models are like creative artists — they understand the style of the data and can create something new out of it.”

---

## **4. The Core Difference: P(y|x) vs P(x) (Intuition Only) (2 minutes)**

Here’s the simplest intuition:

*Discriminative models:*
“Given the input x, tell me the correct label y.”
→ They draw decision boundaries.

*Generative models:*
“Understand the entire dataset so well that you can create new data points from it.”
→ They learn the full underlying structure.

Simple example:
“If I show you a picture of a cat, a discriminative model says: ‘Cat.’
A generative model says: ‘Let me draw a new cat.’”

---

## **5. Side-by-Side Comparison (1 minute)**

| Feature        | Discriminative (Predictive) Models | Generative Models                |                 |
| -------------- | ---------------------------------- | -------------------------------- | --------------- |
| Goal           | Predict labels                     | Create new data                  |                 |
| Learns         | P(y                                | x)                               | P(x) or P(x, y) |
| Output         | Category / number                  | Text/images/audio                |                 |
| Example Tasks  | Spam detection, regression         | Text generation, image synthesis |                 |
| Typical Models | Logistic Regression, SVM           | GANs, VAEs, LLMs                 |                 |

---

## **6. Why This Difference Matters (0.5 minute)**

* Predictive models are great for **accuracy** and **classification**
* Generative models are essential for **creativity**, **content creation**, and **automation**
* Modern AI systems often combine both — discriminative for classification and generative for content creation

---

## **7. Summary (0.5 minute)**

* Discriminative → **Predict**
* Generative → **Create**
* Both are essential parts of the AI ecosystem, and understanding the distinction helps you choose the right approach for a given problem.

