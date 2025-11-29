# Quick Start Guide - Windows PC

## Get Started in 30 Minutes

This quick guide gets you from zero to running your first financial model in Python on Windows.

---

## Step 1: Install VS Code (5 minutes)

1. Go to https://code.visualstudio.com/
2. Click **Download for Windows**
3. Run the installer
4. ✅ Check "Add to PATH"
5. ✅ Check "Create a desktop icon"
6. Click **Install**

---

## Step 2: Install Python (5 minutes)

1. Go to https://www.python.org/downloads/
2. Click **Download Python 3.11** (or latest version)
3. Run the installer
4. ✅ **CRITICAL**: Check "Add Python to PATH"
5. ✅ Check "Install pip"
6. Click **Install Now**

**Test it:**
- Open VS Code
- Press `Ctrl+`` (control + backtick) to open terminal
- Type: `python --version`
- You should see: `Python 3.11.x`

---

## Step 3: Install Extensions (3 minutes)

In VS Code:
1. Click Extensions icon (or press `Ctrl+Shift+X`)
2. Search and install these:
   - **Python** (by Microsoft)
   - **Jupyter** (by Microsoft)
   - **Pylance** (by Microsoft)

---

## Step 4: Create Your Project (5 minutes)

In VS Code terminal (`Ctrl+``):

```bash
# Create and navigate to project folder
mkdir financial-modeling
cd financial-modeling

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# You should see (venv) at the start of your line
```

**PowerShell users:** If you get an error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Step 5: Install Libraries (5 minutes)

With your virtual environment activated:

```bash
pip install numpy pandas matplotlib yfinance jupyter openpyxl
```

This installs everything you need for financial modeling.

---

## Step 6: Test Everything (5 minutes)

Create a new file: `test.py`

Copy and paste this code:

```python
import numpy as np
import pandas as pd

# Simple investment calculator
def future_value(present_value, rate, years):
    return present_value * (1 + rate) ** years

# Example: $10,000 at 8% for 5 years
initial = 10000
rate = 0.08
years = 5

result = future_value(initial, rate, years)

print(f"Investment: ${initial:,.2f}")
print(f"Annual Return: {rate:.1%}")
print(f"Years: {years}")
print(f"Future Value: ${result:,.2f}")
print(f"Profit: ${result - initial:,.2f}")
```

**Run it:**
- Click the ▶️ play button (top right)
- Or press `Ctrl+F5`

You should see:
```
Investment: $10,000.00
Annual Return: 8.0%
Years: 5
Future Value: $14,693.28
Profit: $4,693.28
```

---

## ✅ You're Ready!

If you see the output above, you're all set! You just:
- Installed a professional development environment
- Set up Python for financial analysis
- Ran your first financial calculation

---

## Next Steps

1. **Start the course**: Open `Module_01_Setup/01_Getting_Started.md`
2. **Learn Python basics**: Continue to `Module_02_Python_Fundamentals/`
3. **Build real models**: Module 4 (DCF) and Module 5 (LBO)

---

## Common Issues

### "python is not recognized"
- Python not in PATH
- Reinstall Python and check "Add to PATH"
- Restart VS Code

### Virtual environment won't activate
- Make sure you're in the right folder
- Use: `venv\Scripts\activate` (Command Prompt)
- Or: `.\venv\Scripts\Activate.ps1` (PowerShell)
- PowerShell: May need to change execution policy

### Import errors
- Make sure virtual environment is activated (you see `(venv)`)
- Reinstall packages: `pip install numpy pandas matplotlib`

### Extension not working
- Reload VS Code: `Ctrl+Shift+P` → "Reload Window"
- Restart VS Code completely
- Check for updates

---

## Keyboard Shortcuts to Remember

| Shortcut | Action |
|----------|--------|
| `Ctrl+`` | Open terminal |
| `Ctrl+P` | Quick file open |
| `Ctrl+Shift+P` | Command palette |
| `Ctrl+/` | Comment code |
| `F5` | Run with debugger |
| `Ctrl+F5` | Run without debugger |

---

## Tips for Success

1. **Type code, don't copy-paste** - builds muscle memory
2. **Run code frequently** - see results immediately
3. **Experiment** - change numbers, see what happens
4. **Use comments** - explain your code with `#`
5. **Save often** - `Ctrl+S`

---

## Getting Help

- **Within course**: Check `solutions.py` files in each module
- **Python errors**: Read the error message carefully
- **Google**: "Python [your question]" - Stack Overflow is your friend
- **VS Code**: `Ctrl+Shift+P` → search for commands

---

**Estimated Total Time**: 30 minutes
**Difficulty**: Beginner-friendly

**Ready to become a Python-powered financial modeler? Let's go!** 🚀

→ Start with: `Module_01_Setup/01_Getting_Started.md`
