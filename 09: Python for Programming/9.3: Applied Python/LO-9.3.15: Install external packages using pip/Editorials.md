## Editorials: Install External Packages Using Pip

---

### Q1 Solution

```bash
pip install requests           # Latest
pip install requests==2.28.0   # Exact
pip uninstall requests         # Remove
pip list                       # List all
pip show requests              # Show info
```

---

### Q2-Q5: See Question Bank for problems. Key patterns:

- Always use virtual environments with pip
- Pin versions for reproducibility
- Use `pip freeze > requirements.txt`
