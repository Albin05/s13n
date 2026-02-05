## Pre-Read: Create Virtual Environments For Projects

**Duration:** 5 minutes

---

### What Is a Virtual Environment?

An isolated Python environment for each project:

```bash
python3 -m venv myenv    # Create
source myenv/bin/activate # Activate
pip install flask        # Install (only in this env)
deactivate               # Leave
```

---

### Key Points

- One environment per project
- Keeps dependencies isolated
- Use `requirements.txt` to share setup
