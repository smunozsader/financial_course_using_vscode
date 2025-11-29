# Module 1: Setting Up Your Financial Modeling Environment

## Lesson 1: Getting Started with VS Code

### What is Visual Studio Code?

Visual Studio Code (VS Code) is a powerful, free code editor that has become the tool of choice for modern financial analysts and quants. Unlike Excel, VS Code allows you to:

- Write reproducible, scalable financial models
- Track changes with version control (Git)
- Automate repetitive tasks
- Handle large datasets efficiently
- Create interactive visualizations
- Collaborate with teams seamlessly

### Why VS Code for Financial Modeling?

**Advantages over Excel:**
1. **Scalability**: Handle millions of rows without crashing
2. **Automation**: Run models with a single click
3. **Version Control**: Track every change to your models
4. **Transparency**: Code is self-documenting and auditable
5. **Integration**: Connect to databases, APIs, and cloud services
6. **Speed**: Calculations run orders of magnitude faster

### Why Python? (And What About Other Tools?)

This course focuses on **Python** because it's the most accessible and versatile language for financial modeling. Python strikes the perfect balance between ease of learning and professional capability - exactly what you need at PE Club.

**That said, quants and financial professionals use various tools:**

- **Python** ⭐ **(This Course)** - Best all-around choice for data analysis, modeling, and automation
- **R** - Statistical analysis and econometrics (popular in academia and quant research)
- **SQL** - Database queries and data extraction (essential for working with financial databases)
- **C++/C#** - High-frequency trading and performance-critical systems
- **MATLAB** - Quantitative research (still used in some hedge funds and academic settings)
- **Julia** - Emerging high-performance language for computational finance
- **Excel/VBA** - Still widely used in traditional finance (you already know this!)

**Why we're starting with Python:**
- Most in-demand skill for modern finance roles
- Gentlest learning curve for beginners
- 80% of what you need for PE analysis
- Largest community and best resources
- Perfect foundation for learning other languages later

**Future courses could cover:** SQL for financial databases, R for advanced statistics, or building high-performance trading systems. But Python first - it's the gateway to everything else.

### Installation Guide

#### Step 1: Install VS Code

1. **Download VS Code**
   - Visit: https://code.visualstudio.com/
   - Download for Windows (User Installer, 64-bit)
   - Run the installer (.exe file)
   - **Important**: Check "Add to PATH" during installation
   - Check "Create a desktop icon" for easy access

2. **Launch VS Code**
   - Open from Desktop or Start Menu
   - Pin to Taskbar for easy access

#### Step 2: Install Python

