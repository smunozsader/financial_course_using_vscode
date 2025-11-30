# Module 07: Private Equity Fund Modeling 💼🚀

Welcome to **PE Fund Modeling** - where you learn to think like a GP (General Partner) managing a billion-dollar PE fund!

## 🎯 What You'll Learn

By the end of this module, you'll master:

- ✅ PE fund structure and economics (2/20 model)
- ✅ Portfolio company modeling (multiple deals)
- ✅ Fund-level returns (IRR, MOIC, DPI, TVPI)
- ✅ Waterfall distributions (who gets paid when)
- ✅ Carried interest calculations
- ✅ Complete fund performance analysis

**This is THE CORE of PE Club work!** 💰

---

## 🤔 What is PE Fund Modeling?

### The Simple Version

Imagine you and 9 friends pool $1M to buy houses:
- Each contributes $100K (Limited Partners)
- You manage the fund (General Partner)
- You buy 5 houses over 3 years
- You sell houses over next 3-5 years
- **The deal:** You get 20% of profits AFTER everyone gets their money back

**That's a PE fund!** 🏠

### The Finance Version

**Private Equity Fund** = Investment vehicle where:
- **LPs (Limited Partners):** Provide capital (pension funds, endowments, wealthy individuals)
- **GP (General Partner):** Manage the fund (PE firm like Blackstone, KKR)
- **Portfolio Companies:** The businesses you buy and improve
- **Returns:** Distributed via waterfall (specific order)

---

## 🏢 Real PE Fund Examples

### Example 1: Blackstone Capital Partners VIII (2016)
- **Fund Size:** $17.3 billion (largest PE fund at the time)
- **Strategy:** Large-cap buyouts
- **Target Returns:** 20%+ net IRR
- **Fee Structure:** 1.5% management fee, 20% carry
- **Performance:** 20.8% IRR (as of 2023) ✅

### Example 2: Vista Equity Partners Fund VII (2018)
- **Fund Size:** $16 billion
- **Strategy:** Enterprise software buyouts
- **Notable:** Invested in companies like Marketo, Mindbody
- **Performance:** Consistently 20%+ IRR
- **Secret:** Focus on ONE sector (software)

### Example 3: Apollo Fund IX (2017)
- **Fund Size:** $24.7 billion (mega-fund!)
- **Strategy:** Distressed and corporate carve-outs
- **LP Base:** Pension funds, sovereign wealth funds
- **Investment Period:** 5 years to deploy capital

---

## 💡 The PE Fund Formula (The 2/20 Model)

### Management Fees (The "2")

**Annual Fee:** 2% of committed capital (during investment period)

```
Example:
- Fund Size: $1B
- Management Fee: $1B × 2% = $20M per year
- Purpose: Pay salaries, rent, deal costs
- Who Gets It: GP (the PE firm)
```

**After investment period:** Usually 2% of invested capital (lower base)

### Carried Interest (The "20")

**Performance Fee:** 20% of profits AFTER returning capital to LPs

```
Example:
- LP Investment: $100M
- Fund Returns: $200M
- Profit: $100M
- LP Gets: $100M (capital back) + $80M (80% of profit) = $180M
- GP Gets: $20M (20% of profit) = "Carry"
```

**This is where GPs make REAL money!** 💰

---

## 📊 Key PE Fund Metrics

### 1. IRR (Internal Rate of Return)
**What:** Annualized return rate
**Target:** 20%+ for top-quartile funds
**Formula:** Complex (NPV = 0)

### 2. MOIC (Multiple on Invested Capital)
**What:** Total value ÷ Total invested
**Target:** 2.5x+ for top-quartile
**Formula:** Simple (Ending Value / Beginning Value)

### 3. DPI (Distributions to Paid-In Capital)
**What:** Actual cash returned to LPs ÷ Capital called
**Why Important:** "Realized" returns (not just paper gains)
**Formula:** Total Distributions / Total Contributions

### 4. TVPI (Total Value to Paid-In Capital)
**What:** (Distributions + Remaining Value) / Capital called
**Why Important:** Total value including unrealized gains
**Formula:** (Distributions + NAV) / Contributions

### 5. RVPI (Residual Value to Paid-In Capital)
**What:** Remaining portfolio value / Capital called
**Why Important:** Shows unrealized value still in fund
**Formula:** NAV / Contributions

