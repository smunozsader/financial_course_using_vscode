"""
Solutions to Module 05 Practice Exercises - LBO Modeling

These solutions show how PE firms analyze leveraged buyout opportunities.
Perfect for use at PE Club or any PE firm!
"""

import pandas as pd
import numpy as np


# =============================================================================
# EXERCISE 1: Quick LBO Returns Check
# =============================================================================

def exercise_1_quick_lbo_check():
    """
    Quick LBO returns calculation - the "back of napkin" math
    PE investors do this in their head during initial screening!
    
    Deal Parameters:
    - Entry: $60M EBITDA @ 7.5x = $450M purchase price
    - Financing: 40% equity ($180M), 60% debt ($270M)
    - Exit: $90M EBITDA @ 9.0x
    - Remaining debt at exit: $120M
    """
    print("\n" + "="*80)
    print("EXERCISE 1: QUICK LBO RETURNS CHECK")
    print("="*80)
    
    # Entry
    entry_ebitda = 60.0
    entry_multiple = 7.5
    purchase_price = entry_ebitda * entry_multiple
    
    # Financing
    equity_percent = 0.40
    debt_percent = 0.60
    equity_invested = purchase_price * equity_percent
    initial_debt = purchase_price * debt_percent
    
    print("\nENTRY:")
    print("-" * 80)
    print(f"Entry EBITDA:        ${entry_ebitda:.0f}M")
    print(f"Entry Multiple:      {entry_multiple:.1f}x")
    print(f"Purchase Price:      ${purchase_price:.0f}M")
    print(f"\nFinancing:")
    print(f"  Equity ({equity_percent*100:.0f}%):     ${equity_invested:.0f}M")
    print(f"  Debt ({debt_percent*100:.0f}%):       ${initial_debt:.0f}M")
    
    # Exit
    exit_ebitda = 90.0
    exit_multiple = 9.0
    exit_enterprise_value = exit_ebitda * exit_multiple
    remaining_debt = 120.0
    exit_equity_value = exit_enterprise_value - remaining_debt
    
    print("\nEXIT (Year 5):")
    print("-" * 80)
    print(f"Exit EBITDA:         ${exit_ebitda:.0f}M")
    print(f"Exit Multiple:       {exit_multiple:.1f}x")
    print(f"Exit Enterprise Value: ${exit_enterprise_value:.0f}M")
    print(f"Less: Remaining Debt:  ${remaining_debt:.0f}M")
    print(f"Exit Equity Value:     ${exit_equity_value:.0f}M")
    
    # Returns
    moic = exit_equity_value / equity_invested
    holding_period = 5
    irr = (moic ** (1/holding_period)) - 1
    
    print("\n" + "="*80)
    print("RETURNS:")
    print("="*80)
    print(f"Equity Invested:     ${equity_invested:.0f}M")
    print(f"Exit Equity Value:   ${exit_equity_value:.0f}M")
    print(f"Profit:              ${exit_equity_value - equity_invested:.0f}M")
    print(f"\nMOIC:                {moic:.2f}x")
    print(f"IRR:                 {irr*100:.1f}%")
    
    # Evaluation
    print("\n" + "-"*80)
    print("DEAL EVALUATION:")
    print("-"*80)
    
    if irr >= 0.25:
        verdict = "🔥 HOME RUN! Do this deal!"
    elif irr >= 0.20:
        verdict = "✅ STRONG DEAL. Meets hurdle rate."
    elif irr >= 0.15:
        verdict = "🟡 ACCEPTABLE. Borderline."
    else:
        verdict = "🔴 BELOW HURDLE. Pass."
    
    print(verdict)
    
    # Value creation breakdown
    print("\n" + "-"*80)
    print("VALUE CREATION SOURCES:")
    print("-"*80)
    
    # EBITDA growth
    ebitda_growth = exit_ebitda - entry_ebitda
    value_from_ebitda = ebitda_growth * entry_multiple
    
    # Multiple expansion
    multiple_expansion = exit_multiple - entry_multiple
    value_from_multiple = exit_ebitda * multiple_expansion
    
    # Debt paydown
    debt_paid_down = initial_debt - remaining_debt
    
    print(f"1. EBITDA Growth: ${entry_ebitda:.0f}M → ${exit_ebitda:.0f}M")
    print(f"   Value created: ${value_from_ebitda:.0f}M @ {entry_multiple:.1f}x")
    print(f"\n2. Multiple Expansion: {entry_multiple:.1f}x → {exit_multiple:.1f}x")
    print(f"   Value created: ${value_from_multiple:.0f}M")
    print(f"\n3. Debt Paydown: ${initial_debt:.0f}M → ${remaining_debt:.0f}M")
    print(f"   Debt paid down: ${debt_paid_down:.0f}M (company paid, not you!)")
    
    total_value_created = exit_enterprise_value - purchase_price
    print(f"\nTotal EV Created: ${total_value_created:.0f}M")
    
    return {
        'moic': moic,
        'irr': irr,
        'exit_equity_value': exit_equity_value,
        'equity_invested': equity_invested
    }


# =============================================================================
# EXERCISE 2: Complete LBO Model
# =============================================================================

def exercise_2_complete_lbo_model():
    """
    Build a complete LBO model with all components:
    - Sources & Uses
    - Operating projections
    - Debt schedule
    - Returns calculation
    
    This is a simplified but realistic model structure.
    """
    print("\n" + "="*80)
    print("EXERCISE 2: COMPLETE LBO MODEL - RetailCo Buyout")
    print("="*80)
    
    company_name = "RetailCo Inc."
    
    # === STEP 1: TRANSACTION STRUCTURE ===
    print("\n" + "-"*80)
    print("STEP 1: TRANSACTION STRUCTURE")
    print("-"*80)
    
    # Entry
    ltm_revenue = 500.0
    ltm_ebitda = 75.0
    ebitda_margin = ltm_ebitda / ltm_revenue
    entry_multiple = 8.0
    purchase_price = ltm_ebitda * entry_multiple
    
    # Fees
    transaction_fees = purchase_price * 0.03  # 3% typical
    financing_fees = purchase_price * 0.02    # 2% typical
    total_uses = purchase_price + transaction_fees + financing_fees
    
    # Financing
    equity_percent = 0.40
    debt_percent = 0.60
    equity_investment = total_uses * equity_percent
    total_debt = total_uses * debt_percent
    
    # Debt split
    senior_debt = ltm_ebitda * 4.0  # 4.0x EBITDA
    sub_debt = total_debt - senior_debt
    
    print(f"Target: {company_name}")
    print(f"LTM EBITDA:          ${ltm_ebitda:.0f}M")
    print(f"Entry Multiple:      {entry_multiple:.1f}x")
    print(f"Purchase Price:      ${purchase_price:.0f}M")
    print(f"Transaction Costs:   ${transaction_fees + financing_fees:.0f}M")
    print(f"Total Uses:          ${total_uses:.0f}M")
    print(f"\nFinancing:")
    print(f"  Equity:            ${equity_investment:.0f}M ({equity_percent*100:.0f}%)")
    print(f"  Senior Debt:       ${senior_debt:.0f}M")
    print(f"  Sub Debt:          ${sub_debt:.0f}M")
    print(f"  Total Debt:        ${total_debt:.0f}M ({debt_percent*100:.0f}%)")
    
    # === STEP 2: OPERATING PROJECTIONS ===
    print("\n" + "-"*80)
    print("STEP 2: 5-YEAR OPERATING PROJECTIONS")
    print("-"*80)
    
    # Growth assumptions
    revenue_growth_rates = [0.08, 0.08, 0.07, 0.06, 0.06]
    years = list(range(2025, 2030))
    
    # Build projections
    revenues = []
    current_revenue = ltm_revenue
    for g in revenue_growth_rates:
        current_revenue *= (1 + g)
        revenues.append(current_revenue)
    
    # Operating assumptions
    ebitda_margin_proj = 0.16  # Margin expansion from 15% to 16%
    tax_rate = 0.25
    capex_pct = 0.04
    nwc_pct = 0.10
    
    # Calculate EBITDA and FCF
    ebitdas = [r * ebitda_margin_proj for r in revenues]
    taxes = [ebitda * tax_rate for ebitda in ebitdas]
    capex = [r * capex_pct for r in revenues]
    
    # NWC changes
    base_nwc = ltm_revenue * nwc_pct
    nwc_changes = []
    prev_nwc = base_nwc
    for r in revenues:
        current_nwc = r * nwc_pct
        nwc_changes.append(current_nwc - prev_nwc)
        prev_nwc = current_nwc
    
    # Free Cash Flow (simplified)
    fcfs = [ebitda - tax - cx - nwc for ebitda, tax, cx, nwc in 
            zip(ebitdas, taxes, capex, nwc_changes)]
    
    projections = pd.DataFrame({
        'Year': years,
        'Revenue': revenues,
        'EBITDA': ebitdas,
        'Taxes': taxes,
        'CapEx': capex,
        'Change_NWC': nwc_changes,
        'FCF': fcfs
    })
    
    print(projections.round(1))
    
    # === STEP 3: DEBT SCHEDULE ===
    print("\n" + "-"*80)
    print("STEP 3: DEBT SCHEDULE")
    print("-"*80)
    
    senior_rate = 0.05
    sub_rate = 0.09
    
    senior_balance = senior_debt
    sub_balance = sub_debt
    
    debt_schedule = []
    
    for i, year in enumerate(years):
        # Interest
        senior_interest = senior_balance * senior_rate
        sub_interest = sub_balance * sub_rate
        total_interest = senior_interest + sub_interest
        
        # Cash available for debt paydown
        cash_available = fcfs[i] - total_interest
        
        # Pay down senior first
        if cash_available > 0:
            senior_paydown = min(cash_available, senior_balance)
            senior_balance -= senior_paydown
            
            remaining_cash = cash_available - senior_paydown
            if remaining_cash > 0:
                sub_paydown = min(remaining_cash, sub_balance)
                sub_balance -= sub_paydown
            else:
                sub_paydown = 0
        else:
            senior_paydown = 0
            sub_paydown = 0
        
        debt_schedule.append({
            'Year': year,
            'Senior_Balance': senior_balance,
            'Sub_Balance': sub_balance,
            'Total_Debt': senior_balance + sub_balance,
            'Total_Interest': total_interest,
            'Debt_Paydown': senior_paydown + sub_paydown
        })
    
    debt_df = pd.DataFrame(debt_schedule)
    print(debt_df[['Year', 'Total_Debt', 'Total_Interest', 'Debt_Paydown']].round(1))
    
    # === STEP 4: EXIT & RETURNS ===
    print("\n" + "-"*80)
    print("STEP 4: EXIT VALUATION & RETURNS")
    print("-"*80)
    
    exit_ebitda = ebitdas[-1]
    exit_multiple = 9.0  # Multiple expansion
    exit_ev = exit_ebitda * exit_multiple
    remaining_debt = debt_df['Total_Debt'].iloc[-1]
    exit_equity_value = exit_ev - remaining_debt
    
    moic = exit_equity_value / equity_investment
    irr = (moic ** 0.2) - 1
    
    print(f"Exit EBITDA:         ${exit_ebitda:.0f}M")
    print(f"Exit Multiple:       {exit_multiple:.1f}x")
    print(f"Exit EV:             ${exit_ev:.0f}M")
    print(f"Remaining Debt:      ${remaining_debt:.0f}M")
    print(f"Exit Equity Value:   ${exit_equity_value:.0f}M")
    print(f"\nMOIC:                {moic:.2f}x")
    print(f"IRR:                 {irr*100:.1f}%")
    
    print("\n" + "="*80)
    print(f"VERDICT: {irr*100:.1f}% IRR - ", end="")
    if irr >= 0.20:
        print("✅ STRONG DEAL!")
    elif irr >= 0.15:
        print("🟡 ACCEPTABLE")
    else:
        print("🔴 BELOW HURDLE")
    print("="*80)
    
    return {
        'projections': projections,
        'debt_schedule': debt_df,
        'moic': moic,
        'irr': irr
    }


# =============================================================================
# EXERCISE 3: Sensitivity Analysis
# =============================================================================

def exercise_3_sensitivity_analysis():
    """
    Comprehensive sensitivity analysis for LBO returns.
    Test how different assumptions affect IRR/MOIC.
    """
    print("\n" + "="*80)
    print("EXERCISE 3: SENSITIVITY ANALYSIS")
    print("="*80)
    
    # Base case assumptions
    equity_invested = 180.0
    entry_ebitda = 75.0
    
    def calculate_irr(exit_ebitda, exit_multiple, remaining_debt):
        """Helper to calculate IRR"""
        exit_ev = exit_ebitda * exit_multiple
        exit_equity = exit_ev - remaining_debt
        moic = exit_equity / equity_invested
        irr = (moic ** 0.2) - 1
        return irr * 100  # Return as percentage
    
    # SENSITIVITY 1: Exit EBITDA vs Exit Multiple
    print("\nSENSITIVITY #1: EXIT EBITDA vs EXIT MULTIPLE")
    print("-" * 80)
    
    exit_ebitda_range = [85, 90, 95, 100, 105]
    exit_multiple_range = [8.0, 8.5, 9.0, 9.5, 10.0]
    remaining_debt = 180.0  # Assumption
    
    sensitivity_data = []
    for ebitda in exit_ebitda_range:
        row = []
        for multiple in exit_multiple_range:
            irr = calculate_irr(ebitda, multiple, remaining_debt)
            row.append(irr)
        sensitivity_data.append(row)
    
    sensitivity_df = pd.DataFrame(
        sensitivity_data,
        index=[f'${e}M' for e in exit_ebitda_range],
        columns=[f'{m:.1f}x' for m in exit_multiple_range]
    )
    sensitivity_df.index.name = 'Exit EBITDA'
    sensitivity_df.columns.name = 'Exit Multiple →'
    
    print("\nIRR Sensitivity (%):")
    print(sensitivity_df.round(1))
    
    # SENSITIVITY 2: Revenue Growth
    print("\n" + "="*80)
    print("SENSITIVITY #2: REVENUE GROWTH SCENARIOS")
    print("="*80)
    
    base_revenue = 500.0
    ebitda_margin = 0.16
    exit_multiple = 9.0
    
    print(f"\n{'Revenue CAGR':<15} {'Exit Revenue':<15} {'Exit EBITDA':<15} {'IRR':<10}")
    print("-" * 55)
    
    for cagr in [0.05, 0.06, 0.07, 0.08, 0.09]:
        exit_revenue = base_revenue * ((1 + cagr) ** 5)
        exit_ebitda = exit_revenue * ebitda_margin
        irr = calculate_irr(exit_ebitda, exit_multiple, remaining_debt)
        print(f"{cagr*100:>5.0f}%          ${exit_revenue:>10.0f}M     ${exit_ebitda:>10.0f}M      {irr:>5.1f}%")
    
    # SENSITIVITY 3: Leverage Levels
    print("\n" + "="*80)
    print("SENSITIVITY #3: LEVERAGE IMPACT")
    print("="*80)
    
    purchase_price = 600.0  # From entry_ebitda * 8.0
    exit_ev = 855.0  # Fixed exit
    
    print(f"\n{'Equity %':<12} {'Equity Inv':<15} {'Initial Debt':<15} {'MOIC':<10} {'IRR':<10}")
    print("-" * 62)
    
    for equity_pct in [0.30, 0.35, 0.40, 0.45, 0.50]:
        equity_inv = purchase_price * equity_pct
        initial_debt = purchase_price * (1 - equity_pct)
        
        # Assume 50% debt paydown
        remaining_debt = initial_debt * 0.50
        exit_equity = exit_ev - remaining_debt
        moic = exit_equity / equity_inv
        irr = (moic ** 0.2) - 1
        
        print(f"{equity_pct*100:>5.0f}%       ${equity_inv:>10.0f}M     ${initial_debt:>10.0f}M      {moic:>5.2f}x    {irr*100:>5.1f}%")
    
    print("\n💡 INSIGHT: More leverage = Higher returns, BUT higher risk!")
    
    # SENSITIVITY 4: What Drives Returns?
    print("\n" + "="*80)
    print("SENSITIVITY #4: RETURN DRIVERS")
    print("="*80)
    
    # Base case
    base_exit_ebitda = 95.0
    base_exit_multiple = 9.0
    base_remaining_debt = 180.0
    base_irr = calculate_irr(base_exit_ebitda, base_exit_multiple, base_remaining_debt)
    
    print(f"\nBase Case IRR: {base_irr:.1f}%")
    print("\nTesting +10% change in each variable:")
    print("-" * 80)
    
    # Test EBITDA +10%
    irr_ebitda = calculate_irr(base_exit_ebitda * 1.1, base_exit_multiple, base_remaining_debt)
    impact_ebitda = irr_ebitda - base_irr
    
    # Test Multiple +10%
    irr_multiple = calculate_irr(base_exit_ebitda, base_exit_multiple * 1.1, base_remaining_debt)
    impact_multiple = irr_multiple - base_irr
    
    # Test Debt -10% (more paydown)
    irr_debt = calculate_irr(base_exit_ebitda, base_exit_multiple, base_remaining_debt * 0.9)
    impact_debt = irr_debt - base_irr
    
    results = [
        ('Exit EBITDA +10%', impact_ebitda),
        ('Exit Multiple +10%', impact_multiple),
        ('Debt Paydown +10%', impact_debt)
    ]
    
    results.sort(key=lambda x: abs(x[1]), reverse=True)
    
    for name, impact in results:
        print(f"{name:<25} {impact:+.1f} percentage points")
    
    print(f"\n🎯 MOST IMPORTANT: {results[0][0]}")
    print("   → This is where you should focus your diligence!")
    
    return sensitivity_df


# =============================================================================
# EXERCISE 4: Deal Comparison
# =============================================================================

def exercise_4_deal_comparison():
    """
    Compare two different LBO opportunities.
    Which is better? Which is riskier?
    """
    print("\n" + "="*80)
    print("EXERCISE 4: DEAL COMPARISON")
    print("="*80)
    print("\nYou have $180M to invest. Which deal is better?\n")
    
    equity_invested = 180.0
    holding_period = 5
    
    # Deal A: Mature Company
    print("="*80)
    print("DEAL A: MATURE COMPANY (Stable Cash Flow)")
    print("="*80)
    
    a_entry_ebitda = 50.0
    a_entry_multiple = 7.0
    a_purchase_price = a_entry_ebitda * a_entry_multiple
    a_revenue_cagr = 0.06
    
    # Exit
    a_exit_ebitda = a_entry_ebitda * ((1 + a_revenue_cagr) ** holding_period)
    a_exit_multiple = 7.5  # Limited expansion
    a_exit_ev = a_exit_ebitda * a_exit_multiple
    
    # Assume good debt paydown due to stable cash flow
    a_initial_debt = a_purchase_price * 0.60
    a_remaining_debt = a_initial_debt * 0.35  # 65% paydown
    
    a_exit_equity = a_exit_ev - a_remaining_debt
    a_moic = a_exit_equity / equity_invested
    a_irr = (a_moic ** (1/holding_period)) - 1
    
    print(f"\nEntry: ${a_entry_ebitda:.0f}M EBITDA @ {a_entry_multiple:.1f}x = ${a_purchase_price:.0f}M")
    print(f"Revenue Growth: {a_revenue_cagr*100:.0f}% CAGR (mature, stable)")
    print(f"Exit: ${a_exit_ebitda:.0f}M EBITDA @ {a_exit_multiple:.1f}x = ${a_exit_ev:.0f}M")
    print(f"Debt Paydown: ${a_initial_debt:.0f}M → ${a_remaining_debt:.0f}M (strong FCF)")
    print(f"\nMOIC: {a_moic:.2f}x")
    print(f"IRR: {a_irr*100:.1f}%")
    
    # Deal B: Growth Company
    print("\n" + "="*80)
    print("DEAL B: GROWTH COMPANY (Higher Risk, Higher Reward)")
    print("="*80)
    
    b_entry_ebitda = 35.0
    b_entry_multiple = 9.0
    b_purchase_price = b_entry_ebitda * b_entry_multiple
    b_revenue_cagr = 0.15
    
    # Exit
    b_exit_ebitda = b_entry_ebitda * ((1 + b_revenue_cagr) ** holding_period)
    b_exit_multiple = 11.0  # Strong expansion
    b_exit_ev = b_exit_ebitda * b_exit_multiple
    
    # Less debt paydown (more reinvestment)
    b_initial_debt = b_purchase_price * 0.60
    b_remaining_debt = b_initial_debt * 0.50  # Only 50% paydown
    
    b_exit_equity = b_exit_ev - b_remaining_debt
    b_moic = b_exit_equity / equity_invested
    b_irr = (b_moic ** (1/holding_period)) - 1
    
    print(f"\nEntry: ${b_entry_ebitda:.0f}M EBITDA @ {b_entry_multiple:.1f}x = ${b_purchase_price:.0f}M")
    print(f"Revenue Growth: {b_revenue_cagr*100:.0f}% CAGR (high growth!)")
    print(f"Exit: ${b_exit_ebitda:.0f}M EBITDA @ {b_exit_multiple:.1f}x = ${b_exit_ev:.0f}M")
    print(f"Debt Paydown: ${b_initial_debt:.0f}M → ${b_remaining_debt:.0f}M (growth capex)")
    print(f"\nMOIC: {b_moic:.2f}x")
    print(f"IRR: {b_irr*100:.1f}%")
    
    # Comparison
    print("\n" + "="*80)
    print("COMPARISON:")
    print("="*80)
    
    comparison = pd.DataFrame({
        'Metric': ['Entry EBITDA', 'Entry Multiple', 'Revenue CAGR', 'Exit Multiple', 
                   'MOIC', 'IRR', 'Risk Level'],
        'Deal A (Mature)': [f'${a_entry_ebitda:.0f}M', f'{a_entry_multiple:.1f}x', 
                           f'{a_revenue_cagr*100:.0f}%', f'{a_exit_multiple:.1f}x',
                           f'{a_moic:.2f}x', f'{a_irr*100:.1f}%', 'Lower'],
        'Deal B (Growth)': [f'${b_entry_ebitda:.0f}M', f'{b_entry_multiple:.1f}x',
                           f'{b_revenue_cagr*100:.0f}%', f'{b_exit_multiple:.1f}x',
                           f'{b_moic:.2f}x', f'{b_irr*100:.1f}%', 'Higher']
    })
    
    print(comparison.to_string(index=False))
    
    # Recommendation
    print("\n" + "="*80)
    print("RECOMMENDATION:")
    print("="*80)
    
    if b_irr > a_irr:
        irr_diff = b_irr - a_irr
        print(f"\n🎯 Deal B has {irr_diff*100:.1f}% higher IRR")
        print(f"   BUT it's riskier - high growth may not materialize")
        print(f"\n💡 DECISION:")
        print(f"   - If confident in growth thesis: Choose Deal B")
        print(f"   - If want lower risk: Choose Deal A")
        print(f"   - Portfolio approach: Do BOTH (if you have capital)")
    else:
        print(f"\n✅ Deal A provides better risk-adjusted returns")
    
    return {
        'deal_a': {'moic': a_moic, 'irr': a_irr},
        'deal_b': {'moic': b_moic, 'irr': b_irr}
    }


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "█"*80)
    print("MODULE 05 - LBO MODELING: SOLUTIONS TO PRACTICE EXERCISES")
    print("█"*80)
    print("\nPE-quality LBO analysis - ready for PE Club!")
    print("Study these models to master leveraged buyouts!\n")
    
    # Exercise 1: Quick check
    ex1_results = exercise_1_quick_lbo_check()
    
    # Exercise 2: Complete model
    ex2_results = exercise_2_complete_lbo_model()
    
    # Exercise 3: Sensitivity
    ex3_results = exercise_3_sensitivity_analysis()
    
    # Exercise 4: Deal comparison
    ex4_results = exercise_4_deal_comparison()
    
    print("\n" + "█"*80)
    print("ALL EXERCISES COMPLETED!")
    print("█"*80)
    print("\n✅ Exercise 1: Quick LBO Check - DONE")
    print("✅ Exercise 2: Complete LBO Model - DONE")
    print("✅ Exercise 3: Sensitivity Analysis - DONE")
    print("✅ Exercise 4: Deal Comparison - DONE")
    print("\n🎉 Congratulations! You now think like a PE investor!")
    print("\n💼 Ready for PE Club deal analysis!")
    print("\n📚 Next up: Module 06 - M&A Analysis")
    print("█"*80 + "\n")
