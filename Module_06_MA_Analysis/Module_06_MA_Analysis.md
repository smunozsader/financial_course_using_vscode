# Module 06: M&A Analysis 🤝💼

Welcome to the world of **Mergers & Acquisitions** - where companies buy other companies to create value!

## 🎯 What You'll Learn

By the end of this module, you'll be able to:

- ✅ Analyze M&A deals like an Investment Banker
- ✅ Calculate accretion/dilution analysis
- ✅ Model merger consequences (EPS impact)
- ✅ Perform synergy analysis
- ✅ Value acquisition premiums
- ✅ Build complete merger models

**This is CRITICAL for IB analysts** - M&A is where the big deals happen! 💰

---

## 🤔 What is M&A Analysis?

### The Simple Version

Imagine you own a coffee shop making $100K/year profit. A bigger coffee chain wants to buy you for $1M.

**Questions you need to answer:**
1. Is $1M a fair price? (Valuation)
2. Will the buyer's shareholders benefit? (Accretion/Dilution)
3. What happens to your employees? (Integration)
4. Can combining both shops create more value? (Synergies)

**That's M&A analysis!** 🎯

### The Finance Version

**M&A Analysis** is evaluating whether acquiring another company creates value for shareholders.

**Two perspectives:**
- **Buyer (Acquirer):** "Will this deal increase our earnings per share?"
- **Seller (Target):** "Are we getting a fair premium for our shareholders?"

---

## 🏢 Real-World M&A Examples

### Example 1: Microsoft Acquires LinkedIn (2016)
- **Deal Size:** $26.2 billion
- **Premium:** 50% above market price
- **Rationale:** Access to 400M professional network
- **Synergies:** Integrate LinkedIn with Office 365
- **Result:** ✅ Successful - LinkedIn revenue doubled

### Example 2: Disney Acquires 21st Century Fox (2019)
- **Deal Size:** $71.3 billion
- **Premium:** 35% above market price
- **Rationale:** Content library for Disney+
- **Synergies:** $2B+ cost savings
- **Result:** ✅ Successful - Powered Disney+ growth

### Example 3: HP Acquires Autonomy (2011)
- **Deal Size:** $11.1 billion
- **Premium:** 64% above market price
- **Result:** ❌ DISASTER - Wrote down $8.8B (79% loss!)
- **Lesson:** Overpaying destroys value!

---

## 💡 The M&A Formula (IB Secret Sauce)

### Step 1: Is the Deal Accretive?

**Accretive** = Buyer's EPS goes UP after acquisition
**Dilutive** = Buyer's EPS goes DOWN after acquisition

```
New Combined EPS > Old Acquirer EPS = ✅ ACCRETIVE (Good!)
New Combined EPS < Old Acquirer EPS = ❌ DILUTIVE (Bad!)
```

### Step 2: What's the Fair Price?

Use **multiple methods** (like DCF module):
- Comparable Companies (Trading Comps)
- Precedent Transactions (Deal Comps)
- DCF Valuation
- Breakup Value

### Step 3: What are the Synergies?

**Revenue Synergies:** (Harder to achieve)
- Cross-selling products
- Entering new markets
- Combining customer bases

**Cost Synergies:** (Easier to achieve)
- Eliminating duplicate functions
- Bulk purchasing power
- Shared infrastructure

**Rule of thumb:** Banks give 0% credit to revenue synergies, 70% credit to cost synergies

---

## 📊 THE KEY METRIC: Accretion/Dilution Analysis

This is THE most important analysis in M&A!

### The Setup

**Acquirer Company (BuyerCo):**
- Net Income: $100M
- Shares Outstanding: 50M
- **EPS: $2.00**
- Stock Price: $40
- P/E Ratio: 20x

**Target Company (TargetCo):**
- Net Income: $20M
- Shares Outstanding: 10M
- EPS: $2.00
- Stock Price: $30
- P/E Ratio: 15x