**The Golden Formula:**
```
TVPI = DPI + RVPI
```

---

## 🎓 Module 07 Learning Path

We'll build complete PE fund modeling skills:

### 📁 Concept 1: Fund Structure & Economics
**What:** Understand how PE funds are structured
**Key Topics:**
- Limited Partnership (LP) structure
- Management fees vs carry
- Investment period vs harvest period
- Capital calls and distributions

```python
# Example: Fund structure
class PEFund:
    """
    Model a Private Equity fund structure
    
    This is the foundation of ALL PE modeling!
    """
    def __init__(self, fund_size, management_fee_rate=0.02, carry_rate=0.20):
        self.fund_size = fund_size
        self.management_fee_rate = management_fee_rate
        self.carry_rate = carry_rate
        self.lp_commitment = fund_size * 0.98  # 98% from LPs
        self.gp_commitment = fund_size * 0.02  # 2% from GP
        
    def calculate_annual_management_fee(self, year, invested_capital=None):
        """
        Management fee calculation
        
        Years 1-5 (investment period): 2% of committed capital
        Years 6+: 2% of invested capital
        """
        if year <= 5:
            fee_base = self.fund_size
        else:
            fee_base = invested_capital if invested_capital else self.fund_size
        
        return fee_base * self.management_fee_rate
```

### 📁 Concept 2: Portfolio Company Modeling
**What:** Model multiple LBO investments within the fund
**Key Topics:**
- Deal-by-deal analysis
- Entry and exit timing
- Portfolio diversification
- Winner vs loser deals

```python
# Example: Portfolio company
class PortfolioCompany:
    """
    Model individual portfolio company investment
    
    A fund typically has 8-15 portfolio companies
    """
    def __init__(self, name, entry_year, equity_invested, entry_ebitda, entry_multiple):
        self.name = name
        self.entry_year = entry_year
        self.equity_invested = equity_invested
        self.entry_ebitda = entry_ebitda
        self.entry_multiple = entry_multiple
        self.purchase_price = entry_ebitda * entry_multiple
        
    def calculate_exit_value(self, exit_year, exit_ebitda, exit_multiple, remaining_debt):
        """
        Calculate equity value at exit
        
        This is what determines if deal was successful!
        """
        exit_ev = exit_ebitda * exit_multiple
        equity_value = exit_ev - remaining_debt
        
        moic = equity_value / self.equity_invested
        holding_period = exit_year - self.entry_year
        irr = (moic ** (1/holding_period)) - 1
        
        return {
            'exit_value': equity_value,
            'moic': moic,
            'irr': irr,
            'holding_period': holding_period
        }
```

### 📁 Concept 3: Fund-Level Cash Flows
**What:** Aggregate all portfolio companies to fund level
**Key Topics:**
- Capital calls (when you invest)
- Distributions (when you exit)
- Management fees (ongoing)
- J-curve effect (early negative, then positive)

```python
# Example: Fund cash flows
def calculate_fund_cash_flows(portfolio_companies, management_fees):
    """
    Calculate complete fund-level cash flows
    
    This determines fund IRR and MOIC!
    """
    cash_flows = []
    
    for year in range(1, 11):  # 10-year fund life
        year_cf = 0
        
        # Capital calls (negative)
        for company in portfolio_companies:
            if company.entry_year == year:
                year_cf -= company.equity_invested
        
        # Distributions (positive)
        for company in portfolio_companies:
            if company.exit_year == year:
                year_cf += company.exit_value
        
        # Management fees (negative)
        year_cf -= management_fees[year]
        
        cash_flows.append(year_cf)
    
    return cash_flows
```

### 📁 Concept 4: Waterfall Distributions
**What:** Determine who gets paid when (LP vs GP)
**Key Topics:**
- Return of capital first
- Preferred return (hurdle rate)
- Catch-up provision
- Carried interest

