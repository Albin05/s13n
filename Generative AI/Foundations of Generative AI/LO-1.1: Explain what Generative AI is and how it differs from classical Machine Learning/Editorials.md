# **LO-1.1 — Generative AI vs Classical ML**

---

# **Q4. Short – Explain Generative AI**

### **1. Title**

Understanding Generative AI in Simple Terms

### **2. Problem Description**

Explain what Generative AI means, focusing on the core idea behind it.

### **3. Objective**

Check whether the learner clearly grasps what makes Generative AI unique.

### **4. Hint**

Think: models that *generate*, not *predict*.

### **5. Short Explanation**

Generative AI models learn patterns from large datasets and use them to create new content (text, images, audio, etc.).

### **6. Detailed Explanation**

Generative AI refers to models that learn the underlying distribution of data — meaning they understand *how* data is structured and what patterns are common.
After learning these patterns, they **generate new data that resembles the training data**.

Examples include:

* creating new text (LLMs),
* generating images (Stable Diffusion),
* producing code, music, or videos.

Unlike classical ML, which focuses on making predictions (e.g., “Is this spam?”), generative AI focuses on **creation** (“Write a formal email replying to this message”).

### **7. Constraints**

No strict constraints; explanation must be conceptually correct.

---

# **Q5. Short – Differences Between Classical ML & GenAI**

### **1. Title**

Comparing Predictive Models with Generative Models

### **2. Problem Description**

List at least two differences between classical ML and Generative AI.

### **3. Objective**

Evaluate conceptual clarity about the functional differences between both paradigms.

### **4. Hint**

Think: *type of output*, *data usage*, *deterministic vs stochastic* behavior.

### **5. Short Explanation**

Classical ML predicts outcomes; Generative AI creates new content.

### **6. Detailed Explanation**

Key differences:

| Aspect            | Classical ML                             | Generative AI                           |
| ----------------- | ---------------------------------------- | --------------------------------------- |
| **Goal**          | Predict/ classify                        | Create new data                         |
| **Output Type**   | Labels, numbers, probabilities           | Text, images, audio, code               |
| **Data Handling** | Works best with structured data          | Excels with large unstructured datasets |
| **Behavior**      | Deterministic (same input → same output) | Stochastic (varied outputs)             |

These differences shape where each category excels in real applications.

### **7. Constraints**

No specific constraints; conceptual accuracy required.

---

# **Q6. Short – Applications of Generative AI**

### **1. Title**

Real-World Use Cases of Generative AI

### **2. Problem Description**

Give two examples where Generative AI is more suitable than classical ML.

### **3. Objective**

Assess ability to connect theoretical understanding with practical scenarios.

### **4. Hint**

Think of tasks where creativity or open-ended outputs are needed.

### **5. Short Explanation**

Generative AI is ideal for generating text, images, audio, code, and conversational responses.

### **6. Detailed Explanation**

Generative AI models can understand context and produce creative or contextually rich content.
Two examples:

#### **1. Marketing Content Creation**

Generating slogans, blog drafts, ads, and product descriptions based on user intent.

#### **2. Conversational Chatbots**

Producing natural, human-like responses instead of selecting predefined replies.

Other valid examples:

* converting rough notes into structured documents,
* generating UI mockups,
* creating synthetic training data.

Classical ML cannot generate content; it only categorizes or predicts.

### **7. Constraints**

None.

---

# **Q7. Short – Why Outputs Vary?**

### **1. Title**

Understanding Output Variability in Generative Models

### **2. Problem Description**

Explain why generative models produce different outputs even with identical inputs.

### **3. Objective**

Test understanding of the probabilistic nature of LLMs.

### **4. Hint**

Think: token probability distribution + sampling methods.

### **5. Short Explanation**

Generative AI uses probabilistic sampling, so each generation can choose a different sequence of tokens.

### **6. Detailed Explanation**

Generative models do not pick the single “best” token; they sample from a *distribution* of possible next tokens.

Key factors:

* **Temperature:** controls randomness
* **Top-k sampling:** restricts choices to k most probable tokens
* **Nucleus sampling (top-p):** selects tokens from a cumulative probability mass

Because of these sampling methods, models explore different valid continuations of the same prompt, leading to natural variation — a key feature for creativity and open-ended tasks.

### **7. Constraints**

None.

---

# **Q8. Long – Detailed Comparison**

### **1. Title**

Deep Comparative Analysis: Classical ML vs Generative AI

### **2. Problem Description**

Compare both paradigms on input requirements, output types, and flexibility.

### **3. Objective**

Assess analysis-level thinking and ability to structure a multi-dimensional comparison.

### **4. Hint**

Don’t only list differences — analyze the consequences of each difference.

### **5. Short Explanation**

Classical ML handles structured, predictive tasks; Generative AI handles creative, flexible content generation.

### **6. Detailed Explanation**

---

### **1. Input Requirements**

**Classical ML:**

* Works best on structured/tabular datasets (rows/columns).
* Requires manual feature engineering.
* Limited when handling unstructured data.

**Generative AI:**

* Trained on massive unstructured datasets (text, images, audio).
* Automatically learns representations.
* Requires high computational power and large-scale data.

---

### **2. Output Type**

**Classical ML:**

* Outputs labels (“spam/no spam”), numbers (“price = 12.4”), or probabilities.
* Outputs are deterministic and predictable.

**Generative AI:**

* Outputs *content*: paragraphs, images, videos, code.
* Outputs may vary each time due to probabilistic sampling.
* Capable of long-form and creative generation.

---

### **3. Flexibility**

**Classical ML:**

* Single-purpose; each model is trained for one task.
* Difficult to generalize beyond its training objective.

**Generative AI:**

* Highly flexible: one model can summarize, translate, code, chat, reason.
* Exhibits emergent abilities.
* Scales to multiple domains without retraining.

---

Generative AI offers broader capabilities but at higher computational and reliability costs.

### **7. Constraints**

None.

---

# **Q9. Long – Customer Support Automation**

### **1. Title**

Choosing the Right Approach for Automating Customer Support

### **2. Problem Description**

Decide whether classical ML or Generative AI fits a conversational support use case.

### **3. Objective**

Test real-world decision-making and ability to justify model selection.

### **4. Hint**

Ask: Does the business need *classification* or actual *conversation*?

### **5. Short Explanation**

Generative AI is more suitable because customer queries require dynamic, context-rich responses.

### **6. Detailed Explanation**

Customer support automation needs:

* natural language understanding,
* multi-turn conversation handling,
* contextual responses,
* adaptability to follow-up questions,
* ability to summarize and interpret past conversation threads.

**Classical ML can only:**

* classify queries (e.g., billing, technical issue),
* detect sentiment,
* route tickets.

It cannot produce responses.

**Generative AI can:**

* generate conversational replies,
* adapt tone (formal/informal),
* handle ambiguity,
* summarize long messages,
* continue a multi-turn dialogue.

Thus, Generative AI provides a full end-to-end conversational experience, making it the superior choice.

### **7. Constraints**

None.

---

# **Q10. Long – Can GenAI Replace Classical ML?**

### **1. Title**

Can Generative AI Replace Classical ML in Analytical Domains?

### **2. Problem Description**

Critically evaluate whether generative AI can take over structured analytical tasks such as fraud detection.

### **3. Objective**

Test evaluation-level thinking with balanced arguments.

### **4. Hint**

Think accuracy, determinism, interpretability, scalability.

### **5. Short Explanation**

Generative AI cannot fully replace classical ML for precision-critical analytical tasks.

### **6. Detailed Explanation**

---

### **Arguments FOR Replacement**

1. Generative models understand complex relationships even in unstructured data.
2. They can simulate reasoning steps and create synthetic examples for rare cases.
3. They can augment analytical pipelines (e.g., generate explanations, rewrite logs).

---

### **Arguments AGAINST Replacement**