**Deal Terms:**
- BuyerCo offers $35/share (17% premium)
- Total consideration: $350M
- Payment method: 50% cash, 50% stock

### The Analysis

**Step 1: Calculate new shares issued**
- Stock consideration: $175M / $40 = 4.375M new shares

**Step 2: Calculate combined earnings**
- BuyerCo: $100M
- TargetCo: $20M
- **Combined: $120M**

**Step 3: Calculate new EPS**
- New shares: 50M + 4.375M = 54.375M
- New EPS: $120M / 54.375M = **$2.21**

**Step 4: Accretion/Dilution**
- Old EPS: $2.00
- New EPS: $2.21
- **Accretion: +10.3%** ✅ GOOD DEAL!

---

## 🎓 Module 06 Learning Path

We'll build your M&A skills progressively:

### 📁 File 1: `01_comparable_companies.py`
**What:** Find similar companies and calculate valuation multiples
**Why:** Establish baseline valuation for target
**Key Concepts:**
- Screening comparables
- EV/EBITDA, P/E multiples
- Median vs mean multiples

```python
# Example: Find tech company comparables
import yfinance as yf
import pandas as pd

def find_comparables(sector='Technology', min_market_cap=1_000_000_000):
    """
    Find comparable public companies for valuation
    
    This is Step 1 in any M&A process!
    """
    # Screen companies by sector and size
    # Calculate trading multiples
    # Rank by relevance
    pass
```

### 📁 File 2: `02_precedent_transactions.py`
**What:** Analyze historical M&A deals in the sector
**Why:** Understand what multiples buyers actually paid
**Key Concepts:**
- Control premium
- Deal multiples vs trading multiples
- Sector-specific trends

```python
# Example: Tech M&A premiums
def analyze_precedent_deals(sector='Technology', years=5):
    """
    Analyze historical M&A transactions
    
    Shows what REAL buyers paid (not just trading prices)
    Deal multiples are typically 20-40% higher than trading multiples
    """
    transactions = {
        'Microsoft/LinkedIn': {'EV/Revenue': 7.8, 'Premium': 50},
        'Salesforce/Slack': {'EV/Revenue': 26.0, 'Premium': 55},
        # ... more deals
    }
    
    # Calculate median premium
    # Calculate median multiples
    # Compare to current target
    pass
```

### 📁 File 3: `03_target_valuation.py`
**What:** Value the target company using multiple methods
**Why:** Establish fair value range BEFORE negotiations
**Key Concepts:**
- Valuation range (min/max)
- Triangulation methodology
- Walk-away price

```python
# Example: Multi-method valuation
def value_target(target_financials):
    """
    Value acquisition target using 3 methods
    
    NEVER rely on just one valuation method!
    """
    # Method 1: Trading comps
    comp_value = target_ebitda * median_comp_multiple
    
    # Method 2: Transaction comps
    deal_value = target_ebitda * median_deal_multiple
    
    # Method 3: DCF
    dcf_value = calculate_dcf(target_fcf, wacc)
    
    # Final range: Min to Max of all methods
    valuation_range = (min(...), max(...))
    return valuation_range
```

### 📁 File 4: `04_offer_structure.py`
**What:** Design the acquisition offer (cash vs stock vs mix)
**Why:** Payment method affects accretion/dilution dramatically
**Key Concepts:**
- Cash offer (certain, but uses balance sheet)
- Stock offer (shares risk, but preserves cash)
- Mixed offer (most common)

```python
# Example: Compare payment methods
def compare_payment_methods(target_price=1_000, acquirer_stock_price=50):
    """
    Cash vs Stock vs Mixed offers
    
    THIS IS CRITICAL - Payment method changes everything!
    """
    scenarios = {
        'All Cash': {
            'Cash Paid': target_price,
            'Shares Issued': 0,
            'Balance Sheet Impact': -target_price
        },
        'All Stock': {
            'Cash Paid': 0,
            'Shares Issued': target_price / acquirer_stock_price,
            'Balance Sheet Impact': 0
        },
        '50/50 Mix': {
            'Cash Paid': target_price / 2,
            'Shares Issued': (target_price / 2) / acquirer_stock_price,
            'Balance Sheet Impact': -target_price / 2
        }
    }
    return scenarios
```

