# Module 2: Python Fundamentals for Finance

## Lesson 1: Python Basics for Financial Modeling

### Introduction

In this module, you'll learn Python programming specifically tailored for financial modeling. Unlike general Python courses, we focus exclusively on what you need for Investment Banking and Private Equity work.

### Python Data Types for Finance

#### Numbers in Finance

```python
# Integers - for counting items, years, periods
shares_outstanding = 1000000
projection_years = 5
transaction_year = 2025

# Floats - for monetary values, rates, multiples
stock_price = 45.67
interest_rate = 0.065  # 6.5%
ev_ebitda_multiple = 12.5
revenue = 1_500_000_000  # $1.5B (underscores for readability)

# Financial calculations
market_cap = shares_outstanding * stock_price
print(f"Market Cap: ${market_cap:,.2f}")
```

#### Strings - for labels and formatting

```python
company_name = "TechCo Inc."
ticker = "TECH"
sector = "Technology"

# String formatting (f-strings)
print(f"{company_name} ({ticker}) - {sector}")

# Creating labels for financial statements
line_items = ["Revenue", "COGS", "Gross Profit", "EBITDA", "Net Income"]
```

#### Lists - for time series data

```python
# Revenue projections
revenues = [100, 115, 132, 152, 175]  # in millions

# Years
years = [2025, 2026, 2027, 2028, 2029]

# Accessing elements
current_year_revenue = revenues[0]  # 100
last_year_revenue = revenues[-1]    # 175

# List operations
total_revenue = sum(revenues)
avg_revenue = sum(revenues) / len(revenues)
```

#### Dictionaries - for financial data structures

```python
# Company financials
financials = {
    "revenue": 1500,
    "ebitda": 300,
    "net_income": 150,
    "total_debt": 400,
    "cash": 100
}

# Accessing values
revenue = financials["revenue"]
net_debt = financials["total_debt"] - financials["cash"]

# Calculating metrics
ebitda_margin = financials["ebitda"] / financials["revenue"]
print(f"EBITDA Margin: {ebitda_margin:.1%}")
```

### Essential Financial Functions

#### Time Value of Money

```python
def future_value(pv, rate, periods):
    """Calculate future value"""
    return pv * (1 + rate) ** periods

def present_value(fv, rate, periods):
    """Calculate present value"""
    return fv / (1 + rate) ** periods

def pmt(rate, nper, pv):
    """Calculate payment amount (like Excel PMT)"""
    return pv * (rate * (1 + rate)**nper) / ((1 + rate)**nper - 1)

# Examples
initial_investment = 10000
annual_rate = 0.08
years = 5

fv = future_value(initial_investment, annual_rate, years)
print(f"Future Value: ${fv:,.2f}")
```

#### Growth Calculations

```python
def cagr(beginning_value, ending_value, periods):
    """Calculate Compound Annual Growth Rate"""
    return (ending_value / beginning_value) ** (1 / periods) - 1

# Revenue growth
revenue_2020 = 100
revenue_2024 = 175
years = 4

growth_rate = cagr(revenue_2020, revenue_2024, years)
print(f"Revenue CAGR: {growth_rate:.1%}")
```

#### Financial Metrics

```python
def calculate_roic(nopat, invested_capital):
    """Return on Invested Capital"""
    return nopat / invested_capital

def calculate_wacc(cost_of_equity, cost_of_debt, market_value_equity, 
                   market_value_debt, tax_rate):
    """Weighted Average Cost of Capital"""
    total_value = market_value_equity + market_value_debt
    
    weight_equity = market_value_equity / total_value
    weight_debt = market_value_debt / total_value
    
    wacc = (weight_equity * cost_of_equity + 
            weight_debt * cost_of_debt * (1 - tax_rate))
    
    return wacc

# Example
wacc = calculate_wacc(
    cost_of_equity=0.12,
    cost_of_debt=0.05,
    market_value_equity=1000,
    market_value_debt=400,
    tax_rate=0.25
)
print(f"WACC: {wacc:.2%}")
```

### Loops in Financial Modeling

#### For Loops - Projecting financials

```python
# Project revenue with growth rate
base_revenue = 100
growth_rate = 0.15
years = 5

revenue_projections = []
current_revenue = base_revenue

for year in range(years):
    revenue_projections.append(current_revenue)
    current_revenue *= (1 + growth_rate)

print("Revenue Projections:")
for year, revenue in enumerate(revenue_projections, 1):
    print(f"Year {year}: ${revenue:.2f}M")
```

#### List Comprehensions - Cleaner projections

```python
# Same as above, but more concise
revenues = [base_revenue * (1 + growth_rate)**year for year in range(5)]

# Calculate margins
ebitda_margin = 0.20
ebitdas = [rev * ebitda_margin for rev in revenues]

# NPV calculation
discount_rate = 0.10
npv = sum(cf / (1 + discount_rate)**year 
          for year, cf in enumerate(revenues, 1))
```

### Conditional Logic

