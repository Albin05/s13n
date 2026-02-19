# Understanding Exponential Functions

## Conceptual Explanation
An exponential function is a mathematical function where the variable is located in the exponent. In machine learning, we almost exclusively deal with the **natural exponential function**, denoted as $e^x$. 

Here, the base is Euler's number ($e$), a mathematical constant approximately equal to $2.71828$. The function is written as $f(x) = e^x$.

**Critical Properties:**
1.  **Always Positive:** No matter what real number you plug in for $x$ (even $-1,000,000$), the output $e^x$ is always a positive number.
2.  **Growth vs. Decay:**
    * If $x > 0$, the function grows incredibly fast (Exponential Growth).
    * If $x < 0$, the function approaches zero but never touches it (Exponential Decay).
3.  **The Zero Exponent:** Like any non-zero number, $e^0 = 1$.

## Short Examples
* $e^0 = 1$
* $e^1 \approx 2.718$
* $e^{-1} = \frac{1}{e^1} \approx 0.367$
* $e^{-10} = \frac{1}{e^{10}} \approx 0.000045$ (Very close to zero, but still positive)

## External Links
* [Khan Academy: Exponential Growth and Decay](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:exponential-growth-decay)
* [NumPy Documentation: np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html)
