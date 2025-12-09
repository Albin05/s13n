# **Pre-Read: Predictive (Discriminative) vs Generative Models**

## **1. What Are Discriminative (Predictive) Models?**

<img src="https://coding-platform.s3.amazonaws.com/dev/lms/tickets/4f7a4e64-cc30-4e26-8b41-91d2b69da19c/discriminative.png" alt="image" />

Discriminative models focus on **predicting labels or outcomes** based on input data.
They learn the **boundary** between different classes.

Examples:

* Predicting whether an email is spam
* Sentiment analysis on reviews
* Predicting house prices
* Classifying images (cat vs dog)

**Key idea:**
They learn **P(y | x)** → the probability of label *y* given input *x*.

---

## **2. What Are Generative Models?**

<img src="https://coding-platform.s3.amazonaws.com/dev/lms/tickets/94a98241-89f7-4db9-994f-a829f8b99f77/generative.png" alt="image" />

Generative models focus on **creating new data** similar to the training data.
They learn the **underlying patterns** or **distribution** of the data.

Examples:

* Generating images (Midjourney, Stable Diffusion)
* Writing text (ChatGPT, Gemini)
* Producing audio/music
* Creating code snippets

**Key idea:**
They learn **P(x)** or **P(x, y)** → the probability distribution of the data.

---

## **3. Discriminative vs Generative Models**

| Feature          | Discriminative (Predictive)    | Generative                        |                 |
| ---------------- | ------------------------------ | --------------------------------- | --------------- |
| What they learn  | Boundary between classes       | Data distribution                 |                 |
| Core probability | P(y                            | x)                                | P(x) or P(x, y) |
| Output type      | Label, score, number           | New data/content                  |                 |
| Example tasks    | Spam detection, classification | Image generation, text generation |                 |
| Typical models   | Logistic Regression, SVM       | GANs, VAEs, LLMs                  |                 |

---

## **4. Why This Difference Matters**

* Discriminative models → **Accurate predictions**
* Generative models → **Creative outputs**
* Helps choose the right model for real-world tasks
* Forms the foundation for understanding modern AI systems (LLMs, diffusion models, GANs)
