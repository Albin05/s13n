# Lecture Notes: Create Virtual Environments

## Create Virtual Environments

Isolating project dependencies using virtual environments


---

<div align="center">

![Python Virtual Environment venv Folder Structure](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/python-lectures/9.3/LO-9.3.16.png)

*Virtual environments isolate project dependencies, keeping each project's modules separate*

</div>

---

## Introduction

Virtual environments solve **dependency hell** - the nightmare of conflicting package versions! Each project gets its own isolated Python installation with independent packages. This is **dependency isolation** - the foundation of reproducible, maintainable Python development!

### Why Virtual Environments are Essential

**Before venv** (global installation): All projects share packages - conflict disaster:
```bash
# Project A needs Django 2.2
pip install django==2.2

# Project B needs Django 4.0
pip install django==4.0  # BREAKS Project A!
# Both projects broken!
```

**With venv** (isolated): Each project has own packages:
```bash
# Project A's environment
(projectA) $ pip install django==2.2  # Isolated!

# Project B's environment
(projectB) $ pip install django==4.0  # Also isolated!
# Both work perfectly!
```

**This is dependency isolation** - no more version conflicts!

### Historical Context

**Virtual environments** invented to solve **dependency hell**. **virtualenv** (Ian Bicking, 2007) pioneered isolated environments. **venv** (Python 3.3, 2012) made it standard library!

**The dependency problem**: Projects need different package versions. Global installation = **conflict**. Solution: **isolated environments** - each project gets own package directory!

**Modern tools**: **virtualenv** (original), **venv** (built-in), **conda** (Anaconda), **poetry** (modern dependency management). All solve same problem - isolation!

### Real-World Analogies

**Virtual environments like separate apartments**:
- **Global Python**: One house, everyone shares (chaos!)
- **Virtual envs**: Separate apartments, own furniture (peace!)
- **Activate**: Enter your apartment
- **Deactivate**: Leave apartment
**Each project gets its own space!**

**Or like game save files**:
```bash
# Different save files for different playthroughs
(playthrough1) $ # Character level 50, mage build
(playthrough2) $ # Character level 30, warrior build
# Each isolated!
```

**Or like virtual machines**:
- **VM**: Isolated operating system
- **venv**: Isolated Python environment
- **Lighter**: venv shares Python binary, isolates packages only
**Same isolation concept, lighter weight!**

---
### Key Concepts

Virtual environments allow you to:
- Isolate project dependencies
- Avoid package conflicts between projects
- Maintain different Python versions per project
- Create reproducible development environments
- Share exact dependency versions with team

### Core Principles

**Key tools**: `venv` (built-in), `virtualenv`, activation/deactivation

### Syntax and Usage

```bash
# Create virtual environment
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (Mac/Linux)
source myenv/bin/activate

# Deactivate
deactivate

# Install packages in virtual environment
pip install package_name

# Remove virtual environment
rm -rf myenv  # or delete folder
```

### Practical Examples

#### Example 1: Creating Your First Virtual Environment

```bash
# Create a new project directory
mkdir my_project
cd my_project

# Create virtual environment named 'venv'
python -m venv venv

# Activate it (Mac/Linux)
source venv/bin/activate

# Your prompt should now show (venv)
(venv) $ which python
# Shows: /path/to/my_project/venv/bin/python

# Install packages - they go into venv only
(venv) $ pip install requests
(venv) $ pip list
# Shows only packages in this environment

# Deactivate when done
(venv) $ deactivate
$ # Back to system Python
```

#### Example 2: Project Setup with Requirements

```bash
# Start new project
mkdir web_scraper
cd web_scraper

# Create and activate venv
python -m venv env
source env/bin/activate  # Mac/Linux
# env\Scripts\activate  # Windows

# Install project dependencies
pip install requests beautifulsoup4 pandas

# Save dependencies
pip freeze > requirements.txt

# View requirements.txt:
cat requirements.txt
# Output:
# beautifulsoup4==4.12.2
# pandas==2.1.0
# requests==2.31.0
# ...

# Someone else can now recreate your environment:
# python -m venv env
# source env/bin/activate
# pip install -r requirements.txt
```

#### Example 3: Multiple Environments for Different Projects

```bash
# Project 1: Data Science (needs pandas, numpy)
mkdir data_analysis
cd data_analysis
python -m venv venv
source venv/bin/activate
pip install pandas numpy matplotlib
pip freeze > requirements.txt
deactivate

# Project 2: Web App (needs flask)
cd ..
mkdir web_app
cd web_app
python -m venv venv
source venv/bin/activate
pip install flask
pip freeze > requirements.txt
deactivate

# Each project has isolated dependencies!
# No conflicts between different package versions
```

#### Example 4: Automation Script for Environment Setup

