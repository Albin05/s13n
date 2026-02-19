# The Sigmoid Function (Theory)

## Conceptual Explanation
In previous lessons, we established that a linear model ($z = \theta^T x$) can output any number from $-\infty$ to $\infty$, which breaks the rules of probability. 

To solve this, we need a mathematical "squishing" function. We need a function that can take any number in the universe and map it to a value strictly between $0$ and $1$. 

The **Sigmoid Function**, also known as the Logistic Function, does exactly this. Its shape is an "S-curve". It perfectly bridges the gap between the unbounded world of continuous lines and the bounded world of probabilities.

## The Formula
The Sigmoid function, denoted by the Greek letter sigma ($\sigma$), is defined as:
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

Where $z$ is the input (in our case, the output of the linear equation $\theta^T x$).

## Short Examples
* If you input $z = 0$, the Sigmoid function outputs exactly $0.5$.
* If you input a large positive number like $z = 10$, the output is extremely close to $1$ (e.g., $0.9999$).
* If you input a large negative number like $z = -10$, the output is extremely close to $0$ (e.g., $0.00004$).

## External Links
* [Khan Academy: Logistic Models](https://www.khanacademy.org/math/algebra2/x2ec2f6f830c9fb89:eq/x2ec2f6f830c9fb89:logistic/v/logistic-function)
* [Towards Data Science: Activation Functions - Sigmoid](https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6)
