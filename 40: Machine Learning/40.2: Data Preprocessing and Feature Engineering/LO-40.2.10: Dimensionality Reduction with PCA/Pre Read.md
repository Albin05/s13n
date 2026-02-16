# Dimensionality Reduction with PCA

## Concept
In many Machine Learning problems, datasets have dozens, hundreds, or even thousands of features (columns). This leads to the **Curse of Dimensionality**, where models become slow, prone to overfitting, and hard to visualize.

**Principal Component Analysis (PCA)** is a technique to reduce the number of dimensions (features) while preserving as much "information" (variance) as possible. It transforms the original features into a new set of uncorrelated features called **Principal Components**.

## Real-World Analogy: The Shadow
Imagine a 3D object, like a teapot. You want to take a 2D photograph (reduce dimensions from 3D to 2D) that best represents the object.
* If you take a photo from the top, it might look like a circle (bad representation, low variance).
* If you take a photo from the side, you see the handle, spout, and body (good representation, high variance).
* PCA effectively finds the "angle" that captures the most detail (variance) of the data.


## External Resources
* [Article: PCA Explained Visually](https://setosa.io/ev/principal-component-analysis/)
* [Video: StatQuest: PCA clearly explained](https://www.youtube.com/watch?v=FgakZw6K1QQ)


