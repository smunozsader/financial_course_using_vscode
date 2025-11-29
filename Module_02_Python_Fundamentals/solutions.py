"""
Solutions to Python Fundamentals Practice Exercises
"""

# Exercise 1: Revenue Model
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
    revenues = [base_revenue]
    
    for growth_rate in growth_rates:
        next_revenue = revenues[-1] * (1 + growth_rate)
        revenues.append(next_revenue)
    
    return revenues[1:]  # Return projected years only


# Test Exercise 1
print("=" * 60)
print("EXERCISE 1: Revenue Projections")
print("=" * 60)

base = 100
growth = [0.15, 0.12, 0.10, 0.08, 0.08]
projections = project_revenue(base, growth)

print(f"Base Revenue: ${base}M")
print(f"\nYear | Growth | Revenue")
print("-" * 30)
for i, (g, rev) in enumerate(zip(growth, projections), 1):
    print(f"{i:4} | {g:5.1%}  | ${rev:7.2f}M")


# Exercise 2: LBO Returns Calculator
def lbo_moic(entry_value, exit_value):
    """Calculate Multiple on Invested Capital"""
    return exit_value / entry_value


def approximate_irr(moic, years):
    """
    Approximate IRR from MOIC
    IRR ≈ (MOIC ^ (1/years)) - 1
    """
    return moic ** (1 / years) - 1


# Test Exercise 2
print("\n" + "=" * 60)
print("EXERCISE 2: LBO Returns Analysis")
print("=" * 60)

# Given data
entry_ebitda = 62.5
exit_ebitda = 85
entry_multiple = 8
exit_multiple = 10
holding_period = 5

entry_value = entry_ebitda * entry_multiple
exit_value = exit_ebitda * exit_multiple

moic = lbo_moic(entry_value, exit_value)
irr = approximate_irr(moic, holding_period)

print(f"\nEntry Valuation: ${entry_value:.1f}M ({entry_multiple}x ${entry_ebitda}M EBITDA)")
print(f"Exit Valuation:  ${exit_value:.1f}M ({exit_multiple}x ${exit_ebitda}M EBITDA)")
print(f"Holding Period:  {holding_period} years")
print(f"\nMOIC: {moic:.2f}x")
print(f"IRR:  {irr:.1%}")


# Exercise 3: DCF Model
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
    # PV of projected cash flows
    pv_cash_flows = sum(
        cf / (1 + discount_rate) ** (year + 1)
        for year, cf in enumerate(cash_flows)
    )
    
    # PV of terminal value
    terminal_period = len(cash_flows)
    pv_terminal = terminal_value / (1 + discount_rate) ** terminal_period
    
    # Enterprise value
    enterprise_value = pv_cash_flows + pv_terminal
    
    return enterprise_value


# Test Exercise 3
print("\n" + "=" * 60)
print("EXERCISE 3: DCF Valuation")
print("=" * 60)

# Sample company
fcf_projections = [50, 55, 61, 68, 75]  # 5-year projections
wacc = 0.10
terminal_fcf = 75
terminal_growth = 0.03
terminal_val = terminal_fcf * (1 + terminal_growth) / (wacc - terminal_growth)

ev = simple_dcf(fcf_projections, wacc, terminal_val)

print(f"\nFree Cash Flow Projections:")
for year, fcf in enumerate(fcf_projections, 1):
    pv_factor = 1 / (1 + wacc) ** year
    pv = fcf * pv_factor
    print(f"  Year {year}: ${fcf}M (PV: ${pv:.1f}M)")

print(f"\nTerminal Value: ${terminal_val:.1f}M")
print(f"  Terminal Growth: {terminal_growth:.1%}")
print(f"  PV of Terminal: ${terminal_val / (1 + wacc)**len(fcf_projections):.1f}M")

print(f"\nWACC: {wacc:.1%}")
print(f"Enterprise Value: ${ev:.1f}M")