```python
def classify_credit_rating(interest_coverage):
    """
    Classify credit rating based on interest coverage
    Interest Coverage = EBIT / Interest Expense
    """
    if interest_coverage > 8:
        return "AAA"
    elif interest_coverage > 6:
        return "AA"
    elif interest_coverage > 4:
        return "A"
    elif interest_coverage > 2.5:
        return "BBB"
    elif interest_coverage > 1.5:
        return "BB"
    else:
        return "B or below"

# Example
ebit = 250
interest_expense = 40
coverage = ebit / interest_expense

rating = classify_credit_rating(coverage)
print(f"Interest Coverage: {coverage:.1f}x → Rating: {rating}")
```

### Working with Dates

```python
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Transaction dates
announcement_date = datetime(2025, 1, 15)
closing_date = announcement_date + timedelta(days=90)

print(f"Announcement: {announcement_date.strftime('%B %d, %Y')}")
print(f"Expected Close: {closing_date.strftime('%B %d, %Y')}")

# Financial calendar
fiscal_year_end = datetime(2024, 12, 31)
quarters = [fiscal_year_end - relativedelta(months=3*i) for i in range(4, 0, -1)]

print("\nFiscal Year Quarters:")
for i, quarter in enumerate(quarters, 1):
    print(f"Q{i}: {quarter.strftime('%b %Y')}")
```

### Error Handling in Models

```python
def safe_divide(numerator, denominator, default=0):
    """Safely divide, handling division by zero"""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return default

# Example: calculating margins
revenue = 0  # Edge case
operating_income = 50

margin = safe_divide(operating_income, revenue, default=None)

if margin is None:
    print("Cannot calculate margin - no revenue")
else:
    print(f"Operating Margin: {margin:.1%}")
```

### Building a Financial Model Class

```python
class Company:
    """Simple company financial model"""
    
    def __init__(self, name, ticker, revenue, ebitda, net_income):
        self.name = name
        self.ticker = ticker
        self.revenue = revenue
        self.ebitda = ebitda
        self.net_income = net_income
    
    def ebitda_margin(self):
        """Calculate EBITDA margin"""
        return self.ebitda / self.revenue if self.revenue > 0 else 0
    
    def net_margin(self):
        """Calculate net margin"""
        return self.net_income / self.revenue if self.revenue > 0 else 0
    
    def display_metrics(self):
        """Print key metrics"""
        print(f"\n{self.name} ({self.ticker})")
        print(f"{'='*40}")
        print(f"Revenue:        ${self.revenue:,.0f}M")
        print(f"EBITDA:         ${self.ebitda:,.0f}M")
        print(f"Net Income:     ${self.net_income:,.0f}M")
        print(f"EBITDA Margin:  {self.ebitda_margin():.1%}")
        print(f"Net Margin:     {self.net_margin():.1%}")

# Create company instance
tech_co = Company(
    name="TechCo",
    ticker="TECH",
    revenue=1500,
    ebitda=300,
    net_income=150
)

tech_co.display_metrics()
```

### Practice Exercises

#### Exercise 1: Revenue Model
Build a function that projects revenue given:
- Base year revenue
- Growth rates for each year (can be different)
- Number of years

```python
def project_revenue(base_revenue, growth_rates):
    """
    Project revenue over multiple years
    
    Parameters:
    -----------
    base_revenue : float
        Starting revenue
    growth_rates : list
        Growth rate for each year
    
    Returns:
    --------
    list : Revenue projections
    """
    # Your code here
    pass
```

#### Exercise 2: LBO Returns Calculator
Calculate IRR approximation for an LBO:
- Entry valuation: $500M at 8x EBITDA
- Exit valuation: 5 years later at 10x EBITDA
- EBITDA grows from $62.5M to $85M

```python
def lbo_moic(entry_value, exit_value):
    """Calculate Multiple on Invested Capital"""
    # Your code here
    pass

def approximate_irr(moic, years):
    """Approximate IRR from MOIC"""
    # Your code here
    pass
```

#### Exercise 3: DCF Model
Build a simple DCF calculator:

```python
def simple_dcf(cash_flows, discount_rate, terminal_value):
    """
    Calculate enterprise value using DCF
    
    Parameters:
    -----------
    cash_flows : list
        Free cash flows for projection period
    discount_rate : float
        WACC or discount rate
    terminal_value : float
        Terminal value at end of projection
    
    Returns:
    --------
    float : Enterprise value
    """
    # Your code here
    pass
```

### Solutions

See `Module_02_Python_Fundamentals/solutions.py` for complete solutions.

### Key Takeaways

✅ **Variables**: Use meaningful names (e.g., `ebitda_margin`, not `x`)
✅ **Functions**: Encapsulate financial calculations for reusability
✅ **Lists**: Perfect for time series (revenues, cash flows)
✅ **Dictionaries**: Great for financial statements
✅ **Loops**: Project financials over multiple periods
✅ **Classes**: Build reusable company/model objects

### Next Steps

Continue to: `Module_02_Python_Fundamentals/02_NumPy_for_Finance.md`

---

**Estimated Time**: 2-3 hours
**Prerequisites**: None (complete beginner friendly)