```python
# Example: Waterfall distribution
def calculate_waterfall(total_proceeds, lp_contributed, gp_contributed, 
                        hurdle_rate=0.08, carry_rate=0.20):
    """
    PE waterfall distribution model
    
    THIS IS CRITICAL - Who gets what and when!
    
    Structure (European waterfall):
    1. Return of capital to LPs and GP
    2. Preferred return to LPs (8% hurdle)
    3. GP catch-up (to reach 20% of profits)
    4. Remaining split 80/20
    """
    remaining = total_proceeds
    distributions = {'LP': 0, 'GP': 0}
    
    # Tier 1: Return of capital
    capital_returned_lp = min(remaining, lp_contributed)
    distributions['LP'] += capital_returned_lp
    remaining -= capital_returned_lp
    
    capital_returned_gp = min(remaining, gp_contributed)
    distributions['GP'] += capital_returned_gp
    remaining -= capital_returned_gp
    
    # Tier 2: Preferred return to LPs (8% IRR)
    # Simplified: 8% per year on capital
    years = 5  # Average holding period
    preferred_return = lp_contributed * ((1 + hurdle_rate) ** years - 1)
    preferred_paid = min(remaining, preferred_return)
    distributions['LP'] += preferred_paid
    remaining -= preferred_paid
    
    # Tier 3: GP catch-up (to reach 20% of total profits)
    total_profit = total_proceeds - lp_contributed - gp_contributed
    gp_target = total_profit * carry_rate
    gp_shortfall = gp_target - distributions['GP']
    catchup = min(remaining, gp_shortfall)
    distributions['GP'] += catchup
    remaining -= catchup
    
    # Tier 4: Remaining split 80/20
    distributions['LP'] += remaining * 0.80
    distributions['GP'] += remaining * 0.20
    
    return distributions
```

### 📁 Concept 5: Fund Performance Metrics
**What:** Calculate all standard PE metrics
**Key Topics:**
- IRR calculation (fund-level)
- MOIC, DPI, TVPI, RVPI
- Quartile ranking
- Benchmark comparison

```python
# Example: Fund metrics
def calculate_fund_metrics(cash_flows, nav=0):
    """
    Calculate complete fund performance metrics
    
    These are what LPs use to evaluate funds!
    """
    from numpy import irr as calc_irr
    
    # Total contributions (capital calls)
    contributions = sum([abs(cf) for cf in cash_flows if cf < 0])
    
    # Total distributions (exits)
    distributions = sum([cf for cf in cash_flows if cf > 0])
    
    # Metrics
    metrics = {}
    
    # IRR
    metrics['IRR'] = calc_irr(cash_flows)
    
    # DPI (Distributions / Paid-In)
    metrics['DPI'] = distributions / contributions if contributions > 0 else 0
    
    # RVPI (Residual Value / Paid-In)
    metrics['RVPI'] = nav / contributions if contributions > 0 else 0
    
    # TVPI (Total Value / Paid-In)
    metrics['TVPI'] = metrics['DPI'] + metrics['RVPI']
    
    # MOIC (Total Value / Total Cost)
    total_value = distributions + nav
    metrics['MOIC'] = total_value / contributions if contributions > 0 else 0
    
    return metrics
```

### 📁 Concept 6: Scenario Analysis
**What:** Test fund returns under different scenarios
**Key Topics:**
- Base case vs upside vs downside
- Stress testing
- Monte Carlo simulation
- Risk assessment

```python
# Example: Scenario analysis
def run_fund_scenarios(portfolio_companies):
    """
    Run multiple scenarios for fund performance
    
    PE funds ALWAYS do this - returns are uncertain!
    """
    scenarios = {
        'Base Case': {
            'exit_multiple': 10.0,
            'ebitda_growth': 0.10,
            'debt_paydown': 0.50
        },
        'Upside Case': {
            'exit_multiple': 12.0,
            'ebitda_growth': 0.15,
            'debt_paydown': 0.60
        },
        'Downside Case': {
            'exit_multiple': 8.0,
            'ebitda_growth': 0.05,
            'debt_paydown': 0.30
        }
    }
    
    results = {}
    
    for scenario_name, assumptions in scenarios.items():
        # Recalculate all deals with new assumptions
        scenario_returns = []
        
        for company in portfolio_companies:
            exit_ebitda = company.entry_ebitda * (1 + assumptions['ebitda_growth']) ** 5
            exit_value = calculate_exit(
                exit_ebitda, 
                assumptions['exit_multiple'],
                assumptions['debt_paydown']
            )
            scenario_returns.append(exit_value)
        
        # Calculate fund metrics
        results[scenario_name] = calculate_fund_metrics(scenario_returns)
    
    return results
```

