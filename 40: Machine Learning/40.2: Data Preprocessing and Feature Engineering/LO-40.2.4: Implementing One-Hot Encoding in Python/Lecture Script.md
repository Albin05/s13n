### Hook (3 min)
Show DataFrame with categories
Ask: "Can we train a model on this?"
Response: "No, need numbers"
Say: "Let's convert it! Live coding time."

### Main Content (18 min)
**Basic Implementation (6 min)**
- Import pandas
- Create sample DataFrame
- pd.get_dummies() basic syntax
- Show before/after
- Explain output

**Advanced Options (6 min)**
- Custom prefix
- drop_first parameter
- Why drop first?
- Multiple columns at once
- Real employee example

**ML Pipeline (6 min)**
- Complete example: data to model
- Check correlations
- Handle train/test split
- Common pitfalls
- New categories problem

### Exercise (2 min)
"Encode this data:
```python
df = pd.DataFrame({
    'Animal': ['Cat', 'Dog', 'Bird', 'Cat'],
    'Count': [2, 3, 1, 4]
})
```
"

### Wrap-up (2 min)
- pd.get_dummies() is main tool
- Specify columns parameter
- Check result before ML
- Handle edge cases
