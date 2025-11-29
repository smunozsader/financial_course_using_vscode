# Real-World Project: Complete LBO Case Study

## Project: Retail Company Acquisition Analysis

### Scenario

You are an analyst at a mid-market Private Equity firm evaluating the acquisition of **"FashionRetail Co."**, a specialty apparel retailer. Your task is to build a complete LBO model and recommend whether to proceed with the acquisition.

### Company Overview

**FashionRetail Co.**
- **Industry**: Specialty Retail (Apparel)
- **Founded**: 2010
- **Stores**: 150 locations across the US
- **Employees**: 2,500

### Current Financials (LTM - Last Twelve Months)

```
Revenue:        $500M
EBITDA:         $75M
EBITDA Margin:  15%
CapEx:          $15M (3% of revenue)
D&A:            $12M
```

### Transaction Structure

**Proposed Terms:**
- **Purchase Price**: 8.0x LTM EBITDA = $600M
- **Transaction Date**: January 1, 2025
- **Holding Period**: 5 years
- **Exit Strategy**: Sale to strategic buyer or IPO

**Financing:**
- Senior Debt: 4.0x EBITDA @ 6.5% interest
- Subordinated Debt: 1.5x EBITDA @ 10.0% interest
- Equity: Balance (from PE fund)

### Your Task

Build a complete LBO model that includes:

1. **Sources & Uses** of funds
2. **Operating Model** (5-year projections)
3. **Debt Schedule** with paydown
4. **Returns Analysis** (IRR and MOIC)
5. **Sensitivity Analysis** on key assumptions
6. **Investment Memo** with recommendation

### Operating Assumptions

**Base Case:**
- Revenue Growth: 6%, 6%, 5%, 4%, 4%
- EBITDA Margin: Improves from 15% to 17% by Year 5
- CapEx: 3% of revenue
- NWC: 10% of revenue
- Tax Rate: 25%
- D&A: 2.5% of revenue

**Exit:**
- Exit Multiple: 9.0x EBITDA
- Target IRR: 20%+
- Target MOIC: 2.5x+

### Building the Model

#### Step 1: Set Up Your Environment

```python
import sys
sys.path.append('..')  # Add parent directory to path

from Module_05_LBO_Modeling.lbo_model import LBOModel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

#### Step 2: Initialize the Model

```python
# Create LBO model instance
model = LBOModel(
    company_name="FashionRetail Co.",
    transaction_date="2025-01-01"
)
```

#### Step 3: Set Transaction Assumptions

```python
# Entry valuation
model.set_transaction_assumptions(
    entry_ebitda=75,  # $75M
    entry_multiple=8.0
)

print(f"Purchase Price: ${model.purchase_price}M")
```

#### Step 4: Set Financing Structure

```python
# Debt financing
model.set_financing_structure(
    equity_pct=0.40,  # Will be calculated
    senior_debt_multiple=4.0,
    sub_debt_multiple=1.5,
    senior_rate=0.065,
    sub_rate=0.10
)

# Display sources and uses
su = model.build_sources_and_uses()
print("\nSources of Funds:")
print(su['Sources'])
print("\nUses of Funds:")
print(su['Uses'])
```

#### Step 5: Set Operating Assumptions

```python
# Revenue growth and margins
model.set_operating_assumptions(
    revenue_growth_rates=[0.06, 0.06, 0.05, 0.04, 0.04],
    ebitda_margin=0.16,  # Average over period
    tax_rate=0.25,
    capex_pct=0.03,
    nwc_pct=0.10,
    da_pct=0.025
)
```

#### Step 6: Set Exit Assumptions

```python
# Exit valuation
model.set_exit_assumptions(exit_multiple=9.0)
```

#### Step 7: Build the Model

```python
# Generate projections
projections = model.build_operating_model()
debt_schedule = model.build_debt_schedule()

# Calculate returns
returns = model.calculate_returns()

