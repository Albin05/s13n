# Pre-Read: Learning Data Distributions

## 1. What is a Data Distribution?
<img src="https://coding-platform.s3.amazonaws.com/dev/lms/tickets/d9f12751-5f18-447c-8e38-de1f3b22cf9d/dpEsUMHyg2CwmoDX.png" alt="Distribution Example" />

In statistics, a **distribution** describes how data points are spread out.
*   **Simple Example**: Human heights follow a "Normal Distribution" (Bell Curve). Most people are average height; very few are extremely tall or short.
*   **Complex Example**: Images of faces also follow a distribution, but a much more complex one. It defines the rules of what makes a face a face (e.g., two eyes, one nose, specific skin textures).

## 2. The Core Idea of Generative Learning
Generative AI isn't magic; it's statistics.
*   **Goal**: The model tries to figure out the mathematical formula (distribution) that created the training data.
*   **Training**: The model looks at thousands of examples to approximate this distribution.
*   **Generation**: Once it knows the distribution, it can pick random points from it to create **new** examples that follow the same rules.

## 3. Key Vocabulary
| Term | Definition |
| :--- | :--- |
| **$P_{data}$** | The true probability distribution of real-world data. |
| **$P_{model}$** | The distribution the AI model learns. |
| **Sampling** | The process of generating a new output from the learned distribution. |

## 4. Why is this important?
Understanding distributions is the key to understanding how models like ChatGPT or Midjourney can create infinite variations of content without simply copying what they have seen before.
