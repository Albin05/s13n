# Question Bank: PCA

## Q1 (MCQ)
**Problem:** Which linear algebra concept is fundamental to finding the Principal Components in PCA?
A. Integration
B. Eigendecomposition (Eigenvalues and Eigenvectors)
C. Fourier Transform
D. Derivatives

## Q2 (Coding)
**Problem:** You have a dataset `X`. Write a Python snippet using `sklearn` to standardise `X` and then apply PCA to reduce it to preserve 95% of the variance (hint: `n_components` can be a float). Print the number of components chosen.

## Q3 (NAT)
**Problem:** A dataset has 3 eigenvalues: $\lambda_1 = 4.5$, $\lambda_2 = 1.5$, $\lambda_3 = 0.5$. What is the Explained Variance Ratio of the first Principal Component (PC1)? (Round to 2 decimal places).

## Q4 (MSQ)
**Problem:** Select all statements that are TRUE about PCA.
A. Principal Components are always orthogonal (perpendicular) to each other.
B. PCA is a Supervised Learning technique (uses labels).
C. The first Principal Component captures the maximum possible variance.
D. PCA is reversible (you can reconstruct exact original data from reduced components).

## Q5 (Coding)
**Problem:** Write a function `get_feature_importance(pca_model, feature_names)` that returns a DataFrame showing the weights (loadings) of original features for the first Principal Component (`components_[0]`), sorted by absolute magnitude.

## Q6 (Subjective)
**Problem:** Explain the trade-off involved in PCA. If we reduce a 100-dimensional dataset to 2 dimensions for visualization, what do we gain, and what exactly do we lose?
