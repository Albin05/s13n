# Lecture Script: Dimensionality Reduction with PCA

## Topic Breakdown

### 1. Why do we need Dimensionality Reduction?
* **Instructor Note:** Ask students if they would rather analyze a spreadsheet with 3 columns or 3,000 columns.
* **Why:** High-dimensional data is computationally expensive and sparse. Distances between points become meaningless (Curse of Dimensionality). We need to compress the data without losing the "story" it tells.

### 2. What is PCA?
* **Definition:** An unsupervised linear transformation technique.
* **Core Idea:** It finds new axes (Principal Components) along which the data varies the most.
    * **PC1:** The direction of maximum variance.
    * **PC2:** The direction of second-most variance, orthogonal (90°) to PC1.
* **Key Concept:** Variance = Information. If a feature has zero variance (all values are the same), it holds zero information. PCA maximizes variance preservation.

### 3. How do we perform PCA?
* **Step 1:** Standardize the data (Mean = 0, Variance = 1). *Crucial!*
* **Step 2:** Compute Covariance Matrix.
* **Step 3:** Calculate Eigenvectors (directions) and Eigenvalues (magnitude/importance).
* **Step 4:** Sort Eigenvectors by Eigenvalues and pick top $k$.
* **Step 5:** Project data onto new axes.

* **Code Example:**
    Using Scikit-Learn.

    ```python
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    import pandas as pd

    # Sample Data (High correlation between Height and Weight)
    data = [[170, 65, 25], [180, 80, 30], [160, 55, 22]]
    
    # 1. Standardize
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # 2. Apply PCA
    # Reduce from 3 dimensions to 2
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(scaled_data)

    print("New Shape:", principal_components.shape)
    print("Explained Variance Ratio:", pca.explained_variance_ratio_)
    # Output might be [0.95, 0.04], meaning PC1 captures 95% of info.
    ```

* **Visual Aid:**
    !

* **Demo URL:**
    [Visualizing PCA in 3D](https://projector.tensorflow.org/)
