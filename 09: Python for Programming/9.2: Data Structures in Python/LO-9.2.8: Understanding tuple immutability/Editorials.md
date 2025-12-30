## Editorials: Understanding Tuple Immutability

### Q1 Solution: Testing Immutability

```python
data = (10, 20, 30, 40, 50)

# 1. Try to change element
print("Attempting data[2] = 999:")
try:
    data[2] = 999
except TypeError as e:
    print(f"  TypeError: {e}")

# 2. Try to append
print("\nAttempting data.append(60):")
try:
    data.append(60)
except AttributeError as e:
    print(f"  AttributeError: {e}")

# 3. Try to remove
print("\nAttempting data.remove(30):")
try:
    data.remove(30)
except AttributeError as e:
    print(f"  AttributeError: {e}")

# 4. Concatenate (creates new tuple)
new_data = data + (60, 70)
print(f"\nConcatenation: {new_data}")
print(f"Original unchanged: {data}")

# 5. Create modified copy using slicing
modified = data[:2] + (999,) + data[3:]
print(f"\nModified copy: {modified}")
print(f"Original still: {data}")
```

**Key Concepts:**
- Tuples don't have modify methods (append, remove, etc.)
- Cannot assign to indices
- Can create NEW tuples through concatenation
- Slicing and concatenation preserve original

---

### Q2 Solution: Shallow Immutability

```python
container = (1, 2, [3, 4, 5], 6)

# 1. Try to change container[0]
print("Attempting container[0] = 100:")
try:
    container[0] = 100
except TypeError as e:
    print(f"  TypeError: {e}")

# 2. Try to replace list
print("\nAttempting container[2] = [7, 8, 9]:")
try:
    container[2] = [7, 8, 9]
except TypeError as e:
    print(f"  TypeError: {e}")

# 3. Modify the list inside
print("\nAppending to container[2]:")
container[2].append(6)
print(f"  Success! container[2].append(6) works")
print(f"  Container is now: {container}")

# 4. Modify list element
print("\nModifying container[2][0]:")
container[2][0] = 999
print(f"  Success! container[2][0] = 999 works")
print(f"  Container is now: {container}")

print("\nExplanation: The tuple structure is immutable (cannot reassign elements),")
print("but the mutable objects INSIDE can still be modified.")
```

**Key Concept:**
- Tuple's structure is immutable
- Objects inside can be mutable
- Can modify mutable objects, just can't reassign tuple elements

---

### Q3 Solution: Hashability and Dictionary Keys

```python
# 1. Create game map
game_map = {
    (0, 0): 'Start',
    (5, 3): 'Enemy',
    (10, 7): 'Treasure',
    (3, 9): 'Trap'
}
print(f"Game Map created with {len(game_map)} locations\n")

# 2. Move function
def move_player(position, direction):
    x, y = position
    if direction == 'up':
        return (x, y + 1)
    elif direction == 'down':
        return (x, y - 1)
    elif direction == 'left':
        return (x - 1, y)
    elif direction == 'right':
        return (x + 1, y)
    return position

# 3. Navigate
position = (0, 0)
print(f"Starting at {position}: {game_map.get(position, 'Empty')}\n")

moves = ['right', 'right', 'up', 'up', 'up', 'right', 'right', 'right']
for move in moves:
    position = move_player(position, move)
    location = game_map.get(position, 'Empty')
    print(f"Move {move} to {position}: {location}")

print(f"\nPath complete! Found: {game_map.get(position)} at {position}\n")

# 5. Try list as key
print("Attempting to use list as key:")
try:
    test_map = {[0, 0]: 'value'}
except TypeError as e:
    print(f"TypeError: {e}")
    print("Lists cannot be dictionary keys because they are mutable.")
    print("Tuples work because they are immutable and hashable.")
```

**Key Points:**
- Tuples are hashable → can be dict keys
- Perfect for coordinates, composite keys
- Lists are unhashable → cannot be dict keys

---

### Q4 Solution: Configuration Management