### 📁 Concept 7: GP Economics
**What:** Calculate GP compensation (fees + carry)
**Key Topics:**
- Management fee income
- Carried interest calculation
- Clawback provisions
- GP commitment returns

```python
# Example: GP economics
def calculate_gp_economics(fund_size, fund_irr, fund_moic):
    """
    Calculate total GP compensation
    
    THIS is why people work in PE!
    """
    gp_economics = {}
    
    # Management fees over 10 years
    annual_mgmt_fee = fund_size * 0.02
    total_mgmt_fees = annual_mgmt_fee * 10  # Simplified
    gp_economics['Management Fees'] = total_mgmt_fees
    
    # Carried interest (20% of profits above hurdle)
    lp_capital = fund_size * 0.98
    total_proceeds = lp_capital * fund_moic
    profit = total_proceeds - lp_capital
    
    # Assume hurdle cleared
    gp_economics['Carried Interest'] = profit * 0.20
    
    # GP commitment returns (2% of fund)
    gp_capital = fund_size * 0.02
    gp_economics['GP Commitment Return'] = gp_capital * (fund_moic - 1)
    
    # Total GP value
    gp_economics['Total GP Value'] = sum(gp_economics.values())
    
    # As % of fund profits
    gp_economics['GP % of Profits'] = (gp_economics['Total GP Value'] / profit) * 100
    
    return gp_economics
```

### 📁 Concept 8: Complete Fund Model
**What:** Integrate everything into one comprehensive model
**Why:** This is what PE firms actually use!

```python
# Example: Complete PE fund model
class CompletePEFund:
    """
    Complete Private Equity fund model
    
    This is production-quality fund modeling!
    """
    def __init__(self, fund_name, fund_size, vintage_year):
        self.fund_name = fund_name
        self.fund_size = fund_size
        self.vintage_year = vintage_year
        self.portfolio = []
        self.cash_flows = [0] * 15  # 15-year timeframe
        
    def add_investment(self, company):
        """Add portfolio company investment"""
        self.portfolio.append(company)
        
    def run_fund_model(self):
        """
        Run complete fund analysis
        
        Returns full fund performance report
        """
        # 1. Calculate portfolio company returns
        # 2. Aggregate to fund level
        # 3. Calculate management fees
        # 4. Run waterfall
        # 5. Calculate metrics
        # 6. Generate report
        
        report = {
            'Fund Name': self.fund_name,
            'Vintage': self.vintage_year,
            'Fund Size': self.fund_size,
            'Portfolio Count': len(self.portfolio),
            'Gross IRR': self.calculate_gross_irr(),
            'Net IRR': self.calculate_net_irr(),
            'Gross MOIC': self.calculate_gross_moic(),
            'Net MOIC': self.calculate_net_moic(),
            'DPI': self.calculate_dpi(),
            'TVPI': self.calculate_tvpi(),
            'GP Carry': self.calculate_carry(),
            'LP Returns': self.calculate_lp_returns()
        }
        
        return report
```

---

## 🎯 Practice Exercises

### Exercise 1: Single Fund Quick Analysis
Given a $500M fund with these investments:
- Deal 1: Invested $100M, exited at 3.0x MOIC in Year 5
- Deal 2: Invested $150M, exited at 2.5x MOIC in Year 6
- Deal 3: Invested $100M, exited at 2.0x MOIC in Year 7
- Deal 4: Invested $150M, still holding (NAV = $300M)

**Calculate:**
1. Fund-level MOIC (gross)
2. DPI and RVPI
3. TVPI
4. Estimated gross IRR

### Exercise 2: GP vs LP Economics
$1B fund achieves 2.5x MOIC over 6 years.
- Management fees: 2% for 10 years
- Carry: 20% above 8% hurdle
- GP commitment: 2% of fund

**Calculate:**
1. Total LP proceeds
2. Total GP proceeds (fees + carry)
3. GP % of total profits
4. LP net IRR vs GP returns

### Exercise 3: Waterfall Distribution
Fund raised $500M, achieved these results:
- Capital called: $500M
- Proceeds from exits: $1.2B
- Hurdle rate: 8% IRR
- Carry: 20%
- Average hold: 5 years

**Calculate distribution to:**
1. Tier 1: Return of capital
2. Tier 2: Preferred return
3. Tier 3: GP catch-up
4. Tier 4: Final split

