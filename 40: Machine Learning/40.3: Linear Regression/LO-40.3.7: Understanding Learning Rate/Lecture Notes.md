# Understanding Learning Rate

## Learning Objectives
- Understand what learning rate is
- Recognize why learning rate matters
- Choose appropriate learning rates
- Avoid common pitfalls

## What is Learning Rate?

**Learning Rate (η - eta):** A small number that controls how much we adjust the model parameters in each step.

Think of it as:
- Step size
- Adjustment speed
- How quickly the model learns

**Symbol:** η (Greek letter eta)  
**Typical values:** 0.001, 0.01, 0.1

## Why Do We Need It?

Without learning rate, adjustments might be:
- Too large → Overshoot the target
- Too small → Takes forever to converge

**Learning rate balances speed and stability!**

## The Adjustment Formula

```python
# Without learning rate (BAD)
new_value = old_value + error

# With learning rate (GOOD)
new_value = old_value + η × error

# Example:
old_slope = 5
error = 100
η = 0.01

new_slope = 5 + 0.01 × 100 = 5 + 1 = 6
```

## Visual Analogy: Walking Down a Hill

Imagine you're blindfolded walking down a hill to reach the bottom (minimum error).

### Large Learning Rate (η = 0.5):

```
    Start ●
                     \  Large steps!
            ↓
         ●──────────● Overshooting!
    ↓               ↑
●───────────────────────● Never settles!
        Bottom
```

**Problem:** Steps too big, you overshoot and never reach bottom!

### Small Learning Rate (η = 0.001):

```
Start ●
      ↓ Tiny step
      ●
      ↓ Tiny step
      ●
      ↓ (100 more steps...)
      ●
    Bottom
```

**Problem:** Takes FOREVER to reach bottom!

### Just Right Learning Rate (η = 0.01):

```
Start ●
               \ Reasonable steps
         ↓
         ●
                     ↓
           ● Bottom reached efficiently!
```

**Perfect:** Fast enough but stable!

## Mathematical Example

### Scenario:

```python
# Current line: y = 5x + 10
# Point: (3, 50)
# Predicted: 5(3) + 10 = 25
# Error: 50 - 25 = 25
```

### With Different Learning Rates:

**η = 1.0 (Too Large):**
```python
# Slope adjustment
new_slope = 5 + 1.0 × (25 × 3) = 5 + 75 = 80
# Way too steep! Overshoot!
```

**η = 0.001 (Too Small):**
```python
# Slope adjustment
new_slope = 5 + 0.001 × (25 × 3) = 5 + 0.075 = 5.075
# Barely moved! Will take 1000+ iterations!
```

**η = 0.01 (Just Right):**
```python
# Slope adjustment
new_slope = 5 + 0.01 × (25 × 3) = 5 + 0.75 = 5.75
# Good progress! Stable!
```

## Effect on Training

### Training with η = 0.1 (Good):

```
Error
  │●
50│ ●
  │  ●
25│    ●
  │      ●___
 0│_____________
   0  5  10 15  Iterations

Converges in ~15 iterations!
```

### Training with η = 1.0 (Too Large):

```
Error
  │  ●
50│●   ●
  │      ●
25│●       ●
  │  ●   ●
 0│_____________
   0  5  10 15  Iterations

Never converges! Oscillates!
```

### Training with η = 0.001 (Too Small):

```
Error
  │●
50│ ●
  │  ●
25│   ●
  │    ●
 0│_____________
   0  50 100 150  Iterations

Very slow! Needs 100+ iterations!
```

## Choosing the Right Learning Rate

### Too Large (η > 0.5)

**Symptoms:**
- Error increases instead of decreasing
- Model predictions get worse
- Training unstable, oscillates

**Solution:** Reduce η

### Too Small (η < 0.0001)

**Symptoms:**
- Error decreases very slowly
- Takes many iterations
- Training time too long

**Solution:** Increase η

### Just Right (η ≈ 0.001 - 0.1)

**Symptoms:**
- Error steadily decreases
- Converges in reasonable time
- Stable training

**Success!**

## Common Learning Rate Values

```python
# Very small (for sensitive problems)
η = 0.0001

# Small (conservative, stable)
η = 0.001

# Medium (common default)
η = 0.01

# Larger (faster but riskier)
η = 0.1

# Large (usually too much)
η = 1.0
```

**Rule of thumb:** Start with η = 0.01, adjust based on results.

## Real Training Example

### House Price Prediction:

**Initial:**
```python
η = 0.01
slope = 10  # Random start
intercept = 50000  # Random start
```

**Iteration 1:**
```python
# Point: (2000 sqft, $400k)
predicted = 10 × 2000 + 50000 = $70k
error = 400k - 70k = 330k

# Adjustments
slope = 10 + 0.01 × (330k × 2000) = ...  # Calculated properly
intercept = 50000 + 0.01 × 330k = 53300

# New line: Better!
```

**Iteration 20:**
```python
slope ≈ 95
intercept ≈ 195k
error ≈ $20k  # Much better!
```

**Iteration 100:**
```python
slope ≈ 100
intercept ≈ 200k
error ≈ $2k  # Almost perfect!
```

## Adaptive Learning Rates

Advanced techniques adjust η during training:

### Learning Rate Decay:

```python
# Start large, decrease over time
iteration = 1: η = 0.1
iteration = 10: η = 0.05
iteration = 50: η = 0.01
iteration = 100: η = 0.001
```

**Benefit:** Fast initial progress, fine-tuning at end!

### Adaptive Methods:

- **Adam:** Adjusts η for each parameter
- **RMSprop:** Scales η based on gradient
- **AdaGrad:** Decreases η for frequent updates

We'll learn these in advanced courses!

## Common Mistakes

### Mistake 1: Using η = 1

```python
η = 1  # DON'T DO THIS!
# Usually causes divergence
```

### Mistake 2: Never Adjusting η

```python
# If training not working, try different η!
# Don't just run more iterations with bad η
```

### Mistake 3: Too Different Scales

```python
# Features with very different scales need different η
sqft = 2000 (thousands)
age = 10 (tens)
# Solution: Normalize features first!
```

## Summary

**Learning Rate (η):**
- Controls adjustment step size
- Small number (0.001 - 0.1 typical)
- Balances speed vs stability

**Too Large:**
- Overshoots target
- Unstable training
- Error oscillates or increases

**Too Small:**
- Very slow progress
- Many iterations needed
- Works but inefficient

**Just Right:**
- Steady error decrease
- Reasonable convergence time
- Stable and efficient

**Choosing η:**
- Start with 0.01
- If unstable → decrease
- If too slow → increase
- Monitor error over iterations

**Key Insight:**
Learning rate is like driving speed:
- Too fast → Crash (overshoot)
- Too slow → Never arrive
- Just right → Safe and efficient!

**Next:** We'll see the complete algorithm that uses learning rate!

## Practice

1. What happens if learning rate is too large?

2. Calculate new slope:
```
old_slope = 5
error = 20
η = 0.01
new_slope = ?
```

3. Which learning rate is typically better: 0.001 or 1.0? Why?

4. If your model error oscillates wildly, what should you do to the learning rate?

5. Why do we multiply error by learning rate instead of using error directly?