print(f"\nReturns Summary:")
print(f"MOIC: {returns['MOIC']:.2f}x")
print(f"IRR: {returns['IRR']:.1%}")
```

#### Step 8: Display Full Results

```python
# Complete summary
model.display_summary()
```

### Analysis Questions

Answer these questions in your investment memo:

1. **Valuation**
   - Is 8.0x EBITDA a fair entry multiple?
   - Compare to industry benchmarks
   - What's the implied premium to revenue?

2. **Returns**
   - Does the deal meet target returns (20% IRR, 2.5x MOIC)?
   - What are the key return drivers?
   - Margin expansion vs revenue growth vs multiple expansion?

3. **Leverage**
   - Is 5.5x Debt/EBITDA reasonable?
   - Can the company service the debt?
   - When will debt be paid down to <3x?

4. **Risks**
   - What if revenue growth is slower?
   - What if margins don't improve?
   - What if exit multiple contracts?

5. **Value Creation**
   - Where will value be created?
   - What operational improvements are needed?
   - What are the exit options?

### Sensitivity Analysis

Test different scenarios:

```python
# Revenue growth sensitivity
growth_scenarios = {
    'Base': [0.06, 0.06, 0.05, 0.04, 0.04],
    'Bull': [0.08, 0.08, 0.07, 0.06, 0.05],
    'Bear': [0.04, 0.04, 0.03, 0.02, 0.02]
}

results = []

for scenario, growth_rates in growth_scenarios.items():
    test_model = LBOModel("FashionRetail", "2025-01-01")
    test_model.set_transaction_assumptions(75, 8.0)
    test_model.set_financing_structure(0.40, 4.0, 1.5, 0.065, 0.10)
    test_model.set_operating_assumptions(
        growth_rates, 0.16, 0.25, 0.03, 0.10, 0.025
    )
    test_model.set_exit_assumptions(9.0)
    
    test_model.build_operating_model()
    test_model.build_debt_schedule()
    rets = test_model.calculate_returns()
    
    results.append({
        'Scenario': scenario,
        'MOIC': rets['MOIC'],
        'IRR': rets['IRR']
    })

sensitivity_df = pd.DataFrame(results)
print("\nScenario Analysis:")
print(sensitivity_df)
```

### Deliverables

Create these outputs:

1. **Executive Summary** (1 page)
   - Investment thesis
   - Key metrics
   - Recommendation

2. **Financial Model** (Python notebook)
   - All calculations
   - Clearly commented
   - Reproducible

3. **Sensitivity Analysis**
   - Multiple scenarios
   - Key driver charts
   - Risk assessment

4. **Investment Memo** (3-5 pages)
   - Company overview
   - Transaction structure
   - Financial projections
   - Returns analysis
   - Risks and mitigants
   - Recommendation

### Grading Criteria

- **Model Accuracy** (40%): Correct calculations, logical structure
- **Analysis Depth** (30%): Thoughtful insights, comprehensive scenarios
- **Presentation** (20%): Clear charts, professional memo
- **Judgment** (10%): Sound recommendation with good rationale

### Bonus Challenges

**Advanced:**
1. Build a custom debt schedule with cash sweeps
2. Add management rollover equity
3. Model dividend recaps
4. Create a fund-level IRR analysis
5. Build a Monte Carlo simulation

**Excel Integration:**
- Export model to Excel with formatting
- Create dashboard with charts
- Build sensitivity tables

### Sample Solution

A complete solution is available in:
`Module_09_Projects/lbo_case_study_solution.py`

But try to build it yourself first!

### Real-World Application

This type of analysis is exactly what you'd do in:
- Private Equity firms (deal execution)
- Investment Banking (sell-side / buy-side)
- Corporate Development (M&A evaluation)
- Consulting (transaction advisory)

### Time Estimate

- **Model Building**: 3-4 hours
- **Analysis**: 2-3 hours
- **Memo Writing**: 2-3 hours
- **Total**: 7-10 hours

### Resources

- Historical retail comps data: `data/retail_comps.csv`
- Industry reports: `resources/retail_industry.pdf`
- Template slides: `templates/investment_memo_template.pptx`

---

**Good luck! Remember: this is a real-world skill that will set you apart in finance.**

### Questions?

Review these modules if you need help:
- Module 5: LBO Modeling
- Module 3: Data Analysis
- Module 8: Visualization

---

*This project simulates actual work done by PE associates and IB analysts daily.*
