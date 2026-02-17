## Lecture Script: Install External Packages Using Pip


---

### CS Theory Bite

> **Origin**: **pip** (2008) installs from **PyPI** (Python Package Index, 2003) — a repository of 500K+ packages. The name "pip" recursively stands for "pip installs packages."
>
> **Analogy**: pip + PyPI is like an **app store for code** — search, install, and update packages with one command.
>
> **Why it matters**: The Python ecosystem's strength is its packages — pip is how you access that power.



### Hook (2 minutes)

Someone shares their Python project. You run it and get ImportError for 10 packages. You need pip — Python's package installer.

---

### Section 1: Basics (3 minutes)

```bash
pip install requests          # Install package
pip install requests==2.28.0  # Specific version
pip uninstall requests        # Remove
pip list                      # Show installed
pip freeze > requirements.txt # Save deps
pip install -r requirements.txt # Install from file
```

---

### Section 2: Key Concepts (3 minutes)

**Version specifiers:**
```
requests==2.28.0   # Exact version
requests>=2.28.0   # Minimum version
requests~=2.28.0   # Compatible (2.28.x)
requests!=2.27.0   # Exclude version
```

---

### Section 3: Practical Usage (3 minutes)

**Best practices:**
1. Always use virtual environments
2. Pin versions in requirements.txt
3. Use `pip install --upgrade pip` regularly
4. Check for vulnerabilities: `pip audit`

---

### Summary (1 minute)

1. `pip install` to add packages
2. `pip freeze > requirements.txt` to save dependencies
3. `pip install -r requirements.txt` to reproduce environment
4. Always use virtual environments with pip
