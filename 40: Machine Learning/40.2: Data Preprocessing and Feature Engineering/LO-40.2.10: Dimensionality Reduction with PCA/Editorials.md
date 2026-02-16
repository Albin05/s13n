
# Editorials

## Q1
### Title
Mathematical Foundation of PCA

### Problem Description
Identify the math concept behind PCA.

### Objective
Link linear algebra to ML algorithms.

### Hint
It involves vectors that don't change direction during transformation.

### Short Explanation
PCA relies on Eigendecomposition of the Covariance Matrix to find directions of max variance.

### Detailed Explanation
* PCA calculates the Covariance Matrix of the data.
* It then finds the **Eigenvectors** (which point in the direction of spread) and **Eigenvalues** (which indicate the magnitude of spread).
* Answer: B.

---

## Q2
### Title
PCA with Variance Threshold

### Problem Description
Reduce dimensions to keep 95% variance.

### Objective
Use `n_components` as a float ratio.

### Hint
Set `n_components=0.95`.

### Short Explanation
Standardize first, then init PCA with float.

### Detailed Explanation
```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=0.95) # Keep 95% info
X_pca = pca.fit_transform(X_scaled)

print(pca.n_components_) # Number of components selected

```

---

## Q3

### Title

Calculating Explained Variance

### Problem Description

Calculate ratio given eigenvalues: 4.5, 1.5, 0.5.

### Objective

Understand the relationship between eigenvalues and information.

### Hint

Ratio = Specific Eigenvalue / Sum of All Eigenvalues.

### Short Explanation

Sum = . PC1 Ratio = .

### Detailed Explanation

1. **Total Variance (Sum of Eigenvalues):** .
2. **PC1 Variance:** .
3. **Ratio:** 
4. **Rounded:** 0.69.

---

## Q4

### Title

Properties of PCA

### Problem Description

Select true statements about PCA.

### Objective

Verify theoretical understanding.

### Hint

PCA looks at  only, no . Components are independent.

### Short Explanation

A and C are true. B is false (Unsupervised). D is false (Lossy compression).

### Detailed Explanation

* **A (True):** PCs are mathematically orthogonal.
* **B (False):** PCA does not look at labels (); it is Unsupervised.
* **C (True):** PC1 is defined as the direction of max variance.
* **D (False):** If you drop components (e.g., from 100 to 2), you lose the information in those dropped components. You cannot reconstruct the *exact* original data.

---

## Q5

### Title

Feature Loadings

### Problem Description

Extract feature weights for PC1.

### Objective

Interpret "Black Box" PCA components.

### Hint

Use `pca.components_`.

### Short Explanation

Map feature names to `pca.components_[0]`.

### Detailed Explanation

```python
import pandas as pd
import numpy as np

def get_feature_importance(pca_model, feature_names):
    # components_ is shape (n_components, n_features)
    pc1_weights = pca_model.components_[0]
    
    df = pd.DataFrame({
        'Feature': feature_names,
        'Weight': pc1_weights,
        'Abs_Weight': np.abs(pc1_weights)
    })
    
    return df.sort_values(by='Abs_Weight', ascending=False)

```

---

## Q6

### Title

The PCA Trade-off

### Problem Description

Discuss Gains vs Losses in dimensionality reduction.

### Objective

Critically analyze the utility of the technique.

### Hint

We gain simplicity/speed. We lose detail/nuance.

### Short Explanation

**Gain:** Computational efficiency (faster training), ability to visualize (2D plots), noise reduction (ignoring small variance components), prevention of overfitting.
**Lose:** Information (variance) contained in the discarded dimensions. We also lose **Interpretability**—original features like "Age" are lost and replaced by abstract "Component 1" values.

```

```
