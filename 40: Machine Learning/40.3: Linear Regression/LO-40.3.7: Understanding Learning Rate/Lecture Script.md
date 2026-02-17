# Lecture Script: Understanding Learning Rate

## Topic Breakdown

### 1. Why is this number so important?
* **Instructor Note:** Draw a U-shaped curve. Start a point at the top left.
* **Why:** If you pick the wrong Learning Rate, your model simply won't learn.
    * Too small: You wait forever.
    * Too big: The error actually *increases* (Exploding Gradients).
    * This is often the first thing we tune when a model fails.

### 2. The Goldilocks Zone
* **Small $\alpha$ (e.g., 0.00001):**
    * Safe, but inefficient. The loss curve goes down very, very slowly.
* **Large $\alpha$ (e.g., 10.0):**
    * Dangerous. The loss curve bounces up and down or goes to infinity (`NaN`).
* **Just Right $\alpha$ (e.g., 0.01 or 0.1):**
    * Steady, rapid decrease in loss.

### 3. How do we implement it?
* **Method:** It's a simple multiplier in the update rule.
* **Code Example:**
    Simulating 3 different hikers.

    ```python
    def descent(start_w, learning_rate, steps=10):
        w = start_w
        path = []
        for _ in range(steps):
            # Gradient of w^2 is 2w
            grad = 2 * w
            w = w - (learning_rate * grad)
            path.append(w)
        return path

    # 1. Too Small
    print("Small:", descent(10, 0.001)) 
    # Output: 9.98, 9.96... (Barely moved)

    # 2. Too Big
    print("Big:", descent(10, 1.1))
    # Output: -12, +14, -16... (Getting worse!)

    # 3. Good
    print("Good:", descent(10, 0.1))
    # Output: 8, 6.4, 5.1... (Converging to 0)
    ```

* **Visual Aid:**
    [Image of loss vs epochs graph for different learning rates]

* **Demo URL:**
    [TensorFlow Playground](https://playground.tensorflow.org/) - *Change the Learning Rate dropdown and watch the training speed.*
