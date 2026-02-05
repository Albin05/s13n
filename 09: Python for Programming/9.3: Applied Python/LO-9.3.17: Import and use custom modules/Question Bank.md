## Question Bank: Import and Use Custom Modules

---

### Q1: Create and Import a Module (3 minutes, Low Difficulty)
Create a module `mathutils.py` with functions add, subtract, multiply, divide. Import and use it from another file.

**Key Concepts:** Creating modules, import statement

---

### Q2: Import Styles (3 minutes, Low Difficulty)
Show 5 ways to import from a module: `import module`, `from module import func`, `from module import *`, `import module as alias`, `from module import func as alias`. Explain trade-offs.

**Key Concepts:** Import variations

---

### Q3: Package Structure (5 minutes, Medium Difficulty)
Create a package `shapes/` with modules `circle.py` and `rectangle.py`, each with area and perimeter functions. Include `__init__.py` to simplify imports.

**Key Concepts:** Packages, __init__.py

---

### Q4: Module Search Path (5 minutes, Medium Difficulty)
Explain how Python finds modules: current dir, PYTHONPATH, standard library, site-packages. Demonstrate adding a custom path with sys.path.

**Key Concepts:** sys.path, module resolution

---

### Q5: Reusable Utility Module (5 minutes, Medium Difficulty)
Build a `validators.py` module with functions: validate_email, validate_phone, validate_age, validate_password. Include a `__name__ == "__main__"` block for testing.

**Key Concepts:** __name__ guard, module design
