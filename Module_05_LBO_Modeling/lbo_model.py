"""
LBO (Leveraged Buyout) Model

Complete LBO model for Private Equity analysis including:
- Sources & Uses
- Debt Schedule
- Cash Flow Waterfall
- Returns Analysis (IRR, MOIC)
"""

import numpy as np
import pandas as pd
from datetime import datetime

class LBOModel:
    """
    Comprehensive Leveraged Buyout Model
    
    Models a PE acquisition with debt financing, operations over holding period,
    and exit to calculate returns (IRR and MOIC)
    """
    
    def __init__(self, company_name, transaction_date):
        self.company_name = company_name
        self.transaction_date = transaction_date
        
        # Transaction assumptions
        self.purchase_price = 0.0
        self.entry_multiple = 0.0
        self.entry_ebitda = 0.0
        
        # Financing structure
        self.equity_contribution = 0.0
        self.senior_debt = 0.0
        self.subordinated_debt = 0.0
        self.senior_debt_rate = 0.0
        self.subordinated_debt_rate = 0.0
        
        # Operating assumptions
        self.holding_period = 5
        self.revenue_growth_rates = []
        self.ebitda_margin = 0.0
        self.tax_rate = 0.0
        self.capex_pct_revenue = 0.0
        self.nwc_pct_revenue = 0.0
        self.da_pct_revenue = 0.0
        
        # Exit assumptions
        self.exit_multiple = 0.0
        
        # Results
        self.projections = None
        self.debt_schedule = None
        self.cash_flows = None
        self.moic = 0.0
        self.irr = 0.0
    
    def set_transaction_assumptions(self, entry_ebitda, entry_multiple):
        """Set purchase price based on entry multiple"""
        self.entry_ebitda = entry_ebitda
        self.entry_multiple = entry_multiple
        self.purchase_price = entry_ebitda * entry_multiple
    
    def set_financing_structure(self, equity_pct, senior_debt_multiple, 
                                sub_debt_multiple, senior_rate, sub_rate):
        """
        Set up debt financing structure
        
        Parameters:
        -----------
        equity_pct : float
            Equity as % of purchase price
        senior_debt_multiple : float
            Senior debt as multiple of EBITDA
        sub_debt_multiple : float
            Subordinated debt as multiple of EBITDA
        senior_rate : float
            Interest rate on senior debt
        sub_rate : float
            Interest rate on subordinated debt
        """
        self.senior_debt = self.entry_ebitda * senior_debt_multiple
        self.subordinated_debt = self.entry_ebitda * sub_debt_multiple
        
        total_debt = self.senior_debt + self.subordinated_debt
        self.equity_contribution = self.purchase_price - total_debt
        
        self.senior_debt_rate = senior_rate
        self.subordinated_debt_rate = sub_rate
    
    def set_operating_assumptions(self, revenue_growth_rates, ebitda_margin, 
                                  tax_rate, capex_pct, nwc_pct, da_pct):
        """Set operating model assumptions"""
        self.revenue_growth_rates = revenue_growth_rates
        self.holding_period = len(revenue_growth_rates)
        self.ebitda_margin = ebitda_margin
        self.tax_rate = tax_rate
        self.capex_pct_revenue = capex_pct
        self.nwc_pct_revenue = nwc_pct
        self.da_pct_revenue = da_pct
    
    def set_exit_assumptions(self, exit_multiple):
        """Set exit valuation multiple"""
        self.exit_multiple = exit_multiple
    
    def build_sources_and_uses(self):
        """Create sources and uses of funds table"""
        uses = {
            'Purchase Equity': [self.purchase_price],
            'Transaction Fees': [self.purchase_price * 0.02],  # 2% fees
            'Financing Fees': [(self.senior_debt + self.subordinated_debt) * 0.03]  # 3% fees
        }
        total_uses = sum([v[0] for v in uses.values()])
        
        sources = {
            'Senior Debt': [self.senior_debt],
            'Subordinated Debt': [self.subordinated_debt],
            'Equity Contribution': [total_uses - self.senior_debt - self.subordinated_debt]
        }
        
        self.equity_contribution = sources['Equity Contribution'][0]
        
        sources_df = pd.DataFrame(sources).T
        sources_df.columns = ['Amount']
        
        uses_df = pd.DataFrame(uses).T
        uses_df.columns = ['Amount']
        
        return {
            'Sources': sources_df,
            'Uses': uses_df,
            'Total': total_uses
        }
    
    def build_operating_model(self):
        """Build financial projections"""
        years = list(range(1, self.holding_period + 1))
        
        # Calculate base revenue from EBITDA and margin
        base_revenue = self.entry_ebitda / self.ebitda_margin
        
        # Revenue projections
        revenues = []
        current_revenue = base_revenue
        
        for growth_rate in self.revenue_growth_rates:
            current_revenue *= (1 + growth_rate)
            revenues.append(current_revenue)
        
        # EBITDA
        ebitdas = [rev * self.ebitda_margin for rev in revenues]
        
        # D&A
        da_values = [rev * self.da_pct_revenue for rev in revenues]
        
        # EBIT
        ebits = [ebitda - da for ebitda, da in zip(ebitdas, da_values)]
        
        # Interest expense (calculated from debt schedule)
        # Simplified: using opening debt balances
        interest_expenses = []
        senior_balance = self.senior_debt
        sub_balance = self.subordinated_debt
        
        for _ in years:
            interest = (senior_balance * self.senior_debt_rate + 
                       sub_balance * self.subordinated_debt_rate)
            interest_expenses.append(interest)
        
        # EBT (EBIT - Interest)
        ebts = [ebit - interest for ebit, interest in zip(ebits, interest_expenses)]
        
        # Taxes
        taxes = [ebt * self.tax_rate if ebt > 0 else 0 for ebt in ebts]
        
        # Net Income
        net_incomes = [ebt - tax for ebt, tax in zip(ebts, taxes)]
        
        # Add back D&A
        nopat_plus_da = [ni + da for ni, da in zip(net_incomes, da_values)]
        
        # CapEx
        capex = [rev * self.capex_pct_revenue for rev in revenues]
        
        # Change in NWC
        nwc_changes = []
        prev_nwc = base_revenue * self.nwc_pct_revenue
        
        for rev in revenues:
            current_nwc = rev * self.nwc_pct_revenue
            nwc_changes.append(current_nwc - prev_nwc)
            prev_nwc = current_nwc
        
        # Free Cash Flow (before debt service)
        fcfs = [
            ni_da - cx - nwc
            for ni_da, cx, nwc in zip(nopat_plus_da, capex, nwc_changes)
        ]
        
        # Create projections DataFrame
        self.projections = pd.DataFrame({
            'Year': years,
            'Revenue': revenues,
            'EBITDA': ebitdas,
            'D&A': da_values,
            'EBIT': ebits,
            'Interest': interest_expenses,
            'EBT': ebts,
            'Taxes': taxes,
            'Net_Income': net_incomes,
            'Add_DA': da_values,
            'Less_CapEx': capex,
            'Less_NWC': nwc_changes,
            'FCF': fcfs
        })
        
        return self.projections
    
    def build_debt_schedule(self):
        """Build debt amortization schedule"""
        years = list(range(1, self.holding_period + 1))
        
        senior_balances = [self.senior_debt]
        sub_balances = [self.subordinated_debt]
        
        # Simplified debt paydown: use excess cash flow
        # In practice, would have specific amortization schedules
        
        for year_idx in range(len(years)):
            # Cash available for debt paydown
            cash_available = self.projections.loc[year_idx, 'FCF']
            
            # Mandatory amortization (e.g., 5% of original senior debt)
            mandatory_amort = self.senior_debt * 0.05
            
            # Pay down senior debt first
            senior_payment = min(mandatory_amort, senior_balances[-1])
            new_senior = senior_balances[-1] - senior_payment
            
            # Remaining cash
            remaining_cash = cash_available - senior_payment
            
            # Optional: pay down more if cash available
            if remaining_cash > 0 and new_senior > 0:
                optional_paydown = min(remaining_cash * 0.5, new_senior)
                new_senior -= optional_paydown
            
            senior_balances.append(max(0, new_senior))
            sub_balances.append(sub_balances[-1])  # Sub debt stays constant
        
        self.debt_schedule = pd.DataFrame({
            'Year': [0] + years,
            'Senior_Debt': senior_balances,
            'Sub_Debt': sub_balances,
            'Total_Debt': [s + sub for s, sub in zip(senior_balances, sub_balances)]
        })
        
        return self.debt_schedule
    
    def calculate_returns(self):
        """Calculate IRR and MOIC"""
        # Exit valuation
        exit_ebitda = self.projections['EBITDA'].iloc[-1]
        exit_enterprise_value = exit_ebitda * self.exit_multiple
        
        # Less: remaining debt
        final_debt = self.debt_schedule['Total_Debt'].iloc[-1]
        
        # Exit equity value
        exit_equity_value = exit_enterprise_value - final_debt
        
        # MOIC
        self.moic = exit_equity_value / self.equity_contribution
        
        # IRR (approximation)
        self.irr = (self.moic ** (1 / self.holding_period)) - 1
        
        return {
            'Entry_EV': self.purchase_price,
            'Entry_Multiple': self.entry_multiple,
            'Entry_EBITDA': self.entry_ebitda,
            'Exit_EV': exit_enterprise_value,
            'Exit_Multiple': self.exit_multiple,
            'Exit_EBITDA': exit_ebitda,
            'Exit_Debt': final_debt,
            'Exit_Equity_Value': exit_equity_value,
            'Equity_Invested': self.equity_contribution,
            'MOIC': self.moic,
            'IRR': self.irr
        }
    
    def display_summary(self):
        """Display LBO summary"""
        print(f"\n{'='*70}")
        print(f"LBO ANALYSIS: {self.company_name}")
        print(f"{'='*70}")
        print(f"Transaction Date: {self.transaction_date}")
        
        # Sources and Uses
        su = self.build_sources_and_uses()
        
        print(f"\n{'SOURCES & USES':-^70}")
        print("\nSources of Funds:")
        print(su['Sources'].to_string())
        print(f"\nTotal Sources: ${su['Total']:,.0f}M")
        
        print("\nUses of Funds:")
        print(su['Uses'].to_string())
        print(f"\nTotal Uses: ${su['Total']:,.0f}M")
        
        # Returns
        returns = self.calculate_returns()
        
        print(f"\n{'TRANSACTION SUMMARY':-^70}")
        print(f"Purchase Price:      ${self.purchase_price:>12,.0f}M")
        print(f"Entry Multiple:      {self.entry_multiple:>12.1f}x")
        print(f"Entry EBITDA:        ${self.entry_ebitda:>12,.0f}M")
        print(f"\nEquity Invested:     ${self.equity_contribution:>12,.0f}M")
        print(f"Senior Debt:         ${self.senior_debt:>12,.0f}M")
        print(f"Sub Debt:            ${self.subordinated_debt:>12,.0f}M")
        print(f"Total Debt:          ${self.senior_debt + self.subordinated_debt:>12,.0f}M")
        print(f"Debt/EBITDA:         {(self.senior_debt + self.subordinated_debt)/self.entry_ebitda:>12.1f}x")
        
        print(f"\n{'EXIT ANALYSIS':-^70}")
        print(f"Holding Period:      {self.holding_period:>12} years")
        print(f"Exit EBITDA:         ${returns['Exit_EBITDA']:>12,.0f}M")
        print(f"Exit Multiple:       {returns['Exit_Multiple']:>12.1f}x")
        print(f"Exit EV:             ${returns['Exit_EV']:>12,.0f}M")
        print(f"Less: Exit Debt:     ${returns['Exit_Debt']:>12,.0f}M")
        print(f"Exit Equity Value:   ${returns['Exit_Equity_Value']:>12,.0f}M")
        
        print(f"\n{'RETURNS':-^70}")
        print(f"MOIC:                {self.moic:>12.2f}x")
        print(f"IRR:                 {self.irr:>11.1%}")
        
        print(f"\n{'='*70}\n")


def example_lbo_model():
    """Complete example of building an LBO model"""
    
    # Initialize model
    model = LBOModel("RetailCo", "2025-01-01")
    
    # Transaction assumptions
    model.set_transaction_assumptions(
        entry_ebitda=100,
        entry_multiple=8.0
    )
    
    # Financing structure
    model.set_financing_structure(
        equity_pct=0.40,
        senior_debt_multiple=4.0,
        sub_debt_multiple=1.5,
        senior_rate=0.06,
        sub_rate=0.10
    )
    
    # Operating assumptions
    model.set_operating_assumptions(
        revenue_growth_rates=[0.08, 0.08, 0.07, 0.06, 0.05],
        ebitda_margin=0.20,
        tax_rate=0.25,
        capex_pct=0.03,
        nwc_pct=0.10,
        da_pct=0.025
    )
    
    # Exit assumptions
    model.set_exit_assumptions(exit_multiple=9.0)
    
    # Build model
    model.build_operating_model()
    model.build_debt_schedule()
    
    # Display results
    model.display_summary()
    
    # Show projections
    print("OPERATING PROJECTIONS")
    print("=" * 70)
    print(model.projections.to_string(index=False))
    
    print("\nDEBT SCHEDULE")
    print("=" * 70)
    print(model.debt_schedule.to_string(index=False))
    
    return model


if __name__ == "__main__":
    model = example_lbo_model()
