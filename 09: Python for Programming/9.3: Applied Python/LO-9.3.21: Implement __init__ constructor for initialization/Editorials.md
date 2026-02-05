## Editorials: Implement __init__ Constructor

---

### Q1 Solution

```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * radius ** 2
        self.circumference = 2 * math.pi * radius

c = Circle(5)
print(f"Area: {c.area:.2f}")              # Area: 78.54
print(f"Circumference: {c.circumference:.2f}")  # Circumference: 31.42
```

---

### Q2 Solution

```python
class Config:
    def __init__(self, host="localhost", port=8080, debug=False):
        self.host = host
        self.port = port
        self.debug = debug

c1 = Config()
c2 = Config("0.0.0.0", 3000, True)
c3 = Config(debug=True)

print(f"{c1.host}:{c1.port}")  # localhost:8080
print(f"{c2.host}:{c2.port}")  # 0.0.0.0:3000
print(f"Debug: {c3.debug}")    # Debug: True
```

---

### Q3 Solution

```python
class Temperature:
    def __init__(self, celsius):
        if celsius < -273.15:
            raise ValueError("Below absolute zero")
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32

t = Temperature(100)
print(t.to_fahrenheit())  # 212.0

try:
    Temperature(-300)
except ValueError as e:
    print(e)  # Below absolute zero
```

---

### Q4 Solution

```python
class Team:
    def __init__(self, name, *members):
        self.name = name
        self.members = list(members)

    def add_member(self, name):
        self.members.append(name)

    def __len__(self):
        return len(self.members)

t = Team("Dev", "Alice", "Bob")
t.add_member("Carol")
print(len(t))        # 3
print(t.members)     # ['Alice', 'Bob', 'Carol']
```

---

### Q5 Solution

```python
class DataFrame:
    def __init__(self, data):
        if isinstance(data, dict):
            self._data = data
        elif isinstance(data, list) and data:
            keys = data[0].keys()
            self._data = {k: [row[k] for row in data] for k in keys}
        else:
            self._data = {}

    def columns(self):
        return list(self._data.keys())

    def rows(self):
        if not self._data:
            return []
        cols = self.columns()
        n = len(self._data[cols[0]])
        return [{c: self._data[c][i] for c in cols} for i in range(n)]

# From dict of lists
df1 = DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
print(df1.rows())

# From list of dicts
df2 = DataFrame([{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}])
print(df2.columns())  # ['name', 'age']
```

