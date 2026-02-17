# Understanding Learning Rate

## Concept
The **Learning Rate** (denoted by $\alpha$ or `lr`) is one of the most critical "Hyperparameters" in Machine Learning. It controls the **size of the steps** the algorithm takes when trying to find the best solution (minimum error).

* It does *not* change the direction of the step (the Gradient determines that).
* It determines *how far* we move in that direction.

## Real-World Analogy: The Hiker
Imagine you are hiking down a mountain in thick fog. You want to reach the village in the valley (Global Minimum).
1.  **Tiny Learning Rate:** You take millimeter-sized steps. You will reach the bottom eventually, but it might take 100 years (Too Slow).
2.  **Huge Learning Rate:** You take giant leaps. You might jump right over the valley and land on the opposite peak, or worse, jump higher and higher (Divergence/Overshooting).
3.  **Good Learning Rate:** You take reasonably sized steps that get smaller as you approach the bottom (Convergence).

## Visualization
[Image of three gradient descent paths showing slow convergence perfect convergence and overshooting]

## External Resources
* [Article: Understanding Learning Rate](https://example.com/learning-rate-guide)
* [Video: Effects of Learning Rate](https://example.com/lr-effects-video)
