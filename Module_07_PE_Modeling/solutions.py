"""
Solutions to Module 07 Practice Exercises - Private Equity Fund Modeling

Master PE fund modeling like a GP at Blackstone or KKR!
These solutions show complete fund-level analysis.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple


# =============================================================================
# EXERCISE 1: Single Fund Quick Analysis
# =============================================================================

def exercise_1_fund_quick_analysis():
    """
    Quick fund-level analysis from portfolio company results.
    
    This is how GPs track fund performance in real-time!
    
    Fund: $500M total
    - Deal 1: $100M invested, 3.0x MOIC, Year 5 exit
    - Deal 2: $150M invested, 2.5x MOIC, Year 6 exit
    - Deal 3: $100M invested, 2.0x MOIC, Year 7 exit
    - Deal 4: $150M invested, still holding (NAV = $300M)
    """
    print("\n" + "="*80)
    print("EXERCISE 1: FUND QUICK ANALYSIS")
    print("="*80)
    
    # Fund information
    fund_size = 500.0  # $M
    
    print(f"\nFUND: PE Growth Fund I")
    print(f"Fund Size: ${fund_size:.0f}M")
    print("-" * 80)
    
    # Portfolio companies
    deals = [
        {'name': 'Deal 1', 'invested': 100.0, 'moic': 3.0, 'exit_year': 5, 'status': 'Exited'},
        {'name': 'Deal 2', 'invested': 150.0, 'moic': 2.5, 'exit_year': 6, 'status': 'Exited'},
        {'name': 'Deal 3', 'invested': 100.0, 'moic': 2.0, 'exit_year': 7, 'status': 'Exited'},
        {'name': 'Deal 4', 'invested': 150.0, 'nav': 300.0, 'exit_year': None, 'status': 'Holding'}
    ]
    
    print("\nPORTFOLIO COMPANIES:")
    print("-" * 80)
    
    total_invested = 0
    total_realized = 0
    total_unrealized = 0
    
    for deal in deals:
        invested = deal['invested']
        total_invested += invested
        
        if deal['status'] == 'Exited':
            realized_value = invested * deal['moic']
            total_realized += realized_value
            profit = realized_value - invested
            
            print(f"\n{deal['name']} - {deal['status']} (Year {deal['exit_year']})")
            print(f"  Invested:        ${invested:.0f}M")
            print(f"  Exit Value:      ${realized_value:.0f}M")
            print(f"  MOIC:            {deal['moic']:.1f}x")
            print(f"  Profit:          ${profit:.0f}M")
        else:
            nav = deal['nav']
            total_unrealized += nav
            implied_moic = nav / invested
            
            print(f"\n{deal['name']} - {deal['status']}")
            print(f"  Invested:        ${invested:.0f}M")
            print(f"  Current NAV:     ${nav:.0f}M")
            print(f"  Implied MOIC:    {implied_moic:.1f}x")
    
    # Fund-level calculations
    print("\n" + "="*80)
    print("FUND-LEVEL METRICS:")
    print("="*80)
    
    # 1. Gross MOIC
    total_value = total_realized + total_unrealized
    gross_moic = total_value / total_invested
    
    print(f"\n1. GROSS MOIC (Multiple on Invested Capital)")
    print(f"   Total Invested:   ${total_invested:.0f}M")
    print(f"   Realized Value:   ${total_realized:.0f}M")
    print(f"   Unrealized (NAV): ${total_unrealized:.0f}M")
    print(f"   Total Value:      ${total_value:.0f}M")
    print(f"   ")
    print(f"   GROSS MOIC:       {gross_moic:.2f}x")
    
    # 2. DPI (Distributions to Paid-In)
    dpi = total_realized / total_invested
    
    print(f"\n2. DPI (Distributions / Paid-In Capital)")
    print(f"   Distributions:    ${total_realized:.0f}M")
    print(f"   Paid-In Capital:  ${total_invested:.0f}M")
    print(f"   ")
    print(f"   DPI:              {dpi:.2f}x")
    print(f"   💡 This is REALIZED returns (actual cash back)")
    
    # 3. RVPI (Residual Value to Paid-In)
    rvpi = total_unrealized / total_invested
    
    print(f"\n3. RVPI (Residual Value / Paid-In Capital)")
    print(f"   NAV Remaining:    ${total_unrealized:.0f}M")
    print(f"   Paid-In Capital:  ${total_invested:.0f}M")
    print(f"   ")
    print(f"   RVPI:             {rvpi:.2f}x")
    print(f"   💡 This is UNREALIZED value (still in fund)")
    
    # 4. TVPI (Total Value to Paid-In)
    tvpi = total_value / total_invested
    
    print(f"\n4. TVPI (Total Value / Paid-In Capital)")
    print(f"   Total Value:      ${total_value:.0f}M")
    print(f"   Paid-In Capital:  ${total_invested:.0f}M")
    print(f"   ")
    print(f"   TVPI:             {tvpi:.2f}x")
    print(f"   Check: DPI + RVPI = {dpi:.2f} + {rvpi:.2f} = {dpi+rvpi:.2f}x ✓")
    
    # 5. Estimated IRR (simplified)
    print(f"\n5. ESTIMATED GROSS IRR")
    
    # Build cash flow array
    cash_flows = [0] * 10
    
    # Investments (years 1-2)
    cash_flows[0] = -100  # Deal 1 (Year 1)
    cash_flows[1] = -250  # Deals 2, 3, 4 (Year 2)
    
    # Exits
    cash_flows[5-1] = 300   # Deal 1: $100M * 3.0x
    cash_flows[6-1] = 375   # Deal 2: $150M * 2.5x
    cash_flows[7-1] = 200   # Deal 3: $100M * 2.0x
    cash_flows[9] = 300     # Deal 4: Assumed exit Year 10
    
    # Calculate IRR
    try:
        irr = np.irr(cash_flows)
        print(f"   Cash Flows: {[int(cf) for cf in cash_flows]}")
        print(f"   ")
        print(f"   GROSS IRR:        {irr*100:.1f}%")
    except:
        print(f"   (Using MOIC approximation)")
        holding_period = 6  # Average
        irr = (gross_moic ** (1/holding_period)) - 1
        print(f"   GROSS IRR:        ~{irr*100:.1f}% (estimated)")
    
    # Performance evaluation
    print("\n" + "="*80)
    print("FUND PERFORMANCE EVALUATION:")
    print("="*80)
    
    print(f"\n📊 Key Metrics Summary:")
    print(f"   Gross MOIC:       {gross_moic:.2f}x")
    print(f"   DPI:              {dpi:.2f}x (realized)")
    print(f"   TVPI:             {tvpi:.2f}x (total)")
    print(f"   Gross IRR:        ~{irr*100:.1f}%")
    
    print(f"\n🎯 Benchmark Comparison:")
    if gross_moic >= 2.5 and irr >= 0.20:
        print(f"   ✅ TOP QUARTILE performance!")
        print(f"   → {gross_moic:.2f}x MOIC and {irr*100:.1f}% IRR")
        print(f"   → This fund is a HOME RUN!")
    elif gross_moic >= 2.0 and irr >= 0.15:
        print(f"   ✅ UPPER MID QUARTILE performance")
        print(f"   → Solid returns, LPs will be happy")
    elif gross_moic >= 1.5:
        print(f"   🟡 LOWER MID QUARTILE performance")
        print(f"   → Acceptable but not great")
    else:
        print(f"   ❌ BOTTOM QUARTILE performance")
        print(f"   → Need to improve deal selection")
    
    return {
        'gross_moic': gross_moic,
        'dpi': dpi,
        'rvpi': rvpi,
        'tvpi': tvpi,
        'gross_irr': irr
    }


# =============================================================================
# EXERCISE 2: GP vs LP Economics
# =============================================================================

def exercise_2_gp_vs_lp_economics():
    """
    Calculate GP and LP economics separately.
    
    THIS shows why people want to be GPs (not LPs)!
    
    Fund: $1B, 2.5x MOIC over 6 years
    - Management fees: 2% for 10 years
    - Carry: 20% above 8% hurdle
    - GP commitment: 2% of fund
    """
    print("\n" + "="*80)
    print("EXERCISE 2: GP vs LP ECONOMICS")
    print("="*80)
    
    # Fund parameters
    fund_size = 1_000.0  # $M
    fund_moic = 2.5
    fund_life = 10  # years
    avg_holding_period = 6  # years
    
    management_fee_rate = 0.02
    carry_rate = 0.20
    hurdle_rate = 0.08
    gp_commitment_pct = 0.02
    
    print(f"\nFUND PARAMETERS:")
    print(f"Fund Size:           ${fund_size:.0f}M")
    print(f"Fund MOIC:           {fund_moic:.1f}x")
    print(f"Holding Period:      {avg_holding_period} years")
    print(f"Management Fee:      {management_fee_rate*100:.1f}%")
    print(f"Carry:               {carry_rate*100:.0f}%")
    print(f"Hurdle Rate:         {hurdle_rate*100:.0f}%")
    
    # LP and GP commitments
    lp_commitment = fund_size * (1 - gp_commitment_pct)
    gp_commitment = fund_size * gp_commitment_pct
    
    print(f"\nCOMMITMENTS:")
    print("-" * 80)
    print(f"LP Commitment:       ${lp_commitment:.0f}M ({(1-gp_commitment_pct)*100:.0f}%)")
    print(f"GP Commitment:       ${gp_commitment:.0f}M ({gp_commitment_pct*100:.0f}%)")
    
    # Total proceeds from fund
    total_proceeds = fund_size * fund_moic
    total_profit = total_proceeds - fund_size
    
    print(f"\nFUND RESULTS:")
    print("-" * 80)
    print(f"Total Proceeds:      ${total_proceeds:.0f}M")
    print(f"Less: Invested:      ${fund_size:.0f}M")
    print(f"Total Profit:        ${total_profit:.0f}M")
    
    # === LP ECONOMICS ===
    print("\n" + "="*80)
    print("LP ECONOMICS:")
    print("="*80)
    
    # LP gets their capital back first
    lp_capital_returned = lp_commitment
    
    # LP preferred return (8% hurdle)
    lp_preferred_return = lp_commitment * ((1 + hurdle_rate) ** avg_holding_period - 1)
    
    # Remaining profit after preferred return
    remaining_after_hurdle = total_profit - lp_preferred_return
    
    # LP gets 80% of remaining profit (GP gets 20% carry)
    lp_share_of_remaining = remaining_after_hurdle * (1 - carry_rate)
    
    # Total LP proceeds
    lp_total_proceeds = lp_capital_returned + lp_preferred_return + lp_share_of_remaining
    lp_profit = lp_total_proceeds - lp_commitment
    lp_moic = lp_total_proceeds / lp_commitment
    lp_irr = (lp_moic ** (1/avg_holding_period)) - 1
    
    print(f"\nLP Proceeds Breakdown:")
    print(f"  1. Return of Capital:     ${lp_capital_returned:.0f}M")
    print(f"  2. Preferred Return:      ${lp_preferred_return:.0f}M ({hurdle_rate*100:.0f}% hurdle)")
    print(f"  3. Share of Profit:       ${lp_share_of_remaining:.0f}M ({(1-carry_rate)*100:.0f}%)")
    print(f"  ")
    print(f"  Total LP Proceeds:        ${lp_total_proceeds:.0f}M")
    print(f"  LP Profit:                ${lp_profit:.0f}M")
    print(f"  ")
    print(f"  LP MOIC:                  {lp_moic:.2f}x")
    print(f"  LP NET IRR:               {lp_irr*100:.1f}%")
    
    # === GP ECONOMICS ===
    print("\n" + "="*80)
    print("GP ECONOMICS:")
    print("="*80)
    
    # 1. Management fees
    annual_mgmt_fee = fund_size * management_fee_rate
    total_mgmt_fees = annual_mgmt_fee * fund_life
    
    print(f"\n1. MANAGEMENT FEES:")
    print(f"   Annual Fee:               ${annual_mgmt_fee:.0f}M/year")
    print(f"   × {fund_life} years")
    print(f"   Total Mgmt Fees:          ${total_mgmt_fees:.0f}M")
    print(f"   💡 This covers salaries, rent, deal costs")
    
    # 2. Carried interest
    gp_carried_interest = remaining_after_hurdle * carry_rate
    
    print(f"\n2. CARRIED INTEREST (Performance Fee):")
    print(f"   Profit after hurdle:      ${remaining_after_hurdle:.0f}M")
    print(f"   × {carry_rate*100:.0f}% carry")
    print(f"   Carried Interest:         ${gp_carried_interest:.0f}M")
    print(f"   💰 THIS IS WHERE GPs GET RICH!")
    
    # 3. GP commitment return
    gp_commitment_return = gp_commitment * (fund_moic - 1)
    
    print(f"\n3. GP COMMITMENT RETURN:")
    print(f"   GP Invested:              ${gp_commitment:.0f}M")
    print(f"   × {fund_moic:.1f}x MOIC")
    print(f"   GP Proceeds:              ${gp_commitment * fund_moic:.0f}M")
    print(f"   GP Profit:                ${gp_commitment_return:.0f}M")
    
    # Total GP economics
    gp_total_value = total_mgmt_fees + gp_carried_interest + gp_commitment_return
    
    print(f"\n{'='*80}")
    print(f"TOTAL GP VALUE:")
    print(f"{'='*80}")
    print(f"  Management Fees:          ${total_mgmt_fees:.0f}M")
    print(f"  Carried Interest:         ${gp_carried_interest:.0f}M")
    print(f"  GP Commitment Return:     ${gp_commitment_return:.0f}M")
    print(f"  ")
    print(f"  TOTAL GP VALUE:           ${gp_total_value:.0f}M")
    
    # GP as % of profits
    gp_pct_of_profits = (gp_total_value / total_profit) * 100
    
    print(f"\n💡 GP captures {gp_pct_of_profits:.1f}% of total profits!")
    
    # === COMPARISON ===
    print("\n" + "="*80)
    print("GP vs LP COMPARISON:")
    print("="*80)
    
    comparison_df = pd.DataFrame({
        'Metric': ['Capital Invested', 'Total Proceeds', 'Profit', 'MOIC', 'IRR'],
        'LP': [
            f'${lp_commitment:.0f}M',
            f'${lp_total_proceeds:.0f}M',
            f'${lp_profit:.0f}M',
            f'{lp_moic:.2f}x',
            f'{lp_irr*100:.1f}%'
        ],
        'GP': [
            f'${gp_commitment:.0f}M',
            f'${gp_total_value:.0f}M',
            f'${gp_total_value - gp_commitment:.0f}M',
            f'{gp_total_value/gp_commitment:.2f}x',
            'N/A (fees paid over time)'
        ]
    })
    
    print(comparison_df.to_string(index=False))
    
    print(f"\n🎯 KEY INSIGHTS:")
    print(f"   • LPs: Invested ${lp_commitment:.0f}M, Net IRR = {lp_irr*100:.1f}%")
    print(f"   • GPs: Invested ${gp_commitment:.0f}M, Total Value = ${gp_total_value:.0f}M")
    print(f"   • GP earns ${gp_total_value/gp_commitment:.1f}x their investment!")
    print(f"   • Carry alone = ${gp_carried_interest:.0f}M (vs ${gp_commitment:.0f}M invested)")
    print(f"\n   💰 This is why people want to work in PE!")
    
    return {
        'lp_proceeds': lp_total_proceeds,
        'lp_moic': lp_moic,
        'lp_irr': lp_irr,
        'gp_total_value': gp_total_value,
        'gp_carry': gp_carried_interest,
        'gp_pct_of_profits': gp_pct_of_profits
    }


# =============================================================================
# EXERCISE 3: Waterfall Distribution
# =============================================================================

def exercise_3_waterfall_distribution():
    """
    Detailed waterfall distribution calculation.
    
    THIS is how proceeds are split between LP and GP!
    Critical for understanding PE fund economics.
    
    Fund: $500M raised, $1.2B proceeds
    - Hurdle: 8% IRR
    - Carry: 20%
    - Average hold: 5 years
    """
    print("\n" + "="*80)
    print("EXERCISE 3: WATERFALL DISTRIBUTION")
    print("="*80)
    
    # Fund parameters
    fund_raised = 500.0  # $M
    total_proceeds = 1_200.0  # $M
    hurdle_rate = 0.08
    carry_rate = 0.20
    avg_holding_period = 5
    gp_commitment_pct = 0.02
    
    lp_capital = fund_raised * (1 - gp_commitment_pct)
    gp_capital = fund_raised * gp_commitment_pct
    
    print(f"\nFUND PARAMETERS:")
    print(f"Total Raised:        ${fund_raised:.0f}M")
    print(f"  LP Capital:        ${lp_capital:.0f}M ({(1-gp_commitment_pct)*100:.0f}%)")
    print(f"  GP Capital:        ${gp_capital:.0f}M ({gp_commitment_pct*100:.0f}%)")
    print(f"Total Proceeds:      ${total_proceeds:.0f}M")
    print(f"Hurdle Rate:         {hurdle_rate*100:.0f}%")
    print(f"Carry Rate:          {carry_rate*100:.0f}%")
    print(f"Holding Period:      {avg_holding_period} years")
    
    # Track distributions
    lp_distributions = []
    gp_distributions = []
    remaining_proceeds = total_proceeds
    
    print("\n" + "="*80)
    print("WATERFALL TIERS:")
    print("="*80)
    
    # TIER 1: Return of Capital
    print("\n" + "-"*80)
    print("TIER 1: RETURN OF CAPITAL")
    print("-"*80)
    
    lp_capital_returned = min(remaining_proceeds, lp_capital)
    lp_distributions.append(('Return of Capital', lp_capital_returned))
    remaining_proceeds -= lp_capital_returned
    
    gp_capital_returned = min(remaining_proceeds, gp_capital)
    gp_distributions.append(('Return of Capital', gp_capital_returned))
    remaining_proceeds -= gp_capital_returned
    
    print(f"To LP:               ${lp_capital_returned:.1f}M (return their ${lp_capital:.0f}M)")
    print(f"To GP:               ${gp_capital_returned:.1f}M (return their ${gp_capital:.0f}M)")
    print(f"Remaining:           ${remaining_proceeds:.1f}M")
    
    # TIER 2: Preferred Return to LPs (8% hurdle)
    print("\n" + "-"*80)
    print("TIER 2: PREFERRED RETURN TO LPs (8% Hurdle)")
    print("-"*80)
    
    # Calculate 8% compounded over holding period
    preferred_return = lp_capital * ((1 + hurdle_rate) ** avg_holding_period - 1)
    preferred_paid = min(remaining_proceeds, preferred_return)
    lp_distributions.append(('Preferred Return', preferred_paid))
    remaining_proceeds -= preferred_paid
    
    print(f"Preferred Return:    ${lp_capital:.0f}M × (1.08^{avg_holding_period} - 1)")
    print(f"                     = ${preferred_return:.1f}M")
    print(f"To LP:               ${preferred_paid:.1f}M")
    print(f"Remaining:           ${remaining_proceeds:.1f}M")
    
    # TIER 3: GP Catch-Up
    print("\n" + "-"*80)
    print("TIER 3: GP CATCH-UP (to reach 20% of total profits)")
    print("-"*80)
    
    # Total profit = Total proceeds - capital
    total_profit = total_proceeds - fund_raised
    
    # GP should get 20% of total profit
    gp_target_carry = total_profit * carry_rate
    
    # GP already has return of capital
    gp_already_received = gp_capital_returned
    
    # GP needs catch-up to reach target
    gp_catchup_needed = gp_target_carry - (gp_already_received - gp_capital)
    gp_catchup_paid = min(remaining_proceeds, gp_catchup_needed)
    gp_distributions.append(('Catch-Up', gp_catchup_paid))
    remaining_proceeds -= gp_catchup_paid
    
    print(f"Total Profit:        ${total_profit:.1f}M")
    print(f"GP Target (20%):     ${gp_target_carry:.1f}M")
    print(f"GP Already Has:      ${gp_already_received - gp_capital:.1f}M (excl. capital)")
    print(f"GP Catch-Up Needed:  ${gp_catchup_needed:.1f}M")
    print(f"To GP:               ${gp_catchup_paid:.1f}M")
    print(f"Remaining:           ${remaining_proceeds:.1f}M")
    
    # TIER 4: Remaining Split 80/20
    print("\n" + "-"*80)
    print("TIER 4: REMAINING SPLIT 80% LP / 20% GP")
    print("-"*80)
    
    lp_final_split = remaining_proceeds * 0.80
    gp_final_split = remaining_proceeds * 0.20
    
    lp_distributions.append(('80% of Remaining', lp_final_split))
    gp_distributions.append(('20% of Remaining', gp_final_split))
    
    print(f"Remaining:           ${remaining_proceeds:.1f}M")
    print(f"To LP (80%):         ${lp_final_split:.1f}M")
    print(f"To GP (20%):         ${gp_final_split:.1f}M")
    
    # SUMMARY
    print("\n" + "="*80)
    print("DISTRIBUTION SUMMARY:")
    print("="*80)
    
    print("\nLP DISTRIBUTIONS:")
    print("-" * 80)
    lp_total = 0
    for desc, amount in lp_distributions:
        print(f"  {desc:<30} ${amount:>10.1f}M")
        lp_total += amount
    print(f"  {'-'*44}")
    print(f"  {'TOTAL LP':<30} ${lp_total:>10.1f}M")
    
    print("\nGP DISTRIBUTIONS:")
    print("-" * 80)
    gp_total = 0
    for desc, amount in gp_distributions:
        print(f"  {desc:<30} ${amount:>10.1f}M")
        gp_total += amount
    print(f"  {'-'*44}")
    print(f"  {'TOTAL GP':<30} ${gp_total:>10.1f}M")
    
    # Verification
    print("\n" + "-"*80)
    print("VERIFICATION:")
    print("-"*80)
    print(f"LP Total:            ${lp_total:.1f}M")
    print(f"GP Total:            ${gp_total:.1f}M")
    print(f"Sum:                 ${lp_total + gp_total:.1f}M")
    print(f"Total Proceeds:      ${total_proceeds:.1f}M")
    print(f"Match:               {'✓' if abs((lp_total + gp_total) - total_proceeds) < 0.1 else '✗'}")
    
    # Economics
    print("\n" + "-"*80)
    print("ECONOMIC ANALYSIS:")
    print("-"*80)
    
    lp_profit = lp_total - lp_capital
    gp_profit = gp_total - gp_capital
    
    lp_moic = lp_total / lp_capital
    gp_moic = gp_total / gp_capital
    
    lp_irr = (lp_moic ** (1/avg_holding_period)) - 1
    
    print(f"\nLP Economics:")
    print(f"  Invested:          ${lp_capital:.0f}M")
    print(f"  Received:          ${lp_total:.1f}M")
    print(f"  Profit:            ${lp_profit:.1f}M")
    print(f"  MOIC:              {lp_moic:.2f}x")
    print(f"  IRR:               {lp_irr*100:.1f}%")
    
    print(f"\nGP Economics:")
    print(f"  Invested:          ${gp_capital:.0f}M")
    print(f"  Received:          ${gp_total:.1f}M")
    print(f"  Profit:            ${gp_profit:.1f}M")
    print(f"  MOIC:              {gp_moic:.2f}x")
    
    gp_pct_of_profit = (gp_profit / total_profit) * 100
    print(f"\n💡 GP captures {gp_pct_of_profit:.1f}% of total profit!")
    
    return {
        'lp_total': lp_total,
        'gp_total': gp_total,
        'lp_moic': lp_moic,
        'lp_irr': lp_irr,
        'gp_moic': gp_moic
    }


# =============================================================================
# EXERCISE 4: Complete Fund Model
# =============================================================================

def exercise_4_complete_fund_model():
    """
    Build a complete PE fund model from scratch.
    
    THIS IS THE REAL DEAL - Complete fund modeling!
    
    Fund: $750M
    - Investment period: Years 1-4
    - Exit period: Years 4-8
    - 10 portfolio companies
    - Mix of winners and losers
    """
    print("\n" + "="*80)
    print("EXERCISE 4: COMPLETE FUND MODEL - European Growth Fund II")
    print("="*80)
    
    # Fund parameters
    fund_name = "European Growth Fund II"
    fund_size = 750.0  # $M
    vintage_year = 2020
    mgmt_fee_rate = 0.02
    carry_rate = 0.20
    hurdle_rate = 0.08
    
    print(f"\nFUND: {fund_name}")
    print(f"Vintage:             {vintage_year}")
    print(f"Fund Size:           €{fund_size:.0f}M")
    print(f"Strategy:            European Mid-Market Buyouts")
    print(f"Management Fee:      {mgmt_fee_rate*100:.1f}%")
    print(f"Carry:               {carry_rate*100:.0f}%")
    print(f"Hurdle:              {hurdle_rate*100:.0f}%")
    
    # Portfolio companies
    print("\n" + "="*80)
    print("PORTFOLIO COMPANIES:")
    print("="*80)
    
    portfolio = [
        # Name, Entry Year, Invested, Entry Multiple, Exit Year, Exit Multiple, Status
        ('TechCo', 2021, 100, 8.0, 2026, 12.0, 'Win'),
        ('RetailCo', 2021, 80, 7.5, 2025, 6.0, 'Loser'),
        ('HealthCo', 2022, 90, 8.5, 2027, 11.0, 'Win'),
        ('IndustrialCo', 2022, 70, 7.0, 2026, 9.0, 'Good'),
        ('ConsumerCo', 2022, 85, 8.0, 2028, 10.5, 'Good'),
        ('SoftwareCo', 2023, 95, 9.0, 2028, 15.0, 'Home Run'),
        ('ManufacturingCo', 2023, 75, 7.5, 2027, 8.5, 'Okay'),
        ('ServicesCo', 2023, 65, 7.0, 2025, 5.0, 'Loser'),
        ('MediaCo', 2024, 55, 8.0, 2029, 11.0, 'Win'),
        ('LogisticsCo', 2024, 60, 7.5, 2028, 9.5, 'Good')
    ]
    
    print(f"\n{'Company':<20} {'Entry Yr':<10} {'Invested':<12} {'Entry Mult':<12} {'Exit Yr':<10} {'Exit Mult':<12} {'Category':<10}")
    print("-" * 96)
    
    for company in portfolio:
        name, entry_yr, invested, entry_mult, exit_yr, exit_mult, category = company
        print(f"{name:<20} {entry_yr:<10} €{invested:<10.0f}M {entry_mult:<12.1f}x {exit_yr:<10} {exit_mult:<12.1f}x {category:<10}")
    
    # Calculate deal-by-deal returns
    print("\n" + "="*80)
    print("DEAL-BY-DEAL RETURNS:")
    print("="*80)
    
    total_invested = 0
    total_proceeds = 0
    deal_results = []
    
    print(f"\n{'Company':<20} {'Invested':<12} {'Exit Value':<12} {'MOIC':<8} {'Hold':<8} {'IRR':<10}")
    print("-" * 80)
    
    for company in portfolio:
        name, entry_yr, invested, entry_mult, exit_yr, exit_mult, category = company
        
        # Entry
        entry_ebitda = invested / entry_mult * (1/0.40)  # Assume 40% equity
        purchase_price = entry_ebitda * entry_mult
        
        # Exit (assume EBITDA growth)
        holding_period = exit_yr - entry_yr
        ebitda_growth = 0.08 if category in ['Win', 'Home Run'] else 0.05
        exit_ebitda = entry_ebitda * ((1 + ebitda_growth) ** holding_period)
        exit_ev = exit_ebitda * exit_mult
        
        # Debt paydown (assume 50% paydown)
        initial_debt = purchase_price * 0.60
        remaining_debt = initial_debt * 0.50
        
        exit_value = exit_ev - remaining_debt
        
        moic = exit_value / invested
        irr = (moic ** (1/holding_period)) - 1 if holding_period > 0 else 0
        
        total_invested += invested
        total_proceeds += exit_value
        
        deal_results.append({
            'name': name,
            'invested': invested,
            'exit_value': exit_value,
            'moic': moic,
            'irr': irr,
            'category': category
        })
        
        print(f"{name:<20} €{invested:<10.0f}M €{exit_value:<10.0f}M {moic:<7.2f}x {holding_period:<7}y {irr*100:<9.1f}%")
    
    print("-" * 80)
    print(f"{'TOTALS':<20} €{total_invested:<10.0f}M €{total_proceeds:<10.0f}M")
    
    # Fund-level metrics
    print("\n" + "="*80)
    print("FUND-LEVEL METRICS:")
    print("="*80)
    
    gross_moic = total_proceeds / total_invested
    
    # Build cash flow array
    cash_flows = [0] * 12  # 12 years
    
    for company in portfolio:
        name, entry_yr, invested, entry_mult, exit_yr, exit_mult, category = company
        
        # Investment (negative)
        year_idx = entry_yr - vintage_year
        if 0 <= year_idx < len(cash_flows):
            cash_flows[year_idx] -= invested
        
        # Exit (positive)
        exit_idx = exit_yr - vintage_year
        if 0 <= exit_idx < len(cash_flows):
            result = [r for r in deal_results if r['name'] == name][0]
            cash_flows[exit_idx] += result['exit_value']
    
    # Add management fees (negative)
    for year in range(10):
        if year < len(cash_flows):
            cash_flows[year] -= fund_size * mgmt_fee_rate
    
    # Calculate IRR
    try:
        gross_irr = np.irr(cash_flows)
    except:
        gross_irr = (gross_moic ** (1/6)) - 1  # 6-year average
    
    print(f"\nGross MOIC:          {gross_moic:.2f}x")
    print(f"Gross IRR:           {gross_irr*100:.1f}%")
    
    # Category breakdown
    print("\n" + "-"*80)
    print("PORTFOLIO BY CATEGORY:")
    print("-"*80)
    
    categories = {}
    for result in deal_results:
        cat = result['category']
        if cat not in categories:
            categories[cat] = {'count': 0, 'invested': 0, 'proceeds': 0}
        categories[cat]['count'] += 1
        categories[cat]['invested'] += result['invested']
        categories[cat]['proceeds'] += result['exit_value']
    
    for cat, data in sorted(categories.items()):
        count = data['count']
        invested = data['invested']
        proceeds = data['proceeds']
        moic = proceeds / invested
        contribution = (proceeds - invested) / (total_proceeds - total_invested) * 100
        
        print(f"\n{cat}:")
        print(f"  Deals:             {count}")
        print(f"  Invested:          €{invested:.0f}M")
        print(f"  Proceeds:          €{proceeds:.0f}M")
        print(f"  MOIC:              {moic:.2f}x")
        print(f"  % of Profit:       {contribution:.1f}%")
    
    # Net returns to LPs
    print("\n" + "="*80)
    print("NET RETURNS TO LPs:")
    print("="*80)
    
    # Simplified waterfall
    lp_commitment = fund_size * 0.98
    total_mgmt_fees = fund_size * mgmt_fee_rate * 10
    proceeds_after_fees = total_proceeds - total_mgmt_fees
    
    # Preferred return
    avg_holding = 6
    preferred_return = lp_commitment * ((1 + hurdle_rate) ** avg_holding - 1)
    
    # Carry calculation
    profit_after_hurdle = proceeds_after_fees - lp_commitment - preferred_return
    carry = max(0, profit_after_hurdle * carry_rate)
    
    # LP proceeds
    lp_proceeds = proceeds_after_fees - carry
    lp_moic = lp_proceeds / lp_commitment
    lp_irr = (lp_moic ** (1/avg_holding)) - 1
    
    print(f"LP Commitment:       €{lp_commitment:.0f}M")
    print(f"Gross Proceeds:      €{total_proceeds:.0f}M")
    print(f"Less: Mgmt Fees:     (€{total_mgmt_fees:.0f}M)")
    print(f"Less: GP Carry:      (€{carry:.0f}M)")
    print(f"Net to LPs:          €{lp_proceeds:.0f}M")
    print(f"\nLP Net MOIC:         {lp_moic:.2f}x")
    print(f"LP Net IRR:          {lp_irr*100:.1f}%")
    
    # Performance evaluation
    print("\n" + "="*80)
    print("FUND PERFORMANCE EVALUATION:")
    print("="*80)
    
    print(f"\n📊 Summary:")
    print(f"   Gross MOIC:       {gross_moic:.2f}x")
    print(f"   Gross IRR:        {gross_irr*100:.1f}%")
    print(f"   Net MOIC (LP):    {lp_moic:.2f}x")
    print(f"   Net IRR (LP):     {lp_irr*100:.1f}%")
    
    print(f"\n🎯 Quartile Ranking:")
    if lp_irr >= 0.20:
        ranking = "TOP QUARTILE"
        emoji = "🏆"
    elif lp_irr >= 0.15:
        ranking = "UPPER MID QUARTILE"
        emoji = "✅"
    elif lp_irr >= 0.10:
        ranking = "LOWER MID QUARTILE"
        emoji = "🟡"
    else:
        ranking = "BOTTOM QUARTILE"
        emoji = "❌"
    
    print(f"   {emoji} {ranking}")
    print(f"   ({lp_irr*100:.1f}% net IRR to LPs)")
    
    print(f"\n💡 Key Insights:")
    print(f"   • {len([r for r in deal_results if r['moic'] >= 3.0])} deals returned 3.0x+")
    print(f"   • {len([r for r in deal_results if r['moic'] < 1.0])} deals lost money")
    print(f"   • Power law in action: Top deals drive returns")
    print(f"   • Diversification across {len(portfolio)} companies")
    
    print("\n" + "="*80)
    print("FUND MODEL COMPLETE!")
    print("="*80)
    
    return {
        'gross_moic': gross_moic,
        'gross_irr': gross_irr,
        'lp_moic': lp_moic,
        'lp_irr': lp_irr,
        'total_invested': total_invested,
        'total_proceeds': total_proceeds
    }


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "█"*80)
    print("MODULE 07 - PE FUND MODELING: SOLUTIONS TO PRACTICE EXERCISES")
    print("█"*80)
    print("\nGP-quality fund modeling - ready for Blackstone/KKR!")
    print("Master these to think like a PE General Partner!\n")
    
    # Exercise 1: Fund quick analysis
    ex1_results = exercise_1_fund_quick_analysis()
    
    # Exercise 2: GP vs LP economics
    ex2_results = exercise_2_gp_vs_lp_economics()
    
    # Exercise 3: Waterfall distribution
    ex3_results = exercise_3_waterfall_distribution()
    
    # Exercise 4: Complete fund model
    ex4_results = exercise_4_complete_fund_model()
    
    print("\n" + "█"*80)
    print("ALL EXERCISES COMPLETED!")
    print("█"*80)
    print("\n✅ Exercise 1: Fund Quick Analysis - DONE")
    print("✅ Exercise 2: GP vs LP Economics - DONE")
    print("✅ Exercise 3: Waterfall Distribution - DONE")
    print("✅ Exercise 4: Complete Fund Model - DONE")
    print("\n🎉 Congratulations! You now model PE funds like a GP!")
    print("\n💼 Ready to manage a PE fund!")
    print("\n📚 Next up: Module 08 - Advanced Topics")
    print("█"*80 + "\n")