1. **Hallucinations:** LLMs can produce incorrect information confidently.
2. **Lack of determinism:** Different outputs each time → bad for regulated industries.
3. **Poor structured accuracy:** Classical ML is statistically superior for tasks like fraud detection, churn prediction, anomaly detection.
4. **Explainability:** Classical ML is more transparent.

---

### **Conclusion**

Generative AI complements classical ML but cannot replace it for structured prediction tasks. They serve different purposes and often work best when combined.

### **7. Constraints**

None.

---

# **Q11. Implementation – Output Variability**

### **1. Title**

Exploring Variations in Generative Model Outputs

### **2. Problem Description**

Load a pre-trained model (e.g., GPT-2, Gemma-2B), give the same prompt, and generate multiple outputs.

### **3. Objective**

Help learners understand **sampling behavior** in generative models.

### **4. Hint**

Experiment with temperature, top-k, or top-p settings.

### **5. Short Explanation**

Generative models sample tokens—so even identical prompts yield different responses.

### **6. Detailed Explanation**

When you run the same prompt multiple times:

* the model calculates a probability distribution over possible next tokens,
* sampling introduces randomness,
* different tokens may be chosen each time,
* these choices propagate through the sentence, creating significant variation.

Walkthrough:

1. Load model → `from transformers import AutoModelForCausalLM`
2. Run prompt with `temperature=0.7`
3. Run again with `temperature=1.2`
4. Compare differences.

Higher randomness → more creative outputs
Lower randomness → more stable outputs

### **7. Constraints / Edge Cases**

* Very high temperature causes incoherent text.
* Very low temperature leads to repetitive responses.

---

# **Q12. Implementation – Classical ML vs GenAI Data Use**

### **1. Title**

Experiment: Synthetic Text vs Classical Prediction

### **2. Problem Description**

Train a classical ML classifier, generate synthetic sentences using a generative model, and classify them.

### **3. Objective**

Observe how structured vs generative approaches interpret and use data differently.

### **4. Hint**

Use logistic regression + a small text dataset (IMDB mini, SMS spam mini, etc.)

### **5. Short Explanation**

Classical ML learns fixed decision boundaries; generative AI creates text without such constraints.

### **6. Detailed Explanation**

Steps:

1. Train a classical ML model (logistic regression/SVM) using bag-of-words or TF-IDF features.
2. Generate 5 synthetic sentences using a generative model based on similar themes.
3. Run the classifier on synthetic text.

Insights:

* The classical model uses rigid, pre-defined features → may misclassify diverse synthetic text.
* Generative AI produces more varied vocabulary, structures, and expressions.
* The classifier may struggle with out-of-distribution text, demonstrating its limitations vs the flexibility of generative models.

### **7. Constraints / Edge Cases**

* Synthetic text may contain unseen words.
* Ensure consistent preprocessing.

---

# **Q13. Implementation – Mini Workflow (Classification + Generation)**

### **1. Title**

Designing a Hybrid GenAI + Classical ML Workflow

### **2. Problem Description**

Build a pipeline where classical ML classifies a sentence and generative AI expands it.

### **3. Objective**

Assess design skills and ability to combine two different ML paradigms.

### **4. Hint**

Think modular:
Step 1 — classify topic
Step 2 — generate paragraph

### **5. Short Explanation**

Classical ML identifies category; generative AI expands contextually.

### **6. Detailed Explanation**

Sample architecture:

1. **Input:** “Bitcoin prices fell today.”
2. **Classical ML:**

   * predicts topic = *Finance*
   * uses logistic regression/Naive Bayes with TF-IDF
3. **Generative Model:**

   * takes topic + original sentence
   * generates a well-structured paragraph

Why this works:

* Classical ML excels at structured classification tasks.
* Generative AI excels at textual expansion and creativity.
* Combining them delivers the best of both worlds: accuracy + expressiveness.

### **7. Constraints / Edge Cases**

* Misclassification leads to wrong expansions → add filters or confidence thresholds.