```python
# setup_env.py
import os
import subprocess
import sys

def create_venv(venv_name='venv'):
    """Create a virtual environment"""
    if os.path.exists(venv_name):
        print(f"Virtual environment '{venv_name}' already exists")
        return False

    print(f"Creating virtual environment '{venv_name}'...")
    subprocess.run([sys.executable, '-m', 'venv', venv_name])
    print(f"✓ Created {venv_name}")
    return True

def get_activate_command(venv_name='venv'):
    """Get the activation command for the current OS"""
    if sys.platform == 'win32':
        return f"{venv_name}\\Scripts\\activate"
    else:
        return f"source {venv_name}/bin/activate"

def create_requirements_template():
    """Create a template requirements.txt"""
    requirements = """# Core dependencies
requests==2.31.0
python-dotenv==1.0.0

# Data processing (uncomment if needed)
# pandas==2.1.0
# numpy==1.24.0

# Testing (uncomment if needed)
# pytest==7.4.0
"""
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    print("✓ Created requirements.txt template")

def create_gitignore():
    """Create .gitignore for Python project"""
    gitignore = """# Virtual Environment
venv/
env/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Environment variables
.env

# IDE
.vscode/
.idea/
*.swp
"""
    with open('.gitignore', 'w') as f:
        f.write(gitignore)
    print("✓ Created .gitignore")

def main():
    """Set up a new Python project"""
    print("Python Project Setup\n" + "="*50)

    # Create virtual environment
    venv_name = input("Enter venv name (default: venv): ").strip() or 'venv'
    create_venv(venv_name)

    # Create project files
    create_requirements_template()
    create_gitignore()

    # Instructions
    print("\n" + "="*50)
    print("Setup complete! Next steps:\n")
    print(f"1. Activate virtual environment:")
    print(f"   {get_activate_command(venv_name)}")
    print("\n2. Install dependencies:")
    print("   pip install -r requirements.txt")
    print("\n3. Start coding!")

if __name__ == "__main__":
    main()
```

#### Example 5: Checking Active Environment

```python
# check_env.py
import sys
import os

def check_virtual_env():
    """Check if running in virtual environment"""
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )

    print("Python Environment Check")
    print("="*50)
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Virtual environment: {'Yes' if in_venv else 'No'}")

    if in_venv:
        print(f"Environment path: {sys.prefix}")
    else:
        print("⚠️  Not in a virtual environment!")
        print("Consider creating one: python -m venv venv")

    print("\nInstalled packages:")
    os.system('pip list --format=columns')

if __name__ == "__main__":
    check_virtual_env()
```

### Best Practices

1. **One venv per project**: Keep dependencies isolated
2. **Name it 'venv' or 'env'**: Standard convention
3. **Add to .gitignore**: Don't commit venv to git
4. **Use requirements.txt**: Document dependencies
5. **Activate before working**: Always activate before running project
6. **Update regularly**: Keep dependencies current

### Common Commands Cheat Sheet

```bash
# Create
python -m venv venv
python3 -m venv venv  # If python3 needed

# Activate
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate         # Windows
.\venv\Scripts\Activate.ps1  # Windows PowerShell

# Check if activated
which python  # Should show venv path

# Work with packages
pip install package_name
pip install -r requirements.txt
pip freeze > requirements.txt
pip list

# Deactivate
deactivate

# Delete
rm -rf venv      # Mac/Linux
rmdir /s venv    # Windows
```

### Common Mistakes

1. **Forgetting to activate**: Installing packages globally instead of in venv
2. **Committing venv to git**: Add to .gitignore
3. **Using wrong Python**: Check `which python` after activating
4. **Not using requirements.txt**: Hard to reproduce environment
5. **Mixing system and venv packages**: Keep them separate

### Troubleshooting

```bash
# Problem: venv not activating
# Solution: Check your shell and use correct activation script

# Problem: "python: command not found"
# Solution: Use python3 instead
python3 -m venv venv

# Problem: pip installing to wrong location
# Solution: Check you're in activated venv
which pip  # Should show venv path

# Problem: Permission denied
# Solution: Don't use sudo with venv, fix ownership:
chown -R $USER:$USER venv
```

### Virtual Environment Structure

```
my_project/
├── venv/                  # Virtual environment (don't commit)
│   ├── bin/              # Executables (Mac/Linux)
│   ├── Scripts/          # Executables (Windows)
│   ├── lib/              # Installed packages
│   └── pyvenv.cfg        # Configuration
├── requirements.txt       # Dependencies
├── .gitignore            # Ignore venv
└── main.py               # Your code
```

### Key Takeaways

1. Virtual environments isolate project dependencies
2. Use `python -m venv venv` to create
3. Activate before working: `source venv/bin/activate`
4. Install packages only when activated
5. Use `requirements.txt` to share dependencies
6. Add venv to `.gitignore`
7. One virtual environment per project
