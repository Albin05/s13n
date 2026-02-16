# Lecture Notes: Dimensionality Reduction with PCA

## The Problem: High Dimensions
* **Visualization:** Impossible beyond 3D.
* **Computation:** Algorithms (like KNN) slow down exponentially.
* **Overfitting:** Models memorize sparse data points instead of learning structure.

## The Solution: PCA
PCA rotates the data to align with the directions of greatest variance.

### Steps of PCA
1.  **Standardization:** Scale data so features with large ranges (e.g., Salary) don't dominate features with small ranges (e.g., Age).
2.  **Covariance Matrix Computation:** Understand how variables vary together.
3.  **Eigendecomposition:** Find Eigenvectors (Principal Directions) and Eigenvalues (Amount of Variance).
4.  **Selection:** Choose the top $k$ Eigenvectors that capture, say, 95% of variance.
5.  **Projection:** Transform the original data onto these new axes.

### Explained Variance
* **Eigenvalue:** Represents the magnitude of variance in that direction.
* **Explained Variance Ratio:** The percentage of the dataset's total variance captured by a specific Principal Component.
    $$\text{Ratio}_i = \frac{\lambda_i}{\sum \lambda}$$

## Visualization
!

## Important Note
PCA results in **loss of interpretability**. The new features (PC1, PC2) are linear combinations of original features (e.g., $0.5 \times \text{Age} - 0.2 \times \text{Salary}$), which generally have no physical meaning.
