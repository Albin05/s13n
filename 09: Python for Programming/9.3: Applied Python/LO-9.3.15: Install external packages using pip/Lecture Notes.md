# Lecture Notes: Install External Packages

## Install External Packages

Using pip to install third-party Python packages


---

<div align="center">

![Variables concept - labeled storage containers](https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=800&q=80)

*Think of variables as labeled containers storing different types of data*

</div>

---

## Introduction

`pip` implements **package management** - installing, updating, removing third-party code! **PyPI** (Python Package Index) has 500,000+ packages - the world's largest software repository. `pip` is Python's **app store**!

### Why Package Managers Matter

**Before pip** (manual installation): Download, extract, install manually:
```bash
# The bad old days!
wget package.tar.gz
tar -xzf package.tar.gz
cd package
python setup.py install  # Often failed!
```

**With pip** (automatic): One command, handles everything:
```bash
pip install requests  # Done!
# Dependencies, versions, paths - all automatic!
```

**This is dependency management** - pip handles the complexity!

### Historical Context

**pip created 2008** by Ian Bicking. Replaced **easy_install** (2004) which was problematic. **PyPI** (Python Package Index, 2003) centralized package distribution - inspired by **CPAN** (Perl, 1995).

**Why "pip"?** Originally "Pip Installs Packages" (recursive acronym) or "Pip Installs Python". Follows Unix tradition of recursive names (GNU = "GNU's Not Unix").

**Virtual environments** (venv, 2012) solved **dependency conflicts** - different projects need different package versions. pip + venv = **isolated environments**!

### Real-World Analogies

**pip like app store**:
- **PyPI**: App repository (500K+ packages)
- **pip install**: Download and install app
- **requirements.txt**: App bundle (install multiple)
**Python has an app store for code!**

---
### Key Concepts

