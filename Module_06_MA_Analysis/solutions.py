"""
Solutions to Module 06 Practice Exercises - M&A Analysis

Master M&A like an Investment Banking analyst!
These solutions show complete merger analysis workflows.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple


# =============================================================================
# EXERCISE 1: Quick Accretion/Dilution Check
# =============================================================================

def exercise_1_quick_accretion_dilution():
    """
    Quick accretion/dilution analysis - the "back of napkin" M&A math.
    
    THIS IS THE MOST IMPORTANT M&A METRIC!
    
    Deal Parameters:
    - Acquirer: $200M earnings, 100M shares, $50/share
    - Target: $30M earnings, 20M shares, $40/share
    - Offer: $50/share (25% premium), all stock
    """
    print("\n" + "="*80)
    print("EXERCISE 1: QUICK ACCRETION/DILUTION CHECK")
    print("="*80)
    
    # Acquirer information
    acquirer_earnings = 200.0  # $M
    acquirer_shares = 100.0    # M shares
    acquirer_stock_price = 50.0
    acquirer_eps = acquirer_earnings / acquirer_shares
    
    print("\nACQUIRER (BuyerCo):")
    print("-" * 80)
    print(f"Net Income:          ${acquirer_earnings:.0f}M")
    print(f"Shares Outstanding:  {acquirer_shares:.0f}M")
    print(f"Stock Price:         ${acquirer_stock_price:.2f}")
    print(f"EPS:                 ${acquirer_eps:.2f}")
    print(f"P/E Ratio:           {acquirer_stock_price/acquirer_eps:.1f}x")
    
    # Target information
    target_earnings = 30.0     # $M
    target_shares = 20.0       # M shares
    target_current_price = 40.0
    target_eps = target_earnings / target_shares
    
    print("\nTARGET (TargetCo):")
    print("-" * 80)
    print(f"Net Income:          ${target_earnings:.0f}M")
    print(f"Shares Outstanding:  {target_shares:.0f}M")
    print(f"Current Price:       ${target_current_price:.2f}")
    print(f"EPS:                 ${target_eps:.2f}")
    print(f"P/E Ratio:           {target_current_price/target_eps:.1f}x")
    
    # Deal terms
    offer_price = 50.0
    premium = (offer_price - target_current_price) / target_current_price
    
    print("\nDEAL TERMS:")
    print("-" * 80)
    print(f"Offer Price:         ${offer_price:.2f}/share")
    print(f"Premium:             {premium*100:.1f}%")
    print(f"Total Consideration: ${offer_price * target_shares:.0f}M")
    print(f"Payment Method:      100% Stock")
    
    # Calculate shares issued
    total_consideration = offer_price * target_shares
    shares_issued = total_consideration / acquirer_stock_price
    
    print("\nSHARES ISSUED:")
    print("-" * 80)
    print(f"Consideration:       ${total_consideration:.0f}M")
    print(f"÷ Acquirer Price:    ${acquirer_stock_price:.2f}")
    print(f"= New Shares:        {shares_issued:.2f}M")
    
    # Calculate combined company
    combined_earnings = acquirer_earnings + target_earnings
    combined_shares = acquirer_shares + shares_issued
    new_eps = combined_earnings / combined_shares
    
    print("\nCOMBINED COMPANY:")
    print("-" * 80)
    print(f"Combined Earnings:   ${combined_earnings:.0f}M")
    print(f"Combined Shares:     {combined_shares:.2f}M")
    print(f"New EPS:             ${new_eps:.2f}")
    
    # Accretion/Dilution
    accretion = (new_eps - acquirer_eps) / acquirer_eps
    
    print("\n" + "="*80)
    print("ACCRETION/DILUTION ANALYSIS:")
    print("="*80)
    print(f"Old Acquirer EPS:    ${acquirer_eps:.2f}")
    print(f"New Combined EPS:    ${new_eps:.2f}")
    print(f"Change:              ${new_eps - acquirer_eps:+.2f}")
    print(f"Accretion/Dilution:  {accretion*100:+.1f}%")
    
    if accretion > 0:
        print(f"\n✅ ACCRETIVE by {accretion*100:.1f}%")
        print("   → Good for acquirer shareholders!")
        print("   → Deal likely to be approved by Board")
    elif accretion == 0:
        print("\n🟡 NEUTRAL (No change to EPS)")
        print("   → Synergies needed to justify deal")
    else:
        print(f"\n❌ DILUTIVE by {abs(accretion)*100:.1f}%")
        print("   → Bad for acquirer shareholders!")
        print("   → Need strong synergy story or walk away")
    
    # Additional insights
    print("\n" + "-"*80)
    print("KEY INSIGHTS:")
    print("-"*80)
    
    # Dilution from shares issued
    ownership_dilution = shares_issued / combined_shares
    print(f"1. Existing shareholders diluted by {ownership_dilution*100:.1f}%")
    print(f"   (They now own {(1-ownership_dilution)*100:.1f}% of combined company)")
    
    # P/E arbitrage
    acquirer_pe = acquirer_stock_price / acquirer_eps
    target_pe = target_current_price / target_eps
    print(f"\n2. P/E Arbitrage:")
    print(f"   Acquirer P/E: {acquirer_pe:.1f}x")
    print(f"   Target P/E:   {target_pe:.1f}x")
    if acquirer_pe > target_pe:
        print(f"   → Buying lower P/E with higher P/E stock = Accretive!")
    else:
        print(f"   → Buying higher P/E with lower P/E stock = Dilutive!")
    
    return {
        'old_eps': acquirer_eps,
        'new_eps': new_eps,
        'accretion_percent': accretion,
        'shares_issued': shares_issued
    }


# =============================================================================
# EXERCISE 2: Valuation Range
# =============================================================================

def exercise_2_valuation_range():
    """
    Calculate valuation range using multiple methodologies.
    
    NEVER rely on just one valuation method!
    Use triangulation to establish credible range.
    """
    print("\n" + "="*80)
    print("EXERCISE 2: TARGET VALUATION RANGE")
    print("="*80)
    
    # Target financials
    target_ebitda = 50.0  # $M
    target_revenue = 300.0  # $M
    
    print("\nTARGET COMPANY FINANCIALS:")
    print("-" * 80)
    print(f"Revenue:             ${target_revenue:.0f}M")
    print(f"EBITDA:              ${target_ebitda:.0f}M")
    print(f"EBITDA Margin:       {(target_ebitda/target_revenue)*100:.1f}%")
    
    # Method 1: Trading Comparables
    print("\n" + "="*80)
    print("METHOD 1: TRADING COMPARABLES")
    print("="*80)
    
    trading_comp_multiple = 8.0  # x EBITDA
    trading_comp_value = target_ebitda * trading_comp_multiple
    
    print(f"Comparable Companies Average Multiple: {trading_comp_multiple:.1f}x EBITDA")
    print(f"Target EBITDA:       ${target_ebitda:.0f}M")
    print(f"Implied EV:          ${trading_comp_value:.0f}M")
    print(f"\n💡 NOTE: Trading multiples reflect MINORITY stake")
    print(f"   (No control premium included)")
    
    # Method 2: Precedent Transactions
    print("\n" + "="*80)
    print("METHOD 2: PRECEDENT TRANSACTIONS")
    print("="*80)
    
    deal_comp_multiple = 9.5  # x EBITDA
    deal_comp_value = target_ebitda * deal_comp_multiple
    
    print(f"Recent M&A Deals Average Multiple: {deal_comp_multiple:.1f}x EBITDA")
    print(f"Target EBITDA:       ${target_ebitda:.0f}M")
    print(f"Implied EV:          ${deal_comp_value:.0f}M")
    
    # Control premium
    control_premium = (deal_comp_multiple - trading_comp_multiple) / trading_comp_multiple
    print(f"\n💡 Control Premium: {control_premium*100:.1f}%")
    print(f"   (Premium buyers pay for CONTROL)")
    
    # Method 3: DCF
    print("\n" + "="*80)
    print("METHOD 3: DCF VALUATION")
    print("="*80)
    
    dcf_value = 500.0  # $M (given)
    
    print(f"DCF Enterprise Value: ${dcf_value:.0f}M")
    print(f"Implied Multiple:     {dcf_value/target_ebitda:.1f}x EBITDA")
    print(f"\n💡 DCF reflects intrinsic value based on cash flows")
    print(f"   (Not influenced by market sentiment)")
    
    # Valuation Summary
    print("\n" + "="*80)
    print("VALUATION SUMMARY:")
    print("="*80)
    
    valuation_summary = pd.DataFrame({
        'Method': ['Trading Comps', 'Deal Comps', 'DCF'],
        'Multiple (x)': [trading_comp_multiple, deal_comp_multiple, dcf_value/target_ebitda],
        'Enterprise Value ($M)': [trading_comp_value, deal_comp_value, dcf_value]
    })
    
    print(valuation_summary.to_string(index=False))
    
    # Calculate range
    min_value = min(trading_comp_value, deal_comp_value, dcf_value)
    max_value = max(trading_comp_value, deal_comp_value, dcf_value)
    mid_value = np.mean([trading_comp_value, deal_comp_value, dcf_value])
    
    print("\n" + "="*80)
    print("VALUATION RANGE:")
    print("="*80)
    print(f"Minimum (Floor):     ${min_value:.0f}M  ({min_value/target_ebitda:.1f}x)")
    print(f"Midpoint:            ${mid_value:.0f}M  ({mid_value/target_ebitda:.1f}x)")
    print(f"Maximum (Ceiling):   ${max_value:.0f}M  ({max_value/target_ebitda:.1f}x)")
    
    # Recommendation
    print("\n" + "-"*80)
    print("NEGOTIATION STRATEGY:")
    print("-"*80)
    print(f"💡 Opening Bid:      ${min_value:.0f}M (low-ball)")
    print(f"🎯 Target Price:     ${mid_value:.0f}M (fair value)")
    print(f"🚨 Walk-Away Price:  ${max_value:.0f}M (absolute max)")
    print(f"\n   DO NOT exceed ${max_value:.0f}M - you'll destroy value!")
    
    return {
        'min_value': min_value,
        'mid_value': mid_value,
        'max_value': max_value,
        'valuation_range': (min_value, max_value)
    }


# =============================================================================
# EXERCISE 3: Synergy Analysis
# =============================================================================

def exercise_3_synergy_analysis():
    """
    Comprehensive synergy analysis for retail merger.
    
    BE CONSERVATIVE! Most companies overestimate synergies by 50%+
    """
    print("\n" + "="*80)
    print("EXERCISE 3: SYNERGY ANALYSIS - Retail Merger")
    print("="*80)
    
    # Combined company metrics
    combined_revenue = 2_000.0  # $M
    combined_sga = 400.0        # $M
    combined_headcount = 10_000
    combined_stores = 500
    combined_it_budget = 50.0   # $M
    
    print("\nCOMBINED COMPANY:")
    print("-" * 80)
    print(f"Revenue:             ${combined_revenue:.0f}M")
    print(f"SG&A:                ${combined_sga:.0f}M ({combined_sga/combined_revenue*100:.1f}% of revenue)")
    print(f"Headcount:           {combined_headcount:,} employees")
    print(f"Stores:              {combined_stores:,} locations")
    print(f"IT Budget:           ${combined_it_budget:.0f}M")
    
    # COST SYNERGIES
    print("\n" + "="*80)
    print("COST SYNERGIES (Easier to Achieve)")
    print("="*80)
    
    cost_synergies = {}
    
    # 1. Headcount reduction
    headcount_reduction_pct = 0.10
    avg_comp_per_employee = combined_sga * 0.60 / combined_headcount  # 60% of SG&A is personnel
    headcount_eliminated = combined_headcount * headcount_reduction_pct
    headcount_synergy = headcount_eliminated * avg_comp_per_employee
    cost_synergies['Headcount Reduction'] = headcount_synergy
    
    print(f"\n1. HEADCOUNT REDUCTION:")
    print(f"   - Eliminate {headcount_reduction_pct*100:.0f}% of workforce")
    print(f"   - Employees cut: {headcount_eliminated:,.0f}")
    print(f"   - Avg comp: ${avg_comp_per_employee:.0f}k/employee")
    print(f"   - Annual savings: ${headcount_synergy:.1f}M")
    print(f"   💡 Focus: Duplicate roles (HR, Finance, Marketing)")
    
    # 2. Store closures
    store_closure_pct = 0.15
    avg_rent_per_store = 0.5  # $M per store
    stores_closed = combined_stores * store_closure_pct
    store_synergy = stores_closed * avg_rent_per_store
    cost_synergies['Store Closures'] = store_synergy
    
    print(f"\n2. STORE CLOSURES:")
    print(f"   - Close {store_closure_pct*100:.0f}% of stores")
    print(f"   - Stores closed: {stores_closed:,.0f}")
    print(f"   - Avg rent: ${avg_rent_per_store:.1f}M/store")
    print(f"   - Annual savings: ${store_synergy:.1f}M")
    print(f"   💡 Focus: Overlapping locations within 5 miles")
    
    # 3. IT consolidation
    it_reduction_pct = 0.40
    it_synergy = combined_it_budget * it_reduction_pct
    cost_synergies['IT Consolidation'] = it_synergy
    
    print(f"\n3. IT SYSTEM CONSOLIDATION:")
    print(f"   - Reduce {it_reduction_pct*100:.0f}% of IT budget")
    print(f"   - Annual savings: ${it_synergy:.1f}M")
    print(f"   💡 Focus: Eliminate duplicate ERP, CRM, POS systems")
    
    # 4. Procurement
    procurement_pct = 0.05
    combined_cogs = combined_revenue * 0.60  # Assume 60% COGS
    procurement_synergy = combined_cogs * procurement_pct
    cost_synergies['Procurement'] = procurement_synergy
    
    print(f"\n4. PROCUREMENT SAVINGS:")
    print(f"   - {procurement_pct*100:.0f}% reduction in COGS")
    print(f"   - Combined COGS: ${combined_cogs:.0f}M")
    print(f"   - Annual savings: ${procurement_synergy:.1f}M")
    print(f"   💡 Focus: Volume discounts from suppliers")
    
    total_cost_synergies = sum(cost_synergies.values())
    
    print(f"\n{'='*80}")
    print(f"TOTAL COST SYNERGIES: ${total_cost_synergies:.1f}M annually")
    print(f"{'='*80}")
    
    # REVENUE SYNERGIES
    print("\n" + "="*80)
    print("REVENUE SYNERGIES (Harder to Achieve - BE SKEPTICAL!)")
    print("="*80)
    
    revenue_synergies = {}
    
    # 1. Cross-selling
    cross_sell_pct = 0.05  # Conservative!
    cross_sell_synergy = combined_revenue * cross_sell_pct
    revenue_synergies['Cross-Selling'] = cross_sell_synergy
    
    print(f"\n1. CROSS-SELLING:")
    print(f"   - {cross_sell_pct*100:.0f}% revenue uplift")
    print(f"   - Annual revenue increase: ${cross_sell_synergy:.1f}M")
    print(f"   💡 Example: Sell Company A products in Company B stores")
    print(f"   ⚠️  WARNING: Usually overstated - assume 50% haircut")
    
    # 2. Market expansion
    market_expansion_pct = 0.03
    market_expansion_synergy = combined_revenue * market_expansion_pct
    revenue_synergies['Market Expansion'] = market_expansion_synergy
    
    print(f"\n2. MARKET EXPANSION:")
    print(f"   - {market_expansion_pct*100:.0f}% revenue from new markets")
    print(f"   - Annual revenue increase: ${market_expansion_synergy:.1f}M")
    print(f"   💡 Example: Enter Company B's geographies")
    print(f"   ⚠️  WARNING: Takes 3-5 years to realize")
    
    total_revenue_synergies_gross = sum(revenue_synergies.values())
    haircut = 0.50  # Only count 50% of revenue synergies
    total_revenue_synergies = total_revenue_synergies_gross * haircut
    
    print(f"\n{'='*80}")
    print(f"TOTAL REVENUE SYNERGIES: ${total_revenue_synergies_gross:.1f}M (gross)")
    print(f"Haircut (50%):           ${total_revenue_synergies:.1f}M (net)")
    print(f"{'='*80}")
    print(f"⚠️  IB Rule: Apply 50% haircut to ALL revenue synergies!")
    
    # INTEGRATION COSTS
    print("\n" + "="*80)
    print("ONE-TIME INTEGRATION COSTS")
    print("="*80)
    
    integration_costs = {}
    
    # 1. Severance
    severance_multiple = 1.5  # 1.5x annual comp
    severance_cost = headcount_synergy * severance_multiple
    integration_costs['Severance'] = severance_cost
    
    print(f"\n1. SEVERANCE:")
    print(f"   - {headcount_eliminated:,.0f} employees × 1.5x comp")
    print(f"   - One-time cost: ${severance_cost:.1f}M")
    
    # 2. IT integration
    it_integration = 30.0
    integration_costs['IT Integration'] = it_integration
    
    print(f"\n2. IT SYSTEM INTEGRATION:")
    print(f"   - Migrate to single ERP/CRM/POS")
    print(f"   - One-time cost: ${it_integration:.1f}M")
    
    # 3. Store closure costs
    store_closure_cost = stores_closed * 0.3  # $0.3M per store
    integration_costs['Store Closures'] = store_closure_cost
    
    print(f"\n3. STORE CLOSURE COSTS:")
    print(f"   - Lease terminations, moving, etc.")
    print(f"   - One-time cost: ${store_closure_cost:.1f}M")
    
    # 4. Rebranding
    rebranding = 10.0
    integration_costs['Rebranding'] = rebranding
    
    print(f"\n4. REBRANDING:")
    print(f"   - New signage, marketing, etc.")
    print(f"   - One-time cost: ${rebranding:.1f}M")
    
    total_integration_costs = sum(integration_costs.values())
    
    print(f"\n{'='*80}")
    print(f"TOTAL INTEGRATION COSTS: ${total_integration_costs:.1f}M (one-time)")
    print(f"{'='*80}")
    
    # NPV CALCULATION
    print("\n" + "="*80)
    print("NPV OF SYNERGIES")
    print("="*80)
    
    # Assume EBITDA margin on revenue synergies
    ebitda_margin = 0.15
    revenue_synergy_ebitda = total_revenue_synergies * ebitda_margin
    
    total_annual_synergies = total_cost_synergies + revenue_synergy_ebitda
    
    # Perpetuity value (synergies last forever)
    wacc = 0.10
    pv_synergies = total_annual_synergies / wacc
    
    # Net of integration costs
    npv_synergies = pv_synergies - total_integration_costs
    
    print(f"\nAnnual Cost Synergies:   ${total_cost_synergies:.1f}M")
    print(f"Annual Revenue Synergies (EBITDA): ${revenue_synergy_ebitda:.1f}M")
    print(f"Total Annual Synergies:  ${total_annual_synergies:.1f}M")
    print(f"\nPV of Perpetuity @ {wacc*100:.0f}%:  ${pv_synergies:.1f}M")
    print(f"Less: Integration Costs: (${total_integration_costs:.1f}M)")
    print(f"\n{'='*80}")
    print(f"NET SYNERGY VALUE:       ${npv_synergies:.1f}M")
    print(f"{'='*80}")
    
    # What this means for valuation
    print("\n" + "-"*80)
    print("WHAT THIS MEANS FOR THE DEAL:")
    print("-"*80)
    print(f"💡 Maximum additional premium justified: ${npv_synergies:.1f}M")
    print(f"\n   Example:")
    print(f"   - Standalone value: $500M")
    print(f"   - Max offer with synergies: ${500 + npv_synergies:.1f}M")
    print(f"\n   If you pay more than this, you DESTROY value!")
    
    return {
        'cost_synergies': total_cost_synergies,
        'revenue_synergies': total_revenue_synergies,
        'integration_costs': total_integration_costs,
        'npv_synergies': npv_synergies
    }


# =============================================================================
# EXERCISE 4: Complete Merger Model
# =============================================================================

def exercise_4_complete_merger_model():
    """
    Build a complete merger model from scratch.
    
    This is what you'd present to the Board of Directors!
    """
    print("\n" + "="*80)
    print("EXERCISE 4: COMPLETE MERGER MODEL - TechCo Acquires StartupCo")
    print("="*80)
    
    # === STEP 1: COMPANY FINANCIALS ===
    print("\n" + "="*80)
    print("STEP 1: STANDALONE COMPANY FINANCIALS")
    print("="*80)
    
    # Acquirer (TechCo)
    print("\nACQUIRER - TechCo Inc.:")
    print("-" * 80)
    techco = {
        'revenue': 1_000.0,
        'ebitda': 100.0,
        'ebitda_margin': 0.10,
        'net_income': 60.0,
        'shares': 100.0,
        'stock_price': 50.0,
        'market_cap': 5_000.0
    }
    techco['eps'] = techco['net_income'] / techco['shares']
    techco['pe_ratio'] = techco['stock_price'] / techco['eps']
    
    for key, value in techco.items():
        if key in ['revenue', 'ebitda', 'net_income', 'market_cap']:
            print(f"{key.replace('_', ' ').title():<20} ${value:.0f}M")
        elif key in ['shares']:
            print(f"{key.replace('_', ' ').title():<20} {value:.0f}M")
        elif key in ['stock_price', 'eps']:
            print(f"{key.replace('_', ' ').title():<20} ${value:.2f}")
        elif key in ['ebitda_margin']:
            print(f"{key.replace('_', ' ').title():<20} {value*100:.1f}%")
        elif key in ['pe_ratio']:
            print(f"{key.replace('_', ' ').title():<20} {value:.1f}x")
    
    # Target (StartupCo)
    print("\nTARGET - StartupCo Inc.:")
    print("-" * 80)
    startupco = {
        'revenue': 200.0,
        'ebitda': 30.0,
        'ebitda_margin': 0.15,
        'net_income': 15.0,
        'shares': 20.0,
        'stock_price': 30.0,
        'market_cap': 600.0
    }
    startupco['eps'] = startupco['net_income'] / startupco['shares']
    startupco['pe_ratio'] = startupco['stock_price'] / startupco['eps']
    
    for key, value in startupco.items():
        if key in ['revenue', 'ebitda', 'net_income', 'market_cap']:
            print(f"{key.replace('_', ' ').title():<20} ${value:.0f}M")
        elif key in ['shares']:
            print(f"{key.replace('_', ' ').title():<20} {value:.0f}M")
        elif key in ['stock_price', 'eps']:
            print(f"{key.replace('_', ' ').title():<20} ${value:.2f}")
        elif key in ['ebitda_margin']:
            print(f"{key.replace('_', ' ').title():<20} {value*100:.1f}%")
        elif key in ['pe_ratio']:
            print(f"{key.replace('_', ' ').title():<20} {value:.1f}x")
    
    # === STEP 2: VALUATION ===
    print("\n" + "="*80)
    print("STEP 2: TARGET VALUATION")
    print("="*80)
    
    # Using 1.2x revenue multiple
    revenue_multiple = 1.2
    enterprise_value = startupco['revenue'] * revenue_multiple
    
    print(f"\nValuation Method:    Revenue Multiple")
    print(f"Target Revenue:      ${startupco['revenue']:.0f}M")
    print(f"Multiple:            {revenue_multiple:.1f}x")
    print(f"Enterprise Value:    ${enterprise_value:.0f}M")
    
    # Implied EBITDA multiple
    implied_ebitda_multiple = enterprise_value / startupco['ebitda']
    print(f"\nImplied EBITDA Multiple: {implied_ebitda_multiple:.1f}x")
    
    # Premium analysis
    premium = (enterprise_value - startupco['market_cap']) / startupco['market_cap']
    print(f"\nCurrent Market Cap:  ${startupco['market_cap']:.0f}M")
    print(f"Offer Value:         ${enterprise_value:.0f}M")
    print(f"Premium:             {premium*100:.1f}%")
    
    # === STEP 3: FINANCING STRUCTURE ===
    print("\n" + "="*80)
    print("STEP 3: FINANCING STRUCTURE")
    print("="*80)
    
    cash_percent = 0.60
    stock_percent = 0.40
    
    cash_consideration = enterprise_value * cash_percent
    stock_consideration = enterprise_value * stock_percent
    
    print(f"\nTotal Consideration: ${enterprise_value:.0f}M")
    print(f"\nFinancing Mix:")
    print(f"  Cash ({cash_percent*100:.0f}%):        ${cash_consideration:.0f}M")
    print(f"  Stock ({stock_percent*100:.0f}%):       ${stock_consideration:.0f}M")
    
    # Shares issued
    shares_issued = stock_consideration / techco['stock_price']
    
    print(f"\nShares Issued:")
    print(f"  Stock Value:       ${stock_consideration:.0f}M")
    print(f"  ÷ TechCo Price:    ${techco['stock_price']:.2f}")
    print(f"  = New Shares:      {shares_issued:.2f}M")
    
    # === STEP 4: SYNERGIES ===
    print("\n" + "="*80)
    print("STEP 4: SYNERGY ANALYSIS")
    print("="*80)
    
    annual_synergies = 20.0  # $M
    
    print(f"\nExpected Annual Synergies: ${annual_synergies:.0f}M")
    print(f"Synergy Breakdown:")
    print(f"  - Cost synergies:  ${annual_synergies * 0.70:.0f}M (70%)")
    print(f"  - Revenue synergies: ${annual_synergies * 0.30:.0f}M (30%)")
    
    # === STEP 5: PRO FORMA FINANCIALS ===
    print("\n" + "="*80)
    print("STEP 5: PRO FORMA COMBINED COMPANY")
    print("="*80)
    
    # Revenue
    pro_forma_revenue = techco['revenue'] + startupco['revenue']
    
    # EBITDA (including synergies)
    pro_forma_ebitda = techco['ebitda'] + startupco['ebitda'] + annual_synergies
    
    # Net Income (simplified - no tax on synergies for simplicity)
    pro_forma_net_income = techco['net_income'] + startupco['net_income'] + (annual_synergies * 0.75)
    
    # Shares
    pro_forma_shares = techco['shares'] + shares_issued
    
    # EPS
    pro_forma_eps = pro_forma_net_income / pro_forma_shares
    
    print(f"\nRevenue:             ${pro_forma_revenue:.0f}M")
    print(f"EBITDA:              ${pro_forma_ebitda:.0f}M")
    print(f"EBITDA Margin:       {(pro_forma_ebitda/pro_forma_revenue)*100:.1f}%")
    print(f"Net Income:          ${pro_forma_net_income:.1f}M")
    print(f"Shares Outstanding:  {pro_forma_shares:.2f}M")
    print(f"EPS:                 ${pro_forma_eps:.2f}")
    
    # === STEP 6: ACCRETION/DILUTION ===
    print("\n" + "="*80)
    print("STEP 6: ACCRETION/DILUTION ANALYSIS")
    print("="*80)
    
    accretion = (pro_forma_eps - techco['eps']) / techco['eps']
    
    print(f"\nTechCo Standalone EPS:   ${techco['eps']:.2f}")
    print(f"Pro Forma Combined EPS:  ${pro_forma_eps:.2f}")
    print(f"Change:                  ${pro_forma_eps - techco['eps']:+.2f}")
    print(f"\n{'='*80}")
    print(f"ACCRETION/DILUTION:      {accretion*100:+.1f}%")
    print(f"{'='*80}")
    
    if accretion > 0:
        print(f"\n✅ ACCRETIVE by {accretion*100:.1f}%")
        print(f"   Deal is GOOD for TechCo shareholders!")
    else:
        print(f"\n❌ DILUTIVE by {abs(accretion)*100:.1f}%")
        print(f"   Deal is BAD for TechCo shareholders!")
    
    # === STEP 7: SENSITIVITY ANALYSIS ===
    print("\n" + "="*80)
    print("STEP 7: SENSITIVITY ANALYSIS")
    print("="*80)
    
    print(f"\nEPS Accretion/(Dilution) % - Synergies vs Financing Mix")
    print("-" * 80)
    
    # Create sensitivity table
    synergy_scenarios = [10, 15, 20, 25, 30]  # $M
    stock_pct_scenarios = [0.20, 0.30, 0.40, 0.50, 0.60]
    
    sensitivity_results = []
    
    for synergy in synergy_scenarios:
        row = []
        for stock_pct in stock_pct_scenarios:
            # Recalculate with different assumptions
            temp_shares_issued = (enterprise_value * stock_pct) / techco['stock_price']
            temp_ni = techco['net_income'] + startupco['net_income'] + (synergy * 0.75)
            temp_shares = techco['shares'] + temp_shares_issued
            temp_eps = temp_ni / temp_shares
            temp_accretion = (temp_eps - techco['eps']) / techco['eps']
            row.append(temp_accretion * 100)
        sensitivity_results.append(row)
    
    sensitivity_df = pd.DataFrame(
        sensitivity_results,
        index=[f'${s}M' for s in synergy_scenarios],
        columns=[f'{int(sp*100)}%' for sp in stock_pct_scenarios]
    )
    sensitivity_df.index.name = 'Synergies ↓'
    sensitivity_df.columns.name = 'Stock % →'
    
    print(sensitivity_df.round(1))
    
    # === STEP 8: RECOMMENDATION ===
    print("\n" + "="*80)
    print("STEP 8: FINAL RECOMMENDATION")
    print("="*80)
    
    print(f"\n📊 DEAL SUMMARY:")
    print(f"   - Purchase Price: ${enterprise_value:.0f}M ({revenue_multiple:.1f}x Revenue)")
    print(f"   - Premium: {premium*100:.1f}%")
    print(f"   - Financing: {cash_percent*100:.0f}% Cash / {stock_percent*100:.0f}% Stock")
    print(f"   - Synergies: ${annual_synergies:.0f}M annually")
    print(f"   - EPS Accretion: {accretion*100:+.1f}%")
    
    print(f"\n✅ STRENGTHS:")
    print(f"   • {accretion*100:.1f}% EPS accretion - good for shareholders")
    print(f"   • Achievable synergies (${annual_synergies:.0f}M)")
    print(f"   • Balanced financing mix preserves balance sheet")
    print(f"   • Strategic fit (tech + startup)")
    
    print(f"\n⚠️  RISKS:")
    print(f"   • Integration complexity")
    print(f"   • Cultural differences (big tech vs startup)")
    print(f"   • Synergy execution risk")
    print(f"   • Customer/employee retention")
    
    print(f"\n🎯 FINAL RECOMMENDATION:")
    if accretion > 0.05:  # >5% accretion
        print(f"   ✅ PROCEED WITH ACQUISITION")
        print(f"   → Deal creates significant shareholder value")
        print(f"   → EPS accretion of {accretion*100:.1f}% justifies premium")
        print(f"   → Recommend approval by Board")
    elif accretion > 0:
        print(f"   🟡 PROCEED WITH CAUTION")
        print(f"   → Modest accretion ({accretion*100:.1f}%)")
        print(f"   → Heavily dependent on synergy execution")
        print(f"   → Consider renegotiating price")
    else:
        print(f"   ❌ DO NOT PROCEED")
        print(f"   → Deal is dilutive ({accretion*100:.1f}%)")
        print(f"   → Destroys shareholder value")
        print(f"   → Recommend walking away or renegotiating")
    
    print(f"\n{'='*80}")
    print(f"END OF MERGER ANALYSIS")
    print(f"{'='*80}")
    
    return {
        'enterprise_value': enterprise_value,
        'premium': premium,
        'accretion': accretion,
        'pro_forma_eps': pro_forma_eps,
        'synergies': annual_synergies
    }


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "█"*80)
    print("MODULE 06 - M&A ANALYSIS: SOLUTIONS TO PRACTICE EXERCISES")
    print("█"*80)
    print("\nIB-quality M&A analysis - ready for Goldman Sachs!")
    print("Master these to become an M&A expert!\n")
    
    # Exercise 1: Quick accretion/dilution
    ex1_results = exercise_1_quick_accretion_dilution()
    
    # Exercise 2: Valuation range
    ex2_results = exercise_2_valuation_range()
    
    # Exercise 3: Synergy analysis
    ex3_results = exercise_3_synergy_analysis()
    
    # Exercise 4: Complete merger model
    ex4_results = exercise_4_complete_merger_model()
    
    print("\n" + "█"*80)
    print("ALL EXERCISES COMPLETED!")
    print("█"*80)
    print("\n✅ Exercise 1: Quick Accretion/Dilution - DONE")
    print("✅ Exercise 2: Valuation Range - DONE")
    print("✅ Exercise 3: Synergy Analysis - DONE")
    print("✅ Exercise 4: Complete Merger Model - DONE")
    print("\n🎉 Congratulations! You now analyze M&A like an Investment Banker!")
    print("\n💼 Ready for real deal analysis!")
    print("\n📚 Next up: Module 07 - PE Modeling")
    print("█"*80 + "\n")