### 📁 File 5: `05_accretion_dilution.py`
**What:** Calculate impact on acquirer's EPS
**Why:** THE KEY METRIC - Will shareholders approve?
**Key Concepts:**
- Pro forma combined company
- EPS accretion/dilution %
- Breakeven analysis

```python
# Example: Full accretion/dilution analysis
def accretion_dilution_analysis(acquirer, target, offer_price, payment_mix):
    """
    THE MOST IMPORTANT M&A ANALYSIS!
    
    This determines if deal gets done.
    - Accretive = CEO does deal
    - Dilutive = CEO walks away (usually)
    """
    # Step 1: Calculate shares issued (if stock deal)
    if payment_mix['stock_percent'] > 0:
        new_shares = (offer_price * payment_mix['stock_percent']) / acquirer.stock_price
    else:
        new_shares = 0
    
    # Step 2: Combined earnings
    combined_earnings = acquirer.net_income + target.net_income
    
    # Step 3: New EPS
    new_total_shares = acquirer.shares + new_shares
    new_eps = combined_earnings / new_total_shares
    
    # Step 4: Accretion/Dilution
    accretion = (new_eps - acquirer.eps) / acquirer.eps
    
    print(f"Old EPS: ${acquirer.eps:.2f}")
    print(f"New EPS: ${new_eps:.2f}")
    print(f"Accretion: {accretion*100:+.1f}%")
    
    if accretion > 0:
        print("✅ ACCRETIVE - Good for shareholders!")
    else:
        print("❌ DILUTIVE - Bad for shareholders!")
    
    return {'new_eps': new_eps, 'accretion_percent': accretion}
```

### 📁 File 6: `06_synergy_analysis.py`
**What:** Estimate value creation from combining companies
**Why:** Synergies justify paying a premium
**Key Concepts:**
- Cost synergies (headcount, facilities, IT)
- Revenue synergies (cross-sell, new markets)
- Dis-synergies (integration costs, culture clash)

```python
# Example: Synergy estimation
def estimate_synergies(acquirer, target):
    """
    Estimate value creation from merger
    
    BE CONSERVATIVE! Most companies overestimate synergies.
    """
    # Cost synergies (easier to achieve)
    cost_synergies = {
        'Headcount Reduction': target.sg_and_a * 0.15,  # 15% of SG&A
        'Facilities Consolidation': target.rent * 0.30,  # 30% savings
        'IT Systems': target.it_budget * 0.40,  # 40% savings
        'Procurement': target.cogs * 0.05  # 5% bulk discount
    }
    
    # Revenue synergies (harder to achieve - be skeptical!)
    revenue_synergies = {
        'Cross-Selling': target.revenue * 0.10,  # 10% uplift
        'New Markets': acquirer.revenue * 0.05  # 5% from target channels
    }
    
    # Integration costs (one-time)
    integration_costs = {
        'Severance': cost_synergies['Headcount Reduction'] * 1.5,
        'Systems Integration': 50_000_000,
        'Rebranding': 10_000_000
    }
    
    # NPV of synergies
    annual_synergies = sum(cost_synergies.values()) + sum(revenue_synergies.values()) * 0.5  # Haircut revenue
    one_time_costs = sum(integration_costs.values())
    
    npv_synergies = (annual_synergies / wacc) - one_time_costs
    
    return {
        'Annual Synergies': annual_synergies,
        'One-Time Costs': one_time_costs,
        'NPV of Synergies': npv_synergies
    }
```