External packages extend Python's capabilities:
- Thousands of packages available on PyPI (Python Package Index)
- Use `pip` (Python's package installer)
- Access to web frameworks, data science tools, and more
- Community-maintained libraries

### Core Principles

**Package management**: `pip install`, `pip uninstall`, `pip list`, `pip freeze`, `requirements.txt`

### Syntax and Usage

```bash
# Install a package
pip install package_name

# Install specific version
pip install package_name==1.2.3

# Upgrade a package
pip install --upgrade package_name

# Uninstall a package
pip uninstall package_name

# List installed packages
pip list

# Show package info
pip show package_name

# Generate requirements file
pip freeze > requirements.txt

# Install from requirements file
pip install -r requirements.txt
```

### Practical Examples

#### Example 1: Installing and Using requests

```bash
# In terminal:
pip install requests
```

```python
import requests

# Make HTTP GET request
response = requests.get('https://api.github.com')

print(f"Status code: {response.status_code}")
print(f"Content type: {response.headers['content-type']}")

# Parse JSON response
data = response.json()
print(f"API version: {data.get('current_user_url', 'N/A')}")

# GET request with parameters
params = {'q': 'python', 'sort': 'stars'}
response = requests.get('https://api.github.com/search/repositories', params=params)

if response.status_code == 200:
    results = response.json()
    print(f"Total repositories: {results['total_count']}")

# POST request
payload = {'key': 'value', 'name': 'test'}
response = requests.post('https://httpbin.org/post', json=payload)
print(f"Response: {response.json()}")
```

#### Example 2: Working with Multiple Packages

```bash
# Install multiple packages at once
pip install requests beautifulsoup4 pandas
```

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch webpage
url = 'https://example.com'
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find('title').text
print(f"Page title: {title}")

# Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)

print(df)
# Output:
#       Name  Age      City
# 0    Alice   25  New York
# 1      Bob   30    London
# 2  Charlie   35     Paris

# Save to CSV
df.to_csv('people.csv', index=False)
print("Data saved to people.csv")
```

#### Example 3: Using Requirements File

```bash
# Create requirements.txt file
cat > requirements.txt << EOL
requests==2.31.0
beautifulsoup4==4.12.0
pandas>=2.0.0
python-dotenv==1.0.0
EOL

# Install all requirements
pip install -r requirements.txt

# Check what's installed
pip freeze
```

```python
# Example using python-dotenv
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_key = os.getenv('API_KEY', 'default-key')
debug_mode = os.getenv('DEBUG', 'False') == 'True'

print(f"API Key loaded: {bool(api_key)}")
print(f"Debug mode: {debug_mode}")
```

#### Example 4: Version Management

```bash
# Check pip version
pip --version

# Upgrade pip itself
pip install --upgrade pip

# Install specific version
pip install requests==2.28.0

# Install minimum version
pip install 'requests>=2.28.0'

# Install version range
pip install 'requests>=2.28.0,<3.0.0'

# Show package information
pip show requests
```

```python
# Check package version in code
import requests
print(f"Requests version: {requests.__version__}")

import sys
print(f"Python version: {sys.version}")

# List all installed packages programmatically
import pkg_resources
installed_packages = pkg_resources.working_set
packages_list = sorted([f"{i.key}=={i.version}" for i in installed_packages])

print("\nInstalled packages:")
for package in packages_list[:10]:  # Show first 10
    print(f"  {package}")
```

#### Example 5: Project Setup Script

```python
# setup_project.py
import subprocess
import sys
import os

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print(f"✓ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError:
        print(f"✗ Failed to install {package}")
        return False

def setup_project():
    """Set up project dependencies"""
    print("Setting up project...\n")

    # Required packages
    packages = [
        'requests',
        'beautifulsoup4',
        'pandas',
        'python-dotenv'
    ]

    # Install each package
    success_count = 0
    for package in packages:
        if install_package(package):
            success_count += 1

    # Summary
    print(f"\nInstalled {success_count}/{len(packages)} packages successfully")

    # Create necessary directories
    directories = ['data', 'logs', 'output']
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")

    # Create .env template
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write("API_KEY=your_api_key_here\n")
            f.write("DEBUG=False\n")
        print("Created .env template")

    print("\nProject setup complete!")

if __name__ == "__main__":
    setup_project()
```

### Popular Packages to Know

**Web & APIs**:
- `requests` - HTTP library
- `beautifulsoup4` - Web scraping
- `flask` / `django` - Web frameworks
- `fastapi` - Modern web framework

**Data Science**:
- `pandas` - Data analysis
- `numpy` - Numerical computing
- `matplotlib` - Data visualization
- `scikit-learn` - Machine learning

**Utilities**:
- `python-dotenv` - Environment variables
- `pillow` - Image processing
- `pytest` - Testing framework
- `black` - Code formatter

### Best Practices

1. **Use virtual environments**: Isolate project dependencies
2. **Pin versions**: Use `package==1.2.3` for reproducibility
3. **Create requirements.txt**: Document dependencies
4. **Update regularly**: Keep packages up-to-date for security
5. **Check package reputation**: Use well-maintained packages

### Common Mistakes

1. **Installing globally**: Always use virtual environments
2. **Not pinning versions**: Can cause compatibility issues
3. **Installing unnecessary packages**: Keep dependencies minimal
4. **Ignoring security warnings**: Update vulnerable packages
5. **Not documenting dependencies**: Always maintain requirements.txt

### Pip Commands Reference

```bash
# Install
pip install package_name
pip install package_name==1.2.3
pip install -r requirements.txt

# Uninstall
pip uninstall package_name
pip uninstall -r requirements.txt

# List and Info
pip list
pip show package_name
pip freeze > requirements.txt

# Upgrade
pip install --upgrade package_name
pip install --upgrade pip

# Search (deprecated, use PyPI website)
# Visit pypi.org to search packages
```

### Key Takeaways

1. Use `pip install package_name` to install packages
2. PyPI hosts thousands of open-source packages
3. Create `requirements.txt` for project dependencies
4. Use version specifiers for compatibility
5. Always use virtual environments (covered in next lesson)
6. Check package documentation before use
7. Keep packages updated for security
