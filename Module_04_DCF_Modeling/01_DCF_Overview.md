# Module 4: DCF (Discounted Cash Flow) Modeling

## Building a Complete DCF Model in Python

### Overview

The DCF model is the cornerstone of investment banking valuation. In this module, you'll build a complete, production-quality DCF model in Python that rivals any Excel-based model.

### What You'll Build

A comprehensive DCF model that includes:
- Historical financial statement analysis
- Revenue projections with multiple drivers
- Operating expense modeling
- Working capital calculations
- CapEx and D&A forecasting
- Free cash flow computation
- WACC calculation
- Terminal value (perpetuity growth and exit multiple methods)
- Sensitivity analysis
- Output to Excel and visualizations

### Key Concepts

#### 1. **Free Cash Flow (FCF) Calculation**

```
Free Cash Flow = NOPAT + D&A - CapEx - Δ NWC

Where:
- NOPAT = EBIT × (1 - Tax Rate)
- D&A = Depreciation & Amortization
- CapEx = Capital Expenditures
- Δ NWC = Change in Net Working Capital
```

#### 2. **WACC (Weighted Average Cost of Capital)**

```
WACC = (E/V × Re) + (D/V × Rd × (1-Tc))

Where:
- E = Market value of equity
- D = Market value of debt
- V = E + D
- Re = Cost of equity (CAPM)
- Rd = Cost of debt
- Tc = Corporate tax rate

Cost of Equity (CAPM):
Re = Rf + β × (Rm - Rf)
```

#### 3. **Terminal Value**

**Perpetuity Growth Method:**
```
TV = FCF(n+1) / (WACC - g)
Where g = perpetual growth rate
```

**Exit Multiple Method:**
```
TV = EBITDA(n) × Exit Multiple
```

#### 4. **Enterprise Value**

```
Enterprise Value = PV(Projected FCFs) + PV(Terminal Value)

Equity Value = EV + Cash - Debt - Minority Interest + Investments
```

### Building the Model

See the complete implementation in `dcf_model.py`

The model includes:

1. **Historical Analysis**
   - Load historical financials
   - Calculate historical growth rates and margins
   - Identify trends

2. **Revenue Projections**
   - Multiple methods: % growth, volume × price, segment-based
   - Declining growth rates (terminal to perpetuity)
   
3. **Operating Model**
   - EBITDA margin assumptions
   - D&A as % of revenue or prior CapEx
   - Tax rate (statutory vs effective)

4. **Working Capital**
   - NWC = (AR + Inventory) - (AP + Accrued Expenses)
   - Model as % of revenue or days outstanding

5. **CapEx**
   - Growth CapEx vs Maintenance CapEx
   - As % of revenue or depreciation

6. **WACC Calculation**
   - CAPM for cost of equity
   - Market-based capital structure
   - Tax-affected cost of debt

7. **Valuation**
   - Discount FCFs to present
   - Calculate terminal value
   - Bridge to equity value

### Practical Example

Let's value a technology company:

**Company Profile: TechCo Inc.**
- Current Revenue: $1,050M
- EBITDA Margin: 25%
- Growing market position
- Strong cash generation

**Assumptions:**
- Revenue growth: 18% → 15% → 12% → 10% → 8%
- EBITDA margin: 25% (stable)
- Tax rate: 25%
- CapEx: 4% of revenue
- NWC: 10% of revenue
- D&A: 3% of revenue

**WACC Inputs:**
- Risk-free rate: 4.0%
- Equity risk premium: 6.0%
- Beta: 1.2
- Cost of debt: 5.0%
- D/E ratio: 20%

**Balance Sheet:**
- Cash: $200M
- Debt: $1,000M
- Shares: 100M

Run the model:

```python
from dcf_model import DCFModel

model = DCFModel("TechCo Inc.", "TECH")

# Set up assumptions (see dcf_model.py for complete code)
model.set_historical_data(...)
model.set_revenue_assumptions([0.18, 0.15, 0.12, 0.10, 0.08])
model.set_operating_assumptions(...)
model.set_wacc_assumptions(...)
model.set_terminal_assumptions(growth_rate=0.03, ebitda_multiple=12.0)

# Build and calculate
model.build_projections()
model.calculate_dcf()
model.calculate_equity_value(cash=200, debt=1000, shares_outstanding=100)

# Display results
model.display_summary()
```

### Sensitivity Analysis

Test how valuation changes with different assumptions:

```python
# Create sensitivity table
wacc_range = [0.08, 0.09, 0.10, 0.11, 0.12]
tg_range = [0.02, 0.025, 0.03, 0.035, 0.04]

sensitivity = model.sensitivity_analysis(wacc_range, tg_range)
print(sensitivity)
```

### Best Practices

1. **Model Structure**
   - Separate inputs, calculations, and outputs
   - Use clear variable names
   - Document all assumptions

2. **Assumption Quality**
   - Revenue: Use industry research, management guidance
   - Margins: Compare to peers, historical trends
   - WACC: Market-based, current capital structure
   - Terminal growth: Usually 2-3%, never > GDP growth

3. **Sanity Checks**
   - Implied multiples (EV/Revenue, EV/EBITDA)
   - Margin trends
   - ROIC vs WACC
   - Terminal value as % of total value (typically 60-80%)

4. **Comparables Check**
   - Compare implied multiples to trading comps
   - Check if valuation is reasonable vs peers

### Exercises

#### Exercise 1: Build Your Own DCF
Value a company of your choice:
1. Find public company financials (use yfinance)
2. Set reasonable assumptions
3. Build complete DCF
4. Compare to actual market cap

#### Exercise 2: Sensitivity Analysis
- Create a 2-way sensitivity table (WACC vs Terminal Growth)
- Create a tornado chart showing assumption sensitivity
- Determine which assumptions drive value most

#### Exercise 3: Scenario Analysis
Build three scenarios:
- **Base Case**: Most likely assumptions
- **Bull Case**: Optimistic growth, margins
- **Bear Case**: Conservative assumptions

Compare the valuations.

### Additional Resources

- **dcf_model.py**: Complete model implementation
- **dcf_example.ipynb**: Interactive Jupyter notebook
- **dcf_template.xlsx**: Excel output template

### Next Steps

**🎊 CONGRATULATIONS! You built your first DCF model!**

**Before moving on, run this special celebration:**
```bash
python dcf_celebration.py
```

Your father has a very special message for you! 🎁💝

---

Continue to: `Module_05_LBO_Modeling/01_LBO_Overview.md`

---

**Estimated Time**: 4-5 hours
**Difficulty**: Intermediate
**Prerequisites**: Modules 1-3
