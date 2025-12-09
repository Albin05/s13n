# **Lecture Script (Duration: 10 Minutes)**

### **Title: What is Generative AI & How Does It Differ from Classical ML?**

---

## **1. Introduction (1 minute)**

“Today we’ll understand *what Generative AI actually is* and how it differs from the classical ML systems you’ve seen before — like spam filters, loan prediction, or image classification.”

---

## **2. Classical Machine Learning — Quick Recap (2 minutes)**

“Classical ML focuses on **predictions** based on historical patterns.”

Examples:

* Predict whether an email is spam → Classification
* Predict house price → Regression
* Recommend products → Recommendation systems

Key characteristics:

* Input **→** model **→** a single output label/number
* Bound by the patterns inside the dataset
* Can’t create new content
* Optimizes for accuracy or minimizing error

Analogy:
“Classical ML is like a strict accountant — it memorizes patterns and gives a precise output.”

---

## **3. Generative AI — What it Means (2.5 minutes)**

“Generative AI does not just predict — it *creates*.”

It can generate:

* Text
* Images
* Code
* Audio
* Videos
* 3D objects

Examples:

* ChatGPT generating answers
* Midjourney generating images
* GitHub Copilot generating code

Key characteristics:

* Learns the **distribution** of data
* Produces new outputs that look like the training data but are not copies
* Works using *large-scale neural networks*, especially Transformers

Analogy:
“Generative AI is like a creative writer — it has read billions of examples and can create new, original content.”

---

## **4. How Generative AI Works (Intuition Only) (2 minutes)**

* It does *not* understand like humans
* It predicts the **next likely token** (word/pixel/sound)
* Repeats this millions of times to create full output
* Powered by:

  * Transformers
  * Attention mechanism
  * Large datasets
  * GPUs/TPUs

Simple explanation:
“If I say ‘Once upon a…’, your brain predicts the next word: ‘time’.
LLMs do the same — but at massive scale.”

---

## **5. Classical ML vs Generative AI (1 minute)**

| Feature        | Classical ML                            | Generative AI                       |
| -------------- | --------------------------------------- | ----------------------------------- |
| Output         | Prediction                              | Creation                            |
| Examples       | Spam detection, fraud detection         | ChatGPT responses, image generation |
| Data Use       | Learns decision boundaries              | Learns full data distribution       |
| Creativity     | None                                    | High                                |
| Typical Models | SVM, Random Forest, Logistic Regression | LLMs, Diffusion Models, GANs        |

---

## **6. Why Generative AI is Revolutionizing Everything (0.5 minute)**

* Can automate cognitive tasks
* Works across all domains: coding, design, writing, analytics
* Faster innovation cycles
* Human-AI collaboration → “co-pilot” era

---

## **7. Summary (0.5 minute)**

* Classical ML predicts
* Generative AI creates
* Both coexist; generative builds on classical ML foundations

---