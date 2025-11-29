# GitHub Copilot Instructions for Financial Modeling Course

## 🎯 Course Context

This is a comprehensive financial modeling course for **Investment Banking and Private Equity professionals**, specifically designed for:

- **Student:** Mauricio Muñoz de Alba Montiel (PE analyst at PE Club, Brussels)
- **Created by:** Sergio Muñoz de Alba Medrano (father & course creator)
- **Focus:** Combining traditional finance expertise with modern Python/AI tools
- **Platform:** VS Code + Python + GitHub + AI (Copilot)

---

## 📚 Project Structure

```
Root/
├── START_HERE.md              # Main entry point - personal letter from Sergio
├── QUICK_START_GUIDE.md       # 30-min Windows setup guide
├── README.md                  # Course overview
├── .gitignore                 # Git exclusions
│
├── Tutorials/                 # 🎓 Beginner-focused VS Code tutorials
│   ├── 01_VS_Code_Basics.md
│   ├── 02_GitHub_Copilot_Hands_On.md
│   ├── 03_VS_Code_Data_Analysis.md
│   ├── 04_Building_DCF_with_VS_Code.md
│   └── 05_VS_Code_Power_User.md
│
├── Module_01_Setup/           # Environment setup
├── Module_02_Python_Fundamentals/
├── Module_03_Data_Analysis/
├── Module_04_DCF_Modeling/
├── Module_05_LBO_Modeling/
├── Module_06_MA_Analysis/
├── Module_07_PE_Modeling/
├── Module_08_Advanced_Topics/
└── Module_09_Projects/
```

---

## 🤖 Copilot Coding Guidelines

### When Assisting with Financial Code:

#### 1. **Financial Formulas - Be Precise**
```python
# ✅ GOOD: Clear formula with comments
def calculate_wacc(equity_value, debt_value, cost_of_equity, cost_of_debt, tax_rate):
    """
    Calculate Weighted Average Cost of Capital (WACC)
    Formula: WACC = (E/V × Re) + (D/V × Rd × (1-Tc))
    """
    total_value = equity_value + debt_value
    equity_weight = equity_value / total_value
    debt_weight = debt_value / total_value
    
    wacc = (equity_weight * cost_of_equity) + (debt_weight * cost_of_debt * (1 - tax_rate))
    return wacc

# ❌ AVOID: Unclear, no documentation
def calc(e, d, re, rd, t):
    v = e + d
    return (e/v * re) + (d/v * rd * (1-t))
```

#### 2. **Use Finance-Appropriate Data Types**
```python
# ✅ GOOD: Use Decimal for financial calculations
from decimal import Decimal
revenue = Decimal('1000000.00')  # Precision matters in finance

# ✅ GOOD: Use pandas for financial data
import pandas as pd
income_statement = pd.DataFrame({
    'Year': [2020, 2021, 2022],
    'Revenue': [1000, 1200, 1500],
    'EBITDA': [200, 250, 350]
})

# ❌ AVOID: Floating point precision issues for money
price = 0.1 + 0.2  # = 0.30000000000000004
```

#### 3. **Financial Modeling Best Practices**
```python
# ✅ GOOD: Separate assumptions from calculations
class DCFModel:
    def __init__(self):
        # Assumptions (easy to modify)
        self.projection_years = 5
        self.terminal_growth_rate = 0.025
        self.wacc = 0.10
        
    def calculate_enterprise_value(self, cash_flows):
        # Calculations use assumptions
        pv_cash_flows = [cf / (1 + self.wacc)**i 
                        for i, cf in enumerate(cash_flows, 1)]
        return sum(pv_cash_flows)

# ✅ GOOD: Validate financial inputs
def calculate_irr(cash_flows):
    if not cash_flows:
        raise ValueError("Cash flows cannot be empty")
    if cash_flows[0] >= 0:
        raise ValueError("First cash flow must be negative (investment)")
    # ... IRR calculation
```

#### 4. **PE/IB Specific Patterns**
```python
# ✅ GOOD: LBO model structure
class LBOModel:
    def calculate_sources_and_uses(self):
        """Standard LBO sources and uses table"""
        sources = {
            'Senior Debt': self.senior_debt,
            'Subordinated Debt': self.sub_debt,
            'Equity': self.equity_investment
        }
        uses = {
            'Purchase Price': self.purchase_price,
            'Transaction Fees': self.fees,
            'Refinancing': self.refinancing
        }
        return pd.DataFrame([sources, uses])

# ✅ GOOD: Returns calculation for PE
def calculate_moic_and_irr(entry_value, exit_value, years):
    """Multiple on Invested Capital and IRR"""
    moic = exit_value / entry_value
    irr = (exit_value / entry_value) ** (1/years) - 1
    return {'MOIC': moic, 'IRR': irr}
```

---

## 💡 Copilot Prompt Templates for Finance

### For Building Models:
```
"Create a DCF model class that:
- Takes revenue projections for 5 years
- Calculates EBITDA using margin assumptions
- Computes free cash flow with CapEx and NWC
- Discounts cash flows using WACC
- Calculates terminal value with perpetuity growth
- Returns enterprise value and equity value"
```

### For Data Analysis:
```
"Write a function to:
- Load financial statements from Excel
- Calculate key ratios (ROE, ROA, Debt/Equity, Current Ratio)
- Create year-over-year growth analysis
- Export results to new Excel file with formatting"
```

### For Valuation:
```
"Build a comparable companies analysis that:
- Takes list of ticker symbols
- Downloads financial data using yfinance
- Calculates EV/EBITDA, P/E, EV/Sales multiples
- Creates summary DataFrame sorted by market cap
- Highlights median and quartiles"
```

---

## 🎯 Course-Specific Copilot Behaviors

### For Complete Beginners:
- **Explain EVERYTHING:** Add detailed comments
- **Show examples:** Include usage examples in docstrings
- **Error handling:** Add try/except with clear error messages
- **Type hints:** Use them to clarify what inputs/outputs are expected

### For Financial Code:
- **Formula in comments:** Always show mathematical formula
- **Units in variable names:** `revenue_millions`, `rate_percent`
- **Validate assumptions:** Check for negative prices, rates > 1, etc.
- **Industry conventions:** Follow PE/IB naming (MOIC, ROIC, WACC)

### For PE Club Context:
- **Real-world applicable:** Code should work with actual deals
- **Excel compatibility:** Easy export to Excel for presentations
- **Professional quality:** Clean, documented, reusable
- **Performance matters:** Efficient for large datasets

---

## 📖 Financial Terms for Copilot

When Copilot sees these terms, provide finance-appropriate code:

**Valuation:**
- DCF, NPV, IRR, WACC, CAPM, Terminal Value, Enterprise Value, Equity Value

**LBO:**
- Sources & Uses, Debt Schedule, Cash Flow Waterfall, MOIC, Returns

**Financial Statements:**
- Income Statement, Balance Sheet, Cash Flow Statement, EBITDA, NOPAT, FCF

**Metrics:**
- ROE, ROA, ROIC, P/E Ratio, EV/EBITDA, Debt/Equity, Current Ratio

**PE Specific:**
- Entry Multiple, Exit Multiple, Portfolio Company, Fund Returns, Carry

---

## ✨ Special Features in This Course

### 1. **Personal Touch**
- Course is a gift from father (Sergio) to son (Mauricio)
- Maintain encouraging, professional-yet-warm tone
- PE Club and Brussels context is important

### 2. **Windows-Focused**
- All paths use backslashes: `venv\Scripts\activate`
- PowerShell commands
- Windows keyboard shortcuts (Ctrl, not Cmd)

---

## 🔧 Code Style Preferences

```python
# Naming Conventions
class DCFModel:                    # PascalCase for classes
    def calculate_wacc(self):      # snake_case for functions
        risk_free_rate = 0.04      # snake_case for variables
        DISCOUNT_RATE = 0.10       # UPPER_CASE for constants

# Docstrings - Always include
def calculate_npv(cash_flows, discount_rate):
    """
    Calculate Net Present Value of cash flows.
    
    Parameters:
    -----------
    cash_flows : list of float
        Series of cash flows (negative = outflow, positive = inflow)
    discount_rate : float
        Discount rate (e.g., 0.10 for 10%)
    
    Returns:
    --------
    float
        Net Present Value
        
    Example:
    --------
    >>> calculate_npv([-1000, 300, 400, 500], 0.10)
    79.85
    """
    # Implementation here

# Type Hints - Use them
from typing import List, Dict, Tuple

def analyze_company(ticker: str, years: int = 5) -> Dict[str, float]:
    """Analyze company and return metrics"""
    pass
```

---

## 🎓 Learning Progression

Copilot should adjust complexity based on module:

**Modules 1-2:** Basic Python, heavy explanation, simple examples
**Modules 3-4:** Intermediate, introduce classes, real data
**Modules 5-7:** Advanced, complete models, professional patterns
**Modules 8-9:** Expert, automation, APIs, real projects

---

## ✅ Quality Checklist for Generated Code

Before accepting Copilot suggestions, ensure:

- [ ] Financial formulas are mathematically correct
- [ ] Variable names are descriptive (no `x`, `y`, `z`)
- [ ] Comments explain the "why", not just "what"
- [ ] Includes docstring with parameters/returns
- [ ] Has error handling for edge cases
- [ ] Uses appropriate data types (Decimal for money)
- [ ] Follows finance industry conventions
- [ ] Can export results to Excel if needed
- [ ] Is tested with example data
- [ ] Would work in real PE Club scenario

---

## 🚀 Advanced Copilot Usage Tips

### 1. **Iterative Refinement**
```python
# Start simple
# "Calculate present value"
def present_value(future_value, rate, periods):
    return future_value / (1 + rate) ** periods

# Ask Copilot to enhance:
# "Add error handling, type hints, and docstring to present_value function"
# Copilot will upgrade it
```

### 2. **Context-Aware Prompting**
```python
# Give context in comments
# For a PE analyst at PE Club analyzing retail buyout:
# Calculate leveraged returns for retail company acquisition
# Entry: 8.0x EBITDA, Exit: 10.0x EBITDA, 5-year hold
# 60% debt, 40% equity, EBITDA growth 5% annually

# Copilot will generate PE-appropriate code
```

### 3. **Ask for Explanations**
When reviewing generated code, select it and ask Copilot Chat:
- "Explain this financial formula"
- "What assumptions does this make?"
- "How would this work for a real LBO?"

---

## 🌟 Success Criteria

Code generated for this course should:

1. **Educate:** Clear enough for VS Code beginner to understand
2. **Function:** Actually work for real financial analysis
3. **Professional:** Match PE/IB industry standards
4. **Practical:** Usable at PE Club immediately
5. **Scalable:** Easy to modify and extend
6. **Documented:** Future Mauricio can remember what it does

---

## 📝 Example: Complete Copilot-Generated Function

```python
def calculate_lbo_returns(
    purchase_price: float,
    ebitda_entry: float,
    ebitda_exit: float,
    entry_multiple: float,
    exit_multiple: float,
    debt_percent: float,
    equity_percent: float,
    hold_period: int
) -> Dict[str, float]:
    """
    Calculate LBO returns (MOIC and IRR) for Private Equity analysis.
    
    This function models a leveraged buyout transaction commonly used
    at PE firms like PE Club for deal analysis.
    
    Parameters:
    -----------
    purchase_price : float
        Total purchase price in millions
    ebitda_entry : float
        Entry year EBITDA in millions
    ebitda_exit : float
        Exit year EBITDA in millions (after growth)
    entry_multiple : float
        Entry valuation multiple (e.g., 8.0 for 8.0x EBITDA)
    exit_multiple : float
        Exit valuation multiple (e.g., 10.0 for 10.0x EBITDA)
    debt_percent : float
        Debt as % of purchase price (e.g., 0.60 for 60%)
    equity_percent : float
        Equity as % of purchase price (e.g., 0.40 for 40%)
    hold_period : int
        Investment holding period in years
        
    Returns:
    --------
    dict
        Dictionary with 'MOIC' (Multiple on Invested Capital) and 'IRR'
        
    Example:
    --------
    >>> calculate_lbo_returns(
    ...     purchase_price=400,
    ...     ebitda_entry=50,
    ...     ebitda_exit=75,
    ...     entry_multiple=8.0,
    ...     exit_multiple=10.0,
    ...     debt_percent=0.60,
    ...     equity_percent=0.40,
    ...     hold_period=5
    ... )
    {'MOIC': 3.125, 'IRR': 0.255}  # 3.1x MOIC, 25.5% IRR
    """
    # Calculate equity investment
    equity_investment = purchase_price * equity_percent
    
    # Calculate exit enterprise value
    exit_ev = ebitda_exit * exit_multiple
    
    # Assume debt paid down to 2x EBITDA at exit (common PE assumption)
    exit_debt = ebitda_exit * 2.0
    
    # Calculate equity value at exit
    equity_at_exit = exit_ev - exit_debt
    
    # Calculate returns
    moic = equity_at_exit / equity_investment
    irr = (moic ** (1 / hold_period)) - 1
    
    return {
        'MOIC': round(moic, 3),
        'IRR': round(irr, 3),
        'Equity Investment': equity_investment,
        'Equity at Exit': equity_at_exit,
        'Exit EV': exit_ev
    }
```

**This is the quality bar for all course code!**

---

## 🎁 Remember

This course is:
- A **gift** from Sergio to Mauricio
- Designed for **PE professionals** at top firms
- About **real-world application**, not just theory
- **Beginner-friendly** for VS Code newbies
- **Professional-grade** for career advancement

**Make Sergio proud. Make Mauricio successful.** 🚀

---

*Course: Advanced Financial Modeling with VS Code*  
*For: Mauricio Muñoz de Alba Montiel, PE Club, Brussels*  
*Created: November 2025*
 