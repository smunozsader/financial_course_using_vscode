"""
Solutions to Module 02 Practice Exercises
==========================================

These are complete solutions to the practice exercises in Module 02.

IMPORTANT: Try solving the exercises yourself first!
The learning happens when you struggle through the problem.

Use these solutions to:
- Check your work
- Understand different approaches
- Learn best practices
"""

# Exercise 1: Revenue Projection Function
# ========================================

def project_revenue(base_revenue, growth_rates):
    """
    Project revenue over multiple years with varying growth rates.
    
    Parameters:
    -----------
    base_revenue : float
        Starting revenue (Year 0)
    growth_rates : list
        Annual growth rate for each year (e.g., [0.15, 0.12, 0.10])
    
    Returns:
    --------
    list
        Revenue projections for each year
    
    Example:
    --------
    >>> project_revenue(100, [0.15, 0.12, 0.10])
    [115.0, 128.8, 141.68]
    """
    revenues = []
    current_revenue = base_revenue
    
    for growth_rate in growth_rates:
        current_revenue = current_revenue * (1 + growth_rate)
        revenues.append(current_revenue)
    
    return revenues


# Test Exercise 1
print("=" * 70)
print("EXERCISE 1: Revenue Projection Function")
print("=" * 70)

base = 100
growth = [0.15, 0.12, 0.10, 0.08, 0.06]
revenues = project_revenue(base, growth)

print("\nRevenue Projections:")
print(f"Base Year: ${base:.2f}M")
print("-" * 40)
for year, rev in enumerate(revenues, 1):
    yoy_growth = growth[year-1]
    print(f"Year {year}: ${rev:>8.2f}M  (Growth: {yoy_growth:>5.1%})")

print("\n")


# Exercise 2: LBO Returns Calculator
# ===================================

def calculate_lbo_returns(entry_ev, exit_ev, entry_debt, exit_debt, equity_invested):
    """
    Calculate LBO returns (MOIC and approximate IRR).
    
    In an LBO:
    - Entry: Equity Invested = Entry EV - Entry Debt
    - Exit: Equity Value = Exit EV - Exit Debt
    - MOIC = Exit Equity / Entry Equity
    - Approximate IRR = (MOIC)^(1/years) - 1
    
    Parameters:
    -----------
    entry_ev : float
        Entry enterprise value
    exit_ev : float
        Exit enterprise value
    entry_debt : float
        Debt at entry
    exit_debt : float
        Debt at exit (usually lower due to paydown)
    equity_invested : float
        Equity check written at entry
    
    Returns:
    --------
    dict
        Dictionary with 'moic', 'irr_approx', 'entry_equity', 'exit_equity'
    """
    # Calculate equity values
    entry_equity = entry_ev - entry_debt
    exit_equity = exit_ev - exit_debt
    
    # Calculate MOIC
    moic = exit_equity / equity_invested
    
    # Approximate IRR (assuming 5-year hold)
    years = 5
    irr_approx = (moic ** (1 / years)) - 1
    
    return {
        'moic': moic,
        'irr_approx': irr_approx,
        'entry_equity': entry_equity,
        'exit_equity': exit_equity,
        'value_created': exit_equity - equity_invested
    }


# Test Exercise 2
print("=" * 70)
print("EXERCISE 2: LBO Returns Calculator")
print("=" * 70)

entry_enterprise_value = 500
exit_enterprise_value = 750
debt_at_entry = 300
debt_at_exit = 150
equity_check = 200

returns = calculate_lbo_returns(
    entry_enterprise_value,
    exit_enterprise_value,
    debt_at_entry,
    debt_at_exit,
    equity_check
)

print("\nLBO Transaction Summary:")
print(f"Entry EV:              ${entry_enterprise_value}M")
print(f"Entry Debt:            ${debt_at_entry}M")
print(f"Entry Equity Value:    ${returns['entry_equity']}M")
print(f"Equity Invested:       ${equity_check}M")
print()
print(f"Exit EV:               ${exit_enterprise_value}M")
print(f"Exit Debt:             ${debt_at_exit}M")
print(f"Exit Equity Value:     ${returns['exit_equity']}M")
print()
print(f"Value Created:         ${returns['value_created']}M")
print()
print("Returns Analysis:")
print(f"MOIC:                  {returns['moic']:.2f}x")
print(f"IRR (5-year hold):     {returns['irr_approx']:.1%}")

if returns['irr_approx'] >= 0.20:
    print("✅ Meets PE Club's 20% IRR hurdle!")
else:
    print("❌ Below 20% IRR hurdle")

print("\n")


# Exercise 3: Simple DCF Model
# =============================

def simple_dcf(free_cash_flows, wacc, terminal_growth_rate):
    """
    Calculate enterprise value using Discounted Cash Flow.
    
    Steps:
    1. Discount each cash flow to present value
    2. Calculate terminal value = Final FCF × (1 + g) / (WACC - g)
    3. Discount terminal value to present
    4. Sum all present values
    
    Parameters:
    -----------
    free_cash_flows : list
        Projected free cash flows for 5 years
    wacc : float
        Weighted average cost of capital (discount rate)
    terminal_growth_rate : float
        Perpetual growth rate (typically 2-3%)
    
    Returns:
    --------
    dict
        Dictionary with DCF components and enterprise value
    """
    # Step 1: Calculate PV of projected cash flows
    pv_cash_flows_list = []
    for year, fcf in enumerate(free_cash_flows, start=1):
        pv = fcf / (1 + wacc) ** year
        pv_cash_flows_list.append(pv)
    
    total_pv_cash_flows = sum(pv_cash_flows_list)
    
    # Step 2: Calculate terminal value
    final_fcf = free_cash_flows[-1]
    terminal_value = final_fcf * (1 + terminal_growth_rate) / (wacc - terminal_growth_rate)
    
    # Step 3: Discount terminal value to present
    terminal_year = len(free_cash_flows)
    pv_terminal_value = terminal_value / (1 + wacc) ** terminal_year
    
    # Step 4: Calculate enterprise value
    enterprise_value = total_pv_cash_flows + pv_terminal_value
    
    return {
        'pv_cash_flows': total_pv_cash_flows,
        'pv_cash_flows_list': pv_cash_flows_list,
        'terminal_value': terminal_value,
        'pv_terminal_value': pv_terminal_value,
        'enterprise_value': enterprise_value
    }


# Test Exercise 3
print("=" * 70)
print("EXERCISE 3: Simple DCF Model")
print("=" * 70)

fcf_projections = [100, 110, 121, 133, 146]
discount_rate = 0.10
terminal_growth = 0.025

dcf_result = simple_dcf(fcf_projections, discount_rate, terminal_growth)

print("\nDCF Valuation Model:")
print()
print("Cash Flow Projections:")
print(f"{'Year':<6} {'FCF':<12} {'Discount Factor':<18} {'Present Value':<15}")
print("-" * 55)

for year, (fcf, pv) in enumerate(zip(fcf_projections, dcf_result['pv_cash_flows_list']), 1):
    discount_factor = 1 / (1 + discount_rate) ** year
    print(f"{year:<6} ${fcf:<11,.0f} {discount_factor:<18.4f} ${pv:<14,.2f}")

print("-" * 55)
print(f"{'Total':<6} ${sum(fcf_projections):<11,.0f} {'':<18} ${dcf_result['pv_cash_flows']:<14,.2f}")

print()
print("Terminal Value Calculation:")
print(f"Final Year FCF:           ${fcf_projections[-1]:,.0f}M")
print(f"Terminal Growth Rate:     {terminal_growth:.1%}")
print(f"WACC:                     {discount_rate:.1%}")
print(f"Terminal Value:           ${dcf_result['terminal_value']:,.2f}M")
print(f"PV of Terminal Value:     ${dcf_result['pv_terminal_value']:,.2f}M")

print()
print("=" * 55)
print(f"Enterprise Value:         ${dcf_result['enterprise_value']:,.2f}M")
print("=" * 55)

print("\n")


# Exercise 4: Comparable Companies Table
# =======================================

def create_comps_table(companies):
    """
    Create a comparable companies analysis table.
    
    Calculate for each company:
    - EV/EBITDA multiple
    - EV/Revenue multiple
    - EBITDA margin
    
    Parameters:
    -----------
    companies : list of dict
        Each dict has: name, revenue, ebitda, market_cap, net_debt
    
    Returns:
    --------
    None (prints formatted table)
    """
    print("\nComparable Companies Analysis:\n")
    
    # Header
    print(f"{'Company':<15} {'Revenue':<10} {'EBITDA':<10} {'EV':<10} "
          f"{'EV/Rev':<8} {'EV/EBITDA':<10} {'EBITDA Margin':<15}")
    print("-" * 80)
    
    # Store metrics for median calculation
    ev_rev_multiples = []
    ev_ebitda_multiples = []
    ebitda_margins = []
    
    # Print each company
    for company in companies:
        # Calculate metrics
        ev = company['market_cap'] + company['net_debt']
        ev_rev = ev / company['revenue']
        ev_ebitda = ev / company['ebitda']
        ebitda_margin = company['ebitda'] / company['revenue']
        
        # Store for median
        ev_rev_multiples.append(ev_rev)
        ev_ebitda_multiples.append(ev_ebitda)
        ebitda_margins.append(ebitda_margin)
        
        # Print row
        print(f"{company['name']:<15} ${company['revenue']:<9,.0f} "
              f"${company['ebitda']:<9,.0f} ${ev:<9,.0f} "
              f"{ev_rev:<7.1f}x {ev_ebitda:<9.1f}x {ebitda_margin:<14.1%}")
    
    # Calculate medians
    ev_rev_multiples.sort()
    ev_ebitda_multiples.sort()
    ebitda_margins.sort()
    
    n = len(companies)
    median_ev_rev = ev_rev_multiples[n // 2]
    median_ev_ebitda = ev_ebitda_multiples[n // 2]
    median_ebitda_margin = ebitda_margins[n // 2]
    median_revenue = sorted([c['revenue'] for c in companies])[n // 2]
    median_ebitda = sorted([c['ebitda'] for c in companies])[n // 2]
    median_ev = sorted([c['market_cap'] + c['net_debt'] for c in companies])[n // 2]
    
    # Print median row
    print("-" * 80)
    print(f"{'Median':<15} ${median_revenue:<9,.0f} ${median_ebitda:<9,.0f} "
          f"${median_ev:<9,.0f} {median_ev_rev:<7.1f}x {median_ev_ebitda:<9.1f}x "
          f"{median_ebitda_margin:<14.1%}")


# Test Exercise 4
print("=" * 70)
print("EXERCISE 4: Comparable Companies Table")
print("=" * 70)

comps = [
    {"name": "TechCo A", "revenue": 1000, "ebitda": 200, "market_cap": 1500, "net_debt": 100},
    {"name": "TechCo B", "revenue": 1200, "ebitda": 250, "market_cap": 2000, "net_debt": 200},
    {"name": "TechCo C", "revenue": 800, "ebitda": 150, "market_cap": 1200, "net_debt": 50},
]

create_comps_table(comps)

print("\n")
print("=" * 70)
print("All exercises completed! Great work! 🎉")
print("=" * 70)
print()
print("Key Takeaways:")
print("  ✓ You can project financials with custom growth rates")
print("  ✓ You can calculate PE returns (MOIC and IRR)")
print("  ✓ You can build a complete DCF model")
print("  ✓ You can create professional comp tables")
print()
print("You're ready for Module 03: Data Analysis with Pandas!")
print("=" * 70)
