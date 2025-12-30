## Lecture Notes: Creating and Initializing Sets

### Creating Sets
- Curly braces: `{1, 2, 3}`
- Constructor: `set([1, 2, 3])`
- Empty: `set()` not `{}`

### Unique Values
- Automatic deduplication
- `set([1, 2, 2, 3])` → `{1, 2, 3}`

### Restrictions
- Elements must be immutable
- No lists/dicts/sets as elements
- Use tuples instead

### Common Uses
- Remove duplicates
- Unique tracking
- Fast membership testing
