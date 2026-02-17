# Moving Lines - Adjusting Slope and Intercept

## Concept
Training a Linear Regression model is essentially the process of moving a straight line until it fits the data points as closely as possible. We do this by adjusting two specific "knobs":

1.  **The Intercept Knob ($c$ or $\theta_0$):**
    * **Action:** Shifts the entire line **Up or Down**.
    * **Effect:** Changes the baseline prediction. If your line is consistently underestimating everyone's salary by $10k, increasing the intercept fixes this.
    * *Analogy:* Using an elevator. The floor angle stays flat, but you move up/down.

2.  **The Slope Knob ($m$ or $\theta_1$):**
    * **Action:** Rotates the line **Clockwise or Counter-Clockwise**.
    * **Effect:** Changes the sensitivity. If your line is too flat (predicting everyone earns roughly the same regardless of experience), increasing the slope makes the prediction more sensitive to experience.
    * *Analogy:* A seesaw. The pivot point stays fixed, but the angle changes.

## Visualization
[Image of graph showing the effect of increasing and decreasing slope and intercept on a line]

## Real-World Analogy: Tuning a Radio
* **Intercept:** The Volume dial. It makes everything louder (shifts up) or quieter (shifts down).
* **Slope:** The Tuning dial. It searches for the signal (rotates) until the static disappears and the music (data pattern) is clear.

## External Resources
* [Interactive: Line Fitting Simulation](https://phet.colorado.edu/en/simulations/least-squares-regression)
* [Video: Visualizing Slope and Intercept](https://www.youtube.com/watch?v=zJg2y02V71Q)
