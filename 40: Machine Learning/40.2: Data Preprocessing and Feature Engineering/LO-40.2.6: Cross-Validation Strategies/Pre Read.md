# Cross-Validation Strategies

## Concept
A single Train-Test split (e.g., 80/20) has a flaw: what if the 20% we chose for testing just happened to be the easiest data points? The model would score high, but fail in the real world. Conversely, what if the test set contained all the hardest points? The model would look terrible unfairly.

**Cross-Validation (CV)** solves this by rotating the data. Instead of one exam, we give the model multiple exams on different parts of the data to get a stable, reliable estimate of performance.

## The Standard Method: K-Fold CV
We split the data into $K$ equal parts (folds).
1.  Train on Folds 1-4, Test on Fold 5. Record Score.
2.  Train on Folds 1,2,3,5, Test on Fold 4. Record Score.
3.  ...Repeat $K$ times.
4.  **Final Score:** The average of all $K$ scores.

## Real-World Analogy: The Tournament
* **Train-Test Split:** A single match. One team might just have a bad day.
* **Cross-Validation:** A league tournament. Every team plays every other team. The winner is the one with the best *average* performance across all games.

## Visualization
!

## External Resources
* [Article: A Gentle Introduction to k-fold Cross-Validation](https://example.com/k-fold-intro)
* [Video: Cross-Validation Visualized](https://example.com/cv-viz-video)