### 📁 File 7: `07_merger_consequences.py`
**What:** Model complete pro forma financial statements
**Why:** Full picture of combined company
**Key Concepts:**
- Pro forma income statement
- Pro forma balance sheet
- Goodwill calculation
- Purchase price allocation

```python
# Example: Pro forma financials
def create_pro_forma_financials(acquirer, target, purchase_price):
    """
    Build complete pro forma (as if already merged)
    
    This is what the combined company looks like Day 1 post-merger.
    """
    # Pro Forma Income Statement
    pro_forma_is = {
        'Revenue': acquirer.revenue + target.revenue,
        'COGS': acquirer.cogs + target.cogs,
        'Gross Profit': '...',
        'SG&A': acquirer.sga + target.sga - synergies,  # Less synergies!
        'EBITDA': '...',
        'D&A': acquirer.da + target.da + new_amortization,  # PPA creates new D&A
        'EBIT': '...',
        'Interest': new_interest_expense,  # If debt-financed
        'EBT': '...',
        'Tax': '...',
        'Net Income': '...'
    }
    
    # Pro Forma Balance Sheet
    # Calculate goodwill
    fair_value_of_assets = target.book_value * 1.2  # Usually assets revalued up
    goodwill = purchase_price - fair_value_of_assets
    
    pro_forma_bs = {
        'Cash': acquirer.cash - cash_paid,
        'Goodwill': acquirer.goodwill + goodwill,  # BIG NUMBER!
        'Total Assets': '...',
        'Debt': acquirer.debt + new_debt,
        'Equity': '...'
    }
    
    return pro_forma_is, pro_forma_bs
```

### 📁 File 8: `08_complete_merger_model.py`
**What:** Full end-to-end M&A analysis
**Why:** Bring it all together like a real IB pitch book
**Key Concepts:**
- Executive summary
- Valuation summary
- Accretion/dilution
- Synergies
- Financing structure
- Risk factors

```python
# Example: Complete merger model
class MergerModel:
    """
    Complete M&A analysis model
    
    This is what you'd present to the Board of Directors!
    """
    
    def __init__(self, acquirer, target):
        self.acquirer = acquirer
        self.target = target
        
    def run_full_analysis(self, offer_price_per_share, payment_method):
        """
        Run complete M&A analysis
        """
        results = {}
        
        # 1. Valuation
        results['valuation'] = self.value_target()
        
        # 2. Premium Analysis
        results['premium'] = self.calculate_premium(offer_price_per_share)
        
        # 3. Accretion/Dilution
        results['accretion'] = self.accretion_dilution(offer_price_per_share, payment_method)
        
        # 4. Synergies
        results['synergies'] = self.estimate_synergies()
        
        # 5. Pro Forma Financials
        results['pro_forma'] = self.create_pro_forma()
        
        # 6. Financing
        results['financing'] = self.design_financing_structure()
        
        # 7. Recommendation
        results['recommendation'] = self.make_recommendation()
        
        return results
    
    def make_recommendation(self):
        """
        Final recommendation: DO THE DEAL or WALK AWAY?
        """
        if self.is_accretive and self.premium < 0.30 and self.synergies_achievable:
            return "✅ RECOMMEND PROCEEDING - Deal creates shareholder value"
        else:
            return "❌ DO NOT PROCEED - Deal destroys shareholder value"
```

---

## 🎯 Practice Exercises

### Exercise 1: Quick Accretion/Dilution Check
Given:
- Acquirer: $200M earnings, 100M shares, $50/share
- Target: $30M earnings, 20M shares, $40/share
- Offer: $50/share (25% premium), all stock

**Calculate:**
1. New shares issued
2. Combined EPS
3. Accretion/dilution %

### Exercise 2: Valuation Range
Value a target company using:
- Trading comps: 8.0x EBITDA
- Deal comps: 9.5x EBITDA
- DCF: $500M enterprise value
- Target EBITDA: $50M

What's your valuation range?