```python
# Database config tuple
DB_CONFIG = (
    'postgresql',     # db_type
    'localhost',      # host
    5432,             # port
    'production_db',  # database
    True              # ssl_enabled
)

# 1. Get connection string
def get_connection_string(config):
    db_type, host, port, database, ssl_enabled = config
    ssl = "?ssl=true" if ssl_enabled else ""
    return f"{db_type}://{host}:{port}/{database}{ssl}"

# 2. Update config (returns new tuple)
def update_config(config, **kwargs):
    db_type, host, port, database, ssl_enabled = config
    
    # Update only provided values
    db_type = kwargs.get('db_type', db_type)
    host = kwargs.get('host', host)
    port = kwargs.get('port', port)
    database = kwargs.get('database', database)
    ssl_enabled = kwargs.get('ssl_enabled', ssl_enabled)
    
    return (db_type, host, port, database, ssl_enabled)

# 3. Demonstrate immutability
print(f"Original config: {DB_CONFIG}")
print(f"Connection string: {get_connection_string(DB_CONFIG)}\n")

# Update host
new_config = update_config(DB_CONFIG, host='db.example.com')
print(f"Updated config (new host): {new_config}")
print(f"Original unchanged: {DB_CONFIG}\n")

# Update multiple values
new_config2 = update_config(DB_CONFIG, port=3306, database='test_db')
print(f"Updated config (port and db): {new_config2}")
print(f"Original still unchanged: {DB_CONFIG}\n")

# 4. Try to modify original
print("Attempting to modify original:")
try:
    DB_CONFIG[1] = 'wrong_host'
except TypeError as e:
    print(f"TypeError: {e}")
    print("✓ Original config is protected!\n")

# 5. Compare with mutable list
print("Danger with mutable list:")
list_config = list(DB_CONFIG)
print(f"List config: {list_config}")
list_config[0] = 'WRONG'
print(f"Accidental modification: {list_config}")
print("✗ Original config was corrupted!\n")

print("Conclusion: Immutable tuples prevent accidental config corruption.")
```

**Benefits:**
- Configuration cannot be accidentally modified
- Updates create new config (functional programming)
- Original always preserved
- Thread-safe

---

### Q5 Solution: Caching with Tuples

```python
# Cache and stats
cache = {}
stats = {'hits': 0, 'misses': 0}

def expensive_calculation(a, b, c):
    """Simulates expensive computation"""
    return (a ** 2) + (b ** 3) + (c ** 4)

def cached_calculation(a, b, c):
    key = (a, b, c)  # Tuple as cache key
    
    if key in cache:
        stats['hits'] += 1
        print(f"  Cache HIT! Returning cached value")
        return cache[key]
    else:
        stats['misses'] += 1
        print(f"  Cache MISS - computing...")
        result = expensive_calculation(a, b, c)
        cache[key] = result
        return result

def cache_stats_display():
    total = stats['hits'] + stats['misses']
    hit_rate = (stats['hits'] / total * 100) if total > 0 else 0
    print(f"\nCache Statistics:")
    print(f"  Total calls: {total}")
    print(f"  Cache hits: {stats['hits']}")
    print(f"  Cache misses: {stats['misses']}")
    print(f"  Hit rate: {hit_rate:.1f}%")

print("Cache initialized\n")

# Test calls
test_cases = [
    (2, 3, 4),
    (1, 2, 3),
    (2, 3, 4),  # Should hit
    (1, 2, 3),  # Should hit
    (5, 6, 7)
]

for args in test_cases:
    print(f"Call cached_calculation{args}:")
    result = cached_calculation(*args)
    print(f"  Result: {result}")
    print(f"  Cache now has {len(cache)} {'entry' if len(cache) == 1 else 'entries'}\n")

cache_stats_display()

# Try list as key
print("\nAttempting to use list [2, 3, 4] as cache key:")
try:
    test_cache = {}
    test_cache[[2, 3, 4]] = 'value'
except TypeError as e:
    print(f"TypeError: {e}\n")
    print("Explanation: Lists cannot be dictionary keys because:")
    print("  1. Lists are mutable (can change)")
    print("  2. Mutable objects cannot be hashed")
    print("  3. Dictionary keys must be hashable")
    print("  4. Tuples are immutable and hashable - perfect for caching!")
```

**Caching Pattern:**
- Use tuple of arguments as key
- Immutable = safe cache key
- Hashable = can be dict key
- Common in memoization, dynamic programming

**Key Takeaways:**
- Immutability enables safe caching
- Tuples perfect for composite keys
- Lists fail as keys (unhashable)
- Pattern used in real optimization
