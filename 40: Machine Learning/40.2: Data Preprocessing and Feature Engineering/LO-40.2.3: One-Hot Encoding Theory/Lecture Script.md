### Hook (3 min)
Write on board: "1=Red, 2=Blue, 3=Green"
Ask: "What's the average? (1+2+3)/3 = 2"
Ask: "What color is 2?"
Say: "This is why we can't just assign numbers! We need one-hot encoding."

### Main Content (18 min)
**The Problem (4 min)**
- Can't use categories directly
- Bad solution: numbering (1,2,3)
- Why it's bad: false ordering
- Example: hair color

**One-Hot Encoding (8 min)**
- Concept: Separate binary column per category
- Only one "1", rest "0"
- Visual: Light bulb analogy
- Step-by-step transformation
- Hair color example walkthrough

**Benefits & Drawbacks (6 min)**
- Pros: No false order, equal treatment
- Cons: Many columns, sparse data
- When to use / not use
- Real scenarios

### Exercise (2 min)
"One-hot encode:
| Size |
|------|
| S |
| M |
| S |
| L |"

### Wrap-up (2 min)
- Create binary column per category
- One "hot" (1), rest cold (0)
- Solves categorical problem
- Next: Python implementation!