### Exercise 3: Synergy Analysis
Two retailers merge:
- Combined revenue: $2B
- Combined SG&A: $400M
- Combined headcount: 10,000 employees

Estimate:
- Headcount synergies (10% reduction)
- Store closure synergies (15% of stores)
- IT synergies (combine systems)

What's the NPV of synergies?

### Exercise 4: Complete Merger Model
Build a complete merger model:
- Acquirer: TechCo ($1B revenue, $100M EBITDA)
- Target: StartupCo ($200M revenue, $30M EBITDA)
- Offer: 1.2x revenue multiple
- Payment: 60% cash, 40% stock
- Synergies: $20M annually

Should TechCo do the deal?

---

## 💼 Real M&A at PE Club

When analyzing M&A deals at PE Club, focus on:

### For Strategic Buyers (Corporations):
- **Accretion/Dilution:** Must be accretive Year 1 or Year 2
- **Strategic Fit:** Does target fill a gap?
- **Synergies:** Can you achieve $X in cost saves?
- **Integration Risk:** Can you actually merge them?

### For Financial Buyers (PE Firms):
- **Entry Multiple:** Is it attractive?
- **Exit Multiple:** Can you sell higher?
- **Cash Flow:** Can service debt?
- **Value Creation:** EBITDA growth + multiple expansion?

**Key Difference:**
- **Strategic buyers** care about EPS accretion
- **Financial buyers** care about IRR/MOIC

---

## 📚 M&A Best Practices

### 1. Always Use Multiple Valuation Methods
Never rely on just DCF or just comps. Triangulate!

### 2. Be Conservative on Synergies
- Revenue synergies: Assume ZERO (too risky)
- Cost synergies: Assume 60-70% achievement
- Timing: Takes 2-3 years to realize

### 3. Consider All-In Cost
```
Total Cost = Purchase Price 
           + Assumed Debt
           + Transaction Fees (2-3%)
           + Integration Costs
           - Synergies (PV)
```

### 4. Scenario Analysis
Always run:
- **Base Case:** Expected synergies
- **Bull Case:** All synergies achieved + revenue upside
- **Bear Case:** No synergies, integration problems

### 5. Walk-Away Price
Determine MAX price BEFORE negotiations:
```
Walk-Away Price = DCF Value + 30% premium
```
If price exceeds this, WALK AWAY! 🚶‍♂️

---

## 🎓 Module 06 Summary

**You'll Master:**
1. ✅ Comparable companies analysis
2. ✅ Precedent transactions analysis
3. ✅ Target valuation (multiple methods)
4. ✅ Offer structure (cash/stock/mix)
5. ✅ **Accretion/Dilution analysis** (THE KEY!)
6. ✅ Synergy estimation
7. ✅ Pro forma financials
8. ✅ Complete merger model

**Real-World Application:**
- Analyze M&A deals in the news
- Advise companies on acquisitions
- Evaluate PE platform add-ons
- Present to Boards of Directors

---

## 🚀 Let's Get Started!

Work through files 01-08 in order. Each builds on the previous one.

**Time Investment:** 4-6 hours for complete mastery

**Outcome:** You'll be able to analyze M&A deals like a Goldman Sachs M&A analyst! 💼

---

## 🎯 Special Challenge

After completing this module, try this:

**Pick a recent M&A deal from the news:**
- Google "recent M&A deals"
- Find one with public financials
- Build a complete merger model
- Calculate if it was accretive/dilutive
- Estimate synergies
- Write your recommendation

**Share your analysis at PE Club!** 🎉

---

**Next Steps:**
1. Start with `01_comparable_companies.py`
2. Work through each file sequentially
3. Complete practice exercises
4. Build your own merger model!

**Let's master M&A! You've got this!** 💪🚀

---

*Module 06 - M&A Analysis*  
*Financial Modeling Course for PE/IB Professionals*  
*Created for Mauricio at PE Club, Brussels* 🇧🇪