### Exercise 4: Complete Fund Model
Build a complete fund model:
- Fund Size: $750M
- Investment period: Years 1-4
- Exit period: Years 4-8
- 10 portfolio companies
- Mix of winners (3.0x+) and losers (0.5x)
- Calculate full fund metrics

---

## 💼 Real PE Fund Modeling at PE Club

When modeling funds at PE Club, focus on:

### For Fund Formation:
- **Fund Size:** How much can you raise?
- **Fee Structure:** 2/20 or negotiate different?
- **Investment Strategy:** What types of deals?
- **Target Returns:** 20%+ net IRR to LPs

### For Fund Performance:
- **Portfolio Construction:** 8-15 companies
- **Diversification:** Sector, geography, vintage
- **Exit Strategy:** Strategic vs secondary
- **Timing:** J-curve management

### For LP Reporting:
- **Quarterly Reports:** NAV updates
- **Annual Reports:** Full performance
- **Capital Calls:** When you need money
- **Distributions:** When you return money

---

## 📚 PE Fund Best Practices

### 1. The Power Law in PE
**Reality:** 20% of deals generate 80% of returns

```
Typical $1B fund with 10 deals:
- 2 "home runs" (5.0x MOIC): Drive most returns
- 3 "good" deals (2.5x MOIC): Meet expectations
- 3 "okay" deals (1.5x MOIC): Slight winners
- 2 "losers" (0.5x MOIC): Lose money

Result: Fund still achieves 2.5x MOIC!
```

**Lesson:** You don't need ALL deals to work, just a few big winners!

### 2. The J-Curve Effect
**What:** Fund returns are negative early, then positive

```
Year 1-3: Negative (investing + fees, no exits)
Year 4-6: Neutral (first exits)
Year 7+: Positive (mature exits)
```

**Implication:** Don't panic in Year 2!

### 3. Diversification Strategies

**By Sector:**
- Technology: 30%
- Healthcare: 25%
- Industrials: 20%
- Consumer: 15%
- Financial Services: 10%

**By Deal Size:**
- Large ($100M+): 3-5 deals
- Mid ($50-100M): 4-6 deals
- Small (<$50M): 2-4 deals

### 4. Exit Timing
**Options:**
- Strategic sale: Often highest price (25-40% premium)
- Secondary sale: Quick exit, lower premium
- IPO: Best for large companies, 3-5 year process
- Recapitalization: Take some chips off table

**Rule:** Start exit process in Year 3-4 of hold

### 5. Fee Negotiation
**Standard:** 2% management fee, 20% carry
**Large LPs can negotiate:**
- 1.5% management fee
- Reduced carry (15-18%)
- Lower hurdle rate
- Fee offsets (transaction fees credited)

---

## 🎓 Module 07 Summary

**You'll Master:**
1. ✅ PE fund structure (LP/GP, fees, carry)
2. ✅ Portfolio company modeling (8-15 deals)
3. ✅ Fund-level cash flows (capital calls, distributions)
4. ✅ Waterfall distributions (who gets what)
5. ✅ Performance metrics (IRR, MOIC, DPI, TVPI)
6. ✅ GP economics (total compensation)
7. ✅ Scenario analysis (base/bull/bear)
8. ✅ Complete fund model integration

**Real-World Application:**
- Model PE fund performance
- Evaluate fund manager compensation
- Compare funds (quartile ranking)
- Pitch to LPs for fundraising
- Manage existing funds at PE Club

---

## 🚀 Let's Get Started!

**This is THE module for PE professionals!**

Work through the exercises to build complete fund models.

**Time Investment:** 5-7 hours for mastery

**Outcome:** You'll model PE funds like a Blackstone analyst! 💼

---

## 🎯 Special Challenge

After completing this module:

**Build a complete fund model for PE Club:**
- Fund size: €500M
- Strategy: European mid-market buyouts
- 10 portfolio companies
- Target: 22% net IRR to LPs
- Fee structure: 1.75% / 20%

**Present to your team!** 🎉

---

**Ready to master PE fund modeling?**

This is what separates good PE analysts from GREAT ones! 💪

---

*Module 07 - Private Equity Fund Modeling*  
*Financial Modeling Course for PE Professionals*  
*Created for Mauricio at PE Club, Brussels* 🇧🇪
