"""
Complete DCF (Discounted Cash Flow) Valuation Model

This module contains a comprehensive DCF model for investment banking valuation.
"""
"""
Complete DCF Valuation Model
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class DCFModel:
    """
    Comprehensive Discounted Cash Flow Model
    
    This class builds a complete DCF valuation with:
    - Revenue projections
    - Operating model (EBITDA, D&A, EBIT)
    - Tax calculations
    - Working capital
    - CapEx
    - Free Cash Flow
    - Terminal Value
    - Enterprise and Equity Value
    """
    
    def __init__(self, company_name, ticker):
        self.company_name = company_name
        self.ticker = ticker
        self.model_date = datetime.now()
        
        # Historical data
        self.historical_years = []
        self.historical_revenue = []
        self.historical_ebitda = []
        
        # Assumptions
        self.projection_years = 5
        self.revenue_growth_rates = []
        self.ebitda_margin = 0.0
        self.tax_rate = 0.0
        self.nwc_pct_revenue = 0.0
        self.capex_pct_revenue = 0.0
        self.da_pct_revenue = 0.0
        
        # WACC components
        self.risk_free_rate = 0.0
        self.equity_risk_premium = 0.0
        self.beta = 0.0
        self.cost_of_debt = 0.0
        self.market_value_equity = 0.0
        self.market_value_debt = 0.0
        
        # Terminal value
        self.terminal_growth_rate = 0.0
        self.terminal_ebitda_multiple = 0.0
        
        # Results
        self.projections = None
        self.enterprise_value = 0.0
        self.equity_value = 0.0
        self.equity_value_per_share = 0.0
        
    def set_historical_data(self, years, revenue, ebitda):
        """Set historical financial data"""
        self.historical_years = years
        self.historical_revenue = revenue
        self.historical_ebitda = ebitda
    
    def set_revenue_assumptions(self, growth_rates):
        """Set revenue growth rate assumptions"""
        self.revenue_growth_rates = growth_rates
        self.projection_years = len(growth_rates)
    
    def set_operating_assumptions(self, ebitda_margin, tax_rate, 
                                  da_pct_revenue, capex_pct_revenue, 
                                  nwc_pct_revenue):
        """Set operating model assumptions"""
        self.ebitda_margin = ebitda_margin
        self.tax_rate = tax_rate
        self.da_pct_revenue = da_pct_revenue
        self.capex_pct_revenue = capex_pct_revenue
        self.nwc_pct_revenue = nwc_pct_revenue
    
    def set_wacc_assumptions(self, risk_free_rate, equity_risk_premium, beta,
                            cost_of_debt, mv_equity, mv_debt):
        """Set WACC calculation assumptions"""
        self.risk_free_rate = risk_free_rate
        self.equity_risk_premium = equity_risk_premium
        self.beta = beta
        self.cost_of_debt = cost_of_debt
        self.market_value_equity = mv_equity
        self.market_value_debt = mv_debt
    
    def set_terminal_assumptions(self, growth_rate, ebitda_multiple):
        """Set terminal value assumptions"""
        self.terminal_growth_rate = growth_rate
        self.terminal_ebitda_multiple = ebitda_multiple
    
    def calculate_wacc(self):
        """Calculate Weighted Average Cost of Capital"""
        # Cost of equity (CAPM)
        cost_of_equity = (self.risk_free_rate + 
                         self.beta * self.equity_risk_premium)
        
        # Total capital
        total_capital = self.market_value_equity + self.market_value_debt
        
        # Weights
        weight_equity = self.market_value_equity / total_capital
        weight_debt = self.market_value_debt / total_capital
        
        # WACC
        wacc = (weight_equity * cost_of_equity + 
                weight_debt * self.cost_of_debt * (1 - self.tax_rate))
        
        return wacc
    
    def build_projections(self):
        """Build financial projections"""
        # Initialize projection DataFrame
        years = list(range(1, self.projection_years + 1))
        
        # Revenue projections
        base_revenue = self.historical_revenue[-1]
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
        
        # Taxes
        taxes = [ebit * self.tax_rate if ebit > 0 else 0 for ebit in ebits]
        
        # NOPAT
        nopats = [ebit - tax for ebit, tax in zip(ebits, taxes)]
        
        # Add back D&A
        nopat_plus_da = [nopat + da for nopat, da in zip(nopats, da_values)]
        
        # CapEx
        capex = [rev * self.capex_pct_revenue for rev in revenues]
        
        # Change in NWC
        nwc_changes = []
        prev_nwc = self.historical_revenue[-1] * self.nwc_pct_revenue
        
        for rev in revenues:
            current_nwc = rev * self.nwc_pct_revenue
            nwc_changes.append(current_nwc - prev_nwc)
            prev_nwc = current_nwc
        
        # Free Cash Flow
        fcfs = [
            nopat_da - cx - nwc
            for nopat_da, cx, nwc in zip(nopat_plus_da, capex, nwc_changes)
        ]
        
        # Create DataFrame
        self.projections = pd.DataFrame({
            'Year': years,
            'Revenue': revenues,
            'Revenue_Growth': self.revenue_growth_rates,
            'EBITDA': ebitdas,
            'EBITDA_Margin': [e/r for e, r in zip(ebitdas, revenues)],
            'D&A': da_values,
            'EBIT': ebits,
            'EBIT_Margin': [e/r for e, r in zip(ebits, revenues)],
            'Taxes': taxes,
            'Tax_Rate': [t/ebit if ebit != 0 else 0 for t, ebit in zip(taxes, ebits)],
            'NOPAT': nopats,
            'Add_DA': da_values,
            'Less_CapEx': capex,
            'Less_NWC': nwc_changes,
            'FCF': fcfs
        })
        
        return self.projections
    
    def calculate_terminal_value_perpetuity(self, wacc):
        """Calculate terminal value using perpetuity growth method"""
        terminal_fcf = self.projections['FCF'].iloc[-1] * (1 + self.terminal_growth_rate)
        terminal_value = terminal_fcf / (wacc - self.terminal_growth_rate)
        return terminal_value
    
    def calculate_terminal_value_multiple(self):
        """Calculate terminal value using exit multiple method"""
        terminal_ebitda = self.projections['EBITDA'].iloc[-1]
        terminal_value = terminal_ebitda * self.terminal_ebitda_multiple
        return terminal_value
    
    def calculate_dcf(self, use_perpetuity=True):
        """
        Calculate enterprise value using DCF
        
        Parameters:
        -----------
        use_perpetuity : bool
            If True, use perpetuity growth method for terminal value
            If False, use exit multiple method
        """
        wacc = self.calculate_wacc()
        
        # Present value of projected FCFs
        pv_fcfs = []
        for year, fcf in enumerate(self.projections['FCF'], 1):
            pv = fcf / (1 + wacc) ** year
            pv_fcfs.append(pv)
        
        pv_projection_period = sum(pv_fcfs)
        
        # Terminal value
        if use_perpetuity:
            terminal_value = self.calculate_terminal_value_perpetuity(wacc)
        else:
            terminal_value = self.calculate_terminal_value_multiple()
        
        # PV of terminal value
        pv_terminal = terminal_value / (1 + wacc) ** self.projection_years
        
        # Enterprise value
        self.enterprise_value = pv_projection_period + pv_terminal
        
        return {
            'WACC': wacc,
            'PV_Projection_Period': pv_projection_period,
            'Terminal_Value': terminal_value,
            'PV_Terminal_Value': pv_terminal,
            'Enterprise_Value': self.enterprise_value
        }
    
    def calculate_equity_value(self, cash, debt, minority_interest=0, 
                              investments=0, shares_outstanding=1):
        """
        Calculate equity value and per-share value
        
        Equity Value = Enterprise Value + Cash - Debt - Minority Interest + Investments
        """
        self.equity_value = (self.enterprise_value + cash - debt - 
                            minority_interest + investments)
        self.equity_value_per_share = self.equity_value / shares_outstanding
        
        return {
            'Enterprise_Value': self.enterprise_value,
            'Cash': cash,
            'Debt': debt,
            'Minority_Interest': minority_interest,
            'Investments': investments,
            'Equity_Value': self.equity_value,
            'Shares_Outstanding': shares_outstanding,
            'Equity_Value_Per_Share': self.equity_value_per_share
        }
    
    def sensitivity_analysis(self, wacc_range, terminal_growth_range):
        """
        Perform sensitivity analysis on WACC and terminal growth rate
        
        Returns a DataFrame with equity values per share for different scenarios
        """
        results = []
        
        for wacc in wacc_range:
            row = []
            for tg in terminal_growth_range:
                # Temporarily set values
                original_wacc_assumptions = (
                    self.risk_free_rate, self.equity_risk_premium, 
                    self.beta, self.cost_of_debt
                )
                original_tg = self.terminal_growth_rate
                
                # Override WACC (simplified - just scale proportionally)
                wacc_ratio = wacc / self.calculate_wacc()
                self.risk_free_rate *= wacc_ratio
                
                self.terminal_growth_rate = tg
                
                # Recalculate
                self.calculate_dcf(use_perpetuity=True)
                
                row.append(self.equity_value_per_share)
                
                # Restore
                (self.risk_free_rate, self.equity_risk_premium, 
                 self.beta, self.cost_of_debt) = original_wacc_assumptions
                self.terminal_growth_rate = original_tg
            
            results.append(row)
        
        sensitivity_df = pd.DataFrame(
            results,
            index=[f"{w:.1%}" for w in wacc_range],
            columns=[f"{tg:.1%}" for tg in terminal_growth_range]
        )
        sensitivity_df.index.name = 'WACC'
        sensitivity_df.columns.name = 'Terminal Growth'
        
        return sensitivity_df
    
    def display_summary(self):
        """Display valuation summary"""
        wacc = self.calculate_wacc()
        
        print(f"\n{'='*70}")
        print(f"DCF VALUATION SUMMARY: {self.company_name} ({self.ticker})")
        print(f"{'='*70}")
        print(f"Valuation Date: {self.model_date.strftime('%B %d, %Y')}")
        
        print(f"\n{'WACC CALCULATION':-^70}")
        print(f"Risk-free Rate:        {self.risk_free_rate:>6.2%}")
        print(f"Equity Risk Premium:   {self.equity_risk_premium:>6.2%}")
        print(f"Beta:                  {self.beta:>6.2f}")
        print(f"Cost of Equity:        {self.risk_free_rate + self.beta * self.equity_risk_premium:>6.2%}")
        print(f"Cost of Debt:          {self.cost_of_debt:>6.2%}")
        print(f"After-tax Cost of Debt:{self.cost_of_debt * (1-self.tax_rate):>6.2%}")
        print(f"WACC:                  {wacc:>6.2%}")
        
        print(f"\n{'VALUATION RESULTS':-^70}")
        print(f"Enterprise Value:      ${self.enterprise_value:>12,.0f}M")
        print(f"Equity Value:          ${self.equity_value:>12,.0f}M")
        print(f"Equity Value/Share:    ${self.equity_value_per_share:>12,.2f}")
        
        print(f"\n{'='*70}\n")


# Example usage
def example_dcf_model():
    """Complete example of building a DCF model"""
    
    # Initialize model
    model = DCFModel("TechCo Inc.", "TECH")
    
    # Historical data (last 3 years)
    model.set_historical_data(
        years=[2022, 2023, 2024],
        revenue=[800, 920, 1050],
        ebitda=[160, 200, 250]
    )
    
    # Revenue assumptions (declining growth)
    model.set_revenue_assumptions(
        growth_rates=[0.18, 0.15, 0.12, 0.10, 0.08]
    )
    
    # Operating assumptions
    model.set_operating_assumptions(
        ebitda_margin=0.25,
        tax_rate=0.25,
        da_pct_revenue=0.03,
        capex_pct_revenue=0.04,
        nwc_pct_revenue=0.10
    )
    
    # WACC assumptions
    model.set_wacc_assumptions(
        risk_free_rate=0.04,
        equity_risk_premium=0.06,
        beta=1.2,
        cost_of_debt=0.05,
        mv_equity=5000,
        mv_debt=1000
    )
    
    # Terminal value assumptions
    model.set_terminal_assumptions(
        growth_rate=0.03,
        ebitda_multiple=12.0
    )
    
    # Build projections
    projections = model.build_projections()
    
    # Calculate DCF
    dcf_results = model.calculate_dcf(use_perpetuity=True)
    
    # Calculate equity value
    equity_results = model.calculate_equity_value(
        cash=200,
        debt=1000,
        minority_interest=0,
        investments=0,
        shares_outstanding=100
    )
    
    # Display results
    model.display_summary()
    
    # Show projections
    print("FINANCIAL PROJECTIONS")
    print("=" * 70)
    print(projections.to_string(index=False))
    
    return model

if __name__ == "__main__":
    model = example_dcf_model()