1. **Check if Python is installed**
   - Open VS Code
   - Go to Terminal → New Terminal (or press Ctrl+`)
   - Type: `python --version`
   - If you see a version number (3.8+), you're good to go

2. **Install Python (if needed)**
   - Download from: https://www.python.org/downloads/
   - Choose Python 3.11 or later (64-bit recommended)
   - Run the installer (.exe)
   - **CRITICAL**: Check "Add Python to PATH" before installing
   - Also check "Install pip"
   - Click "Install Now"

3. **Verify installation**
   ```bash
   python --version
   pip --version
   ```
   Note: On Windows, use `python` and `pip` (not `python3` and `pip3`)

#### Step 3: Essential VS Code Extensions

Install these extensions for financial modeling:

1. **Python** (by Microsoft)
   - Click Extensions icon (left sidebar)
   - Search "Python"
   - Install the official Microsoft Python extension
   - Provides IntelliSense, debugging, and Jupyter support

2. **Jupyter** (by Microsoft)
   - Search "Jupyter"
   - Install for notebook support
   - Essential for interactive financial analysis

3. **Excel Viewer** (by GrapeCity)
   - View and edit Excel files in VS Code
   - Useful for comparing Excel models to Python models

4. **GitLens** (by GitKraken)
   - Advanced Git integration
   - Track changes to your models

5. **Pylance** (by Microsoft)
   - Advanced Python language support
   - Better autocomplete and type checking

**To install extensions:**
- Click the Extensions icon (Ctrl+Shift+X on Windows)
- Search for each extension
- Click "Install"

#### Step 4: Set Up Python Environment

Create a dedicated environment for financial modeling:

```bash
# Create a project folder
mkdir financial-modeling
cd financial-modeling

# Create a virtual environment
python -m venv venv

# Activate the environment (Windows)
venv\Scripts\activate

# You should see (venv) at the beginning of your prompt
```

**Note for PowerShell users:** If you get an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Step 5: Install Essential Python Libraries

With your virtual environment activated:

```bash
# Core data analysis
pip install numpy pandas

# Financial data
pip install yfinance pandas-datareader

# Visualization
pip install matplotlib seaborn plotly

# Excel integration
pip install openpyxl xlrd

# Jupyter for notebooks
pip install jupyter ipykernel

# Additional useful libraries
pip install scipy scikit-learn
```

**Create a requirements.txt file** for easy reinstallation:

```bash
pip freeze > requirements.txt
```

### VS Code Configuration for Finance

#### Recommended Settings

1. **Open Settings** (Ctrl+, on Windows or File → Preferences → Settings)
2. **Add these configurations:**

```json
{
    "python.defaultInterpreterPath": ".\\venv\\Scripts\\python.exe",
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "editor.rulers": [88],
    "files.autoSave": "afterDelay",
    "editor.minimap.enabled": true,
    "workbench.colorTheme": "Default Dark Modern",
    "terminal.integrated.defaultProfile.windows": "PowerShell"
}
```

#### Setting Up Jupyter Notebooks

1. Create a new file: `test.ipynb`
2. VS Code will prompt you to select a kernel
3. Choose your virtual environment (`venv`)
4. Test with this code:

```python
import numpy as np
import pandas as pd

print("Financial Modeling Environment Ready!")
print(f"NumPy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")
```

### Your First Financial Calculation in VS Code

Create a new file: `Module_01_Setup/test_environment.py`

```python
"""
Test your financial modeling environment
"""

import numpy as np
import pandas as pd
from datetime import datetime

# Simple DCF calculation
def present_value(cash_flow, discount_rate, year):
    """Calculate present value of a future cash flow"""
    return cash_flow / (1 + discount_rate) ** year

# Example: Value a series of cash flows
cash_flows = [100, 110, 121, 133, 146]  # Growing at 10%
discount_rate = 0.12
years = range(1, 6)

pv_cash_flows = [present_value(cf, discount_rate, year) 
                 for cf, year in zip(cash_flows, years)]

print("Cash Flow Valuation Example")
print("-" * 40)
print(f"Discount Rate: {discount_rate:.1%}")
print(f"\nYear | Cash Flow | Present Value")
print("-" * 40)

for year, cf, pv in zip(years, cash_flows, pv_cash_flows):
    print(f"{year:4} | ${cf:8.2f} | ${pv:13.2f}")

total_pv = sum(pv_cash_flows)
print("-" * 40)
print(f"Total Present Value: ${total_pv:,.2f}")
```

Run this by clicking the ▶️ play button in the top right corner.

### Workspace Organization

Create this folder structure for your course:

```
financial-modeling/
│
├── venv/                          # Virtual environment
├── Module_01_Setup/               # This module
├── Module_02_Python_Fundamentals/ # Python basics
├── Module_03_Data_Analysis/       # Data handling
├── Module_04_DCF_Modeling/        # DCF models
├── Module_05_LBO_Modeling/        # LBO models
├── Module_06_MA_Analysis/         # M&A analysis
├── Module_07_PE_Modeling/         # PE models
├── Module_08_Advanced_Topics/     # Advanced techniques
├── Module_09_Projects/            # Real-world projects
│
├── data/                          # Sample datasets
├── templates/                     # Model templates
├── outputs/                       # Generated reports
│
├── requirements.txt               # Python dependencies
└── README.md                      # Course overview
```

### Keyboard Shortcuts (Windows)

Master these VS Code shortcuts:

| Shortcut | Action |
|----------|--------|
| Ctrl+P | Quick file open |
| Ctrl+Shift+P | Command palette |
| Ctrl+B | Toggle sidebar |
| Ctrl+J | Toggle terminal |
| Ctrl+/ | Comment/uncomment |
| Alt+↑/↓ | Move line up/down |
| Shift+Alt+↑/↓ | Copy line up/down |
| Ctrl+D | Select next occurrence |
| Ctrl+F | Find |
| Ctrl+Shift+F | Find in files |
| F5 | Run debugger |
| Ctrl+` | Toggle terminal |

### Git Setup (Version Control)

Track changes to your models:

```bash
# Initialize Git in your project
git init

# Create .gitignore file
echo "venv/
__pycache__/
*.pyc
.DS_Store
.ipynb_checkpoints/
outputs/" > .gitignore

# Make your first commit
git add .
git commit -m "Initial setup: Financial modeling environment"
```

### Troubleshooting

**Python not found?**
- Make sure Python is in your PATH (reinstall Python and check "Add to PATH")
- Restart VS Code after installing Python
- Open a new terminal window after installation
- Try `py` command if `python` doesn't work

**Virtual environment not activating?**
- Check that you're in the correct folder
- Use: `venv\Scripts\activate` (Command Prompt) or `.\venv\Scripts\Activate.ps1` (PowerShell)
- If PowerShell blocks scripts, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Extensions not working?**
- Reload VS Code: Ctrl+Shift+P → "Developer: Reload Window"
- Check for extension updates
- Restart VS Code completely

**Import errors?**
- Verify virtual environment is activated (look for `(venv)` in terminal)
- Reinstall packages: `pip install -r requirements.txt`

### Next Steps

You're now ready to start building financial models in Python!

**Practice Exercise:**
1. Create a new Jupyter notebook: `my_first_model.ipynb`
2. Import numpy and pandas
3. Create a simple time value of money calculator
4. Calculate the future value of $10,000 invested for 5 years at 8% annual return

**Continue to:** `Module_02_Python_Fundamentals/01_Python_Basics.md`

### Additional Resources

- VS Code Documentation: https://code.visualstudio.com/docs
- Python for Finance: https://www.python.org/about/gettingstarted/
- Pandas Documentation: https://pandas.pydata.org/docs/
- Financial Modeling Best Practices: See `resources/` folder

---

**Checkpoint**: By completing this lesson, you should have:
- ✅ VS Code installed and configured
- ✅ Python environment set up
- ✅ Essential extensions installed
- ✅ Successfully run your first financial calculation
- ✅ Understood the advantages of VS Code over Excel

**Estimated Time**: 45-60 minutes
