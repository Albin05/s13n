## Lecture Script: Create Virtual Environments For Projects


---

### CS Theory Bite

> **Origin**: Virtual environments solve **"dependency hell"** — conflicting package versions between projects. **virtualenv** (2007) pioneered this, **venv** (Python 3.3, PEP 405) built it into Python itself.
>
> **Analogy**: Virtual environments are like **separate apartments** — each project has its own space with its own furniture (packages), no conflicts with neighbors.
>
> **Why it matters**: Without virtual environments, installing a package for one project can break another.



### Hook (2 minutes)

You install package X for Project A. Project B needs a different version of X. Both break. Virtual environments solve this — isolated Python per project.

---

### Section 1: Basics (3 minutes)

```bash
# Create
python3 -m venv myenv

# Activate (Mac/Linux)
source myenv/bin/activate

# Activate (Windows)
myenv\\Scripts\\activate

# Deactivate
deactivate
```

---

### Section 2: Key Concepts (3 minutes)

**Why virtual environments?**
- Project A needs Django 3.2, Project B needs Django 4.0
- Without venv: one overwrites the other
- With venv: each project has its own isolated packages

**What's inside a venv?**
- Its own Python binary
- Its own pip
- Its own site-packages directory

---

### Section 3: Practical Usage (3 minutes)

**Workflow:**
```bash
mkdir myproject && cd myproject
python3 -m venv venv
source venv/bin/activate
pip install requests flask
pip freeze > requirements.txt
echo "venv/" >> .gitignore
```

---

### Summary (1 minute)

1. `python -m venv name` to create
2. `source name/bin/activate` to activate
3. `deactivate` to leave
4. One venv per project — always