# Bonus: Complete Financial Model Class
class FinancialModel:
    """
    Comprehensive financial model with DCF capabilities
    """
    
    def __init__(self, name, base_revenue, revenue_growth_rates, 
                 ebitda_margin, tax_rate, capex_pct_revenue, 
                 nwc_pct_revenue, discount_rate):
        self.name = name
        self.base_revenue = base_revenue
        self.revenue_growth_rates = revenue_growth_rates
        self.ebitda_margin = ebitda_margin
        self.tax_rate = tax_rate
        self.capex_pct_revenue = capex_pct_revenue
        self.nwc_pct_revenue = nwc_pct_revenue
        self.discount_rate = discount_rate
        
        # Build projections
        self.build_model()
    
    def build_model(self):
        """Build financial projections"""
        years = len(self.revenue_growth_rates)
        
        # Revenue projections
        self.revenues = []
        current_rev = self.base_revenue
        for growth in self.revenue_growth_rates:
            current_rev *= (1 + growth)
            self.revenues.append(current_rev)
        
        # EBITDA projections
        self.ebitdas = [rev * self.ebitda_margin for rev in self.revenues]
        
        # NOPAT (simplified: EBITDA * (1 - tax))
        self.nopats = [ebitda * (1 - self.tax_rate) for ebitda in self.ebitdas]
        
        # CapEx
        self.capex = [rev * self.capex_pct_revenue for rev in self.revenues]
        
        # Change in NWC
        self.nwc_changes = []
        prev_nwc = self.base_revenue * self.nwc_pct_revenue
        for rev in self.revenues:
            current_nwc = rev * self.nwc_pct_revenue
            self.nwc_changes.append(current_nwc - prev_nwc)
            prev_nwc = current_nwc
        
        # Free Cash Flow
        self.fcfs = [
            nopat - capex - nwc_change
            for nopat, capex, nwc_change in zip(self.nopats, self.capex, self.nwc_changes)
        ]
    
    def calculate_dcf(self, terminal_growth_rate):
        """Calculate enterprise value"""
        # PV of cash flows
        pv_fcfs = [
            fcf / (1 + self.discount_rate) ** (year + 1)
            for year, fcf in enumerate(self.fcfs)
        ]
        
        # Terminal value
        terminal_fcf = self.fcfs[-1] * (1 + terminal_growth_rate)
        terminal_value = terminal_fcf / (self.discount_rate - terminal_growth_rate)
        pv_terminal = terminal_value / (1 + self.discount_rate) ** len(self.fcfs)
        
        return sum(pv_fcfs) + pv_terminal
    
    def display(self):
        """Display model output"""
        print(f"\n{'='*70}")
        print(f"FINANCIAL MODEL: {self.name}")
        print(f"{'='*70}")
        print(f"\n{'Year':<6} {'Revenue':>10} {'EBITDA':>10} {'NOPAT':>10} {'FCF':>10}")
        print("-" * 70)
        
        for year, (rev, ebitda, nopat, fcf) in enumerate(
            zip(self.revenues, self.ebitdas, self.nopats, self.fcfs), 1
        ):
            print(f"{year:<6} ${rev:>9.1f}M ${ebitda:>9.1f}M ${nopat:>9.1f}M ${fcf:>9.1f}M")


# Test the complete model
print("\n" + "=" * 60)
print("BONUS: Complete Financial Model")
print("=" * 60)

model = FinancialModel(
    name="TechCo",
    base_revenue=100,
    revenue_growth_rates=[0.20, 0.18, 0.15, 0.12, 0.10],
    ebitda_margin=0.25,
    tax_rate=0.25,
    capex_pct_revenue=0.05,
    nwc_pct_revenue=0.10,
    discount_rate=0.12
)

model.display()

terminal_growth = 0.03
ev = model.calculate_dcf(terminal_growth)
print(f"\nTerminal Growth Rate: {terminal_growth:.1%}")
print(f"Discount Rate (WACC): {model.discount_rate:.1%}")
print(f"\nEnterprise Value: ${ev:.1f}M")

print("\n" + "=" * 60)
print("✅ All exercises completed!")
print("=" * 60)
