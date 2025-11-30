"""
Solutions to Module 03 Practice Exercises

Complete solutions with detailed explanations and expected outputs.
Study these after attempting the exercises yourself!
"""

import pandas as pd
import numpy as np
import yfinance as yf


# =============================================================================
# EXERCISE 1: Historical Revenue Analysis
# =============================================================================

def exercise_1_revenue_analysis():
    """
    Build a complete quarterly revenue analysis with growth metrics.
    
    This demonstrates:
    - Time series data creation
    - Growth rate calculations (QoQ, YoY)
    - CAGR calculation
    - Seasonality analysis
    """
    print("\n" + "="*80)
    print("EXERCISE 1: HISTORICAL REVENUE ANALYSIS")
    print("="*80)
    
    # Create quarterly dates
    quarters = pd.date_range('2020-01-01', periods=20, freq='Q')
    
    # Create realistic quarterly revenue with growth
    # Starting at $100M, growing 5-8% per quarter
    np.random.seed(42)  # For reproducibility
    growth_rates = np.random.uniform(0.05, 0.08, 20)
    
    revenue = [100.0]  # Start at $100M
    for i in range(1, 20):
        revenue.append(revenue[-1] * (1 + growth_rates[i]))
    
    # Create DataFrame
    df = pd.DataFrame({
        'Quarter': quarters,
        'Revenue': revenue
    })
    df.set_index('Quarter', inplace=True)
    
    # Calculate QoQ growth
    df['QoQ_Growth_%'] = df['Revenue'].pct_change() * 100
    
    # Calculate YoY growth (4 quarters ago)
    df['YoY_Growth_%'] = df['Revenue'].pct_change(periods=4) * 100
    
    # Add quarter labels for seasonality
    df['Quarter_Label'] = df.index.to_period('Q').astype(str).str[-2:]
    
    print("\nQuarterly Revenue Data:")
    print(df)
    
    # Calculate CAGR
    # CAGR = (Ending Value / Beginning Value)^(1/years) - 1
    years = 5
    cagr = ((df['Revenue'].iloc[-1] / df['Revenue'].iloc[0]) ** (1/years) - 1) * 100
    print(f"\n5-Year Revenue CAGR: {cagr:.2f}%")
    
    # Best and worst quarters
    best_quarter = df['QoQ_Growth_%'].idxmax()
    worst_quarter = df['QoQ_Growth_%'].idxmin()
    
    print(f"\nBest Quarter (QoQ Growth):  {best_quarter} at {df.loc[best_quarter, 'QoQ_Growth_%']:.2f}%")
    print(f"Worst Quarter (QoQ Growth): {worst_quarter} at {df.loc[worst_quarter, 'QoQ_Growth_%']:.2f}%")
    
    # Seasonality analysis
    print("\nSeasonality Analysis (Average Revenue by Quarter):")
    seasonality = df.groupby('Quarter_Label')['Revenue'].mean()
    print(seasonality)
    
    return df


# =============================================================================
# EXERCISE 2: Tech Comps Table
# =============================================================================

def exercise_2_comps_analysis():
    """
    Build a professional comparable company analysis with valuation.
    
    This demonstrates:
    - Comp table construction
    - Multiple calculations
    - Statistical analysis
    - Valuation using multiples
    """
    print("\n" + "="*80)
    print("EXERCISE 2: TECH COMPS TABLE")
    print("="*80)
    
    # Create comp table with realistic SaaS metrics
    comps = pd.DataFrame({
        'Company': ['SaaS Leader A', 'Cloud Co B', 'Platform C', 'Enterprise D', 'Growth Co E', 'Target Co'],
        'Revenue': [2500, 1800, 3200, 4000, 1200, 2000],
        'EBITDA': [500, 360, 640, 800, 240, 400],
        'Market_Cap': [7500, 5000, 10000, 12000, 3500, np.nan],  # Target unknown
        'Net_Debt': [300, 200, 500, 600, 100, 250],
        'Growth_%': [28, 35, 22, 18, 45, 30]
    })
    
    # Calculate Enterprise Value
    comps['Enterprise_Value'] = comps['Market_Cap'] + comps['Net_Debt']
    
    # Calculate multiples
    comps['EV/Revenue'] = comps['Enterprise_Value'] / comps['Revenue']
    comps['EV/EBITDA'] = comps['Enterprise_Value'] / comps['EBITDA']
    comps['EBITDA_Margin_%'] = (comps['EBITDA'] / comps['Revenue']) * 100
    
    print("\nFull Comp Table:")
    print(comps.round(2))
    
    # Statistics (excluding target)
    is_comp = comps['Company'] != 'Target Co'
    
    print("\n" + "-"*80)
    print("COMPARABLE COMPANY STATISTICS (Excluding Target):")
    print("-"*80)
    
    stats = comps[is_comp][['EV/Revenue', 'EV/EBITDA', 'EBITDA_Margin_%', 'Growth_%']].describe()
    print(stats.round(2))
    
    # Get median multiples for valuation
    median_ev_revenue = comps[is_comp]['EV/Revenue'].median()
    median_ev_ebitda = comps[is_comp]['EV/EBITDA'].median()
    
    print("\n" + "-"*80)
    print("VALUATION MULTIPLES:")
    print("-"*80)
    print(f"Median EV/Revenue: {median_ev_revenue:.2f}x")
    print(f"Median EV/EBITDA:  {median_ev_ebitda:.2f}x")
    
    # Value target company
    target_revenue = comps[comps['Company'] == 'Target Co']['Revenue'].values[0]
    target_ebitda = comps[comps['Company'] == 'Target Co']['EBITDA'].values[0]
    target_net_debt = comps[comps['Company'] == 'Target Co']['Net_Debt'].values[0]
    
    ev_from_revenue = target_revenue * median_ev_revenue
    ev_from_ebitda = target_ebitda * median_ev_ebitda
    avg_ev = (ev_from_revenue + ev_from_ebitda) / 2
    
    # Calculate equity values
    equity_from_revenue = ev_from_revenue - target_net_debt
    equity_from_ebitda = ev_from_ebitda - target_net_debt
    avg_equity = avg_ev - target_net_debt
    
    print("\n" + "-"*80)
    print("TARGET COMPANY VALUATION:")
    print("-"*80)
    print(f"Target Revenue:     ${target_revenue:,.0f}M")
    print(f"Target EBITDA:      ${target_ebitda:,.0f}M")
    print(f"Target Net Debt:    ${target_net_debt:,.0f}M")
    print()
    print("Enterprise Value Estimates:")
    print(f"  Using Revenue multiple: ${ev_from_revenue:,.0f}M ({median_ev_revenue:.2f}x)")
    print(f"  Using EBITDA multiple:  ${ev_from_ebitda:,.0f}M ({median_ev_ebitda:.2f}x)")
    print(f"  Average:                ${avg_ev:,.0f}M")
    print()
    print("Equity Value Estimates:")
    print(f"  Using Revenue multiple: ${equity_from_revenue:,.0f}M")
    print(f"  Using EBITDA multiple:  ${equity_from_ebitda:,.0f}M")
    print(f"  Average:                ${avg_equity:,.0f}M")
    
    # BONUS: Premium/Discount analysis
    print("\n" + "-"*80)
    print("BONUS: Premium/Discount to Median Multiple:")
    print("-"*80)
    
    comps_only = comps[is_comp].copy()
    comps_only['Premium_Discount_%'] = ((comps_only['EV/EBITDA'] / median_ev_ebitda) - 1) * 100
    
    print(comps_only[['Company', 'EV/EBITDA', 'Premium_Discount_%']].sort_values('EV/EBITDA', ascending=False))
    
    return comps


# =============================================================================
# EXERCISE 3: Stock Returns and Risk Analysis
# =============================================================================

def exercise_3_stock_analysis(ticker='AAPL', start_date='2022-01-01', end_date='2024-12-31'):
    """
    Download and analyze real stock data with risk metrics.
    
    Parameters:
    -----------
    ticker : str
        Stock ticker symbol (default: AAPL)
    start_date : str
        Start date for analysis
    end_date : str
        End date for analysis
    
    This demonstrates:
    - Real market data download
    - Returns calculations
    - Risk metrics (volatility, Sharpe ratio)
    - Performance analysis
    """
    print("\n" + "="*80)
    print(f"EXERCISE 3: STOCK RETURNS ANALYSIS - {ticker}")
    print("="*80)
    
    print(f"\nDownloading {ticker} data from {start_date} to {end_date}...")
    
    # Download stock data
    stock = yf.download(ticker, start=start_date, end=end_date, progress=False)
    
    print(f"✅ Downloaded {len(stock)} trading days\n")
    
    # Calculate returns
    stock['Daily_Return_%'] = stock['Close'].pct_change() * 100
    stock['Cumulative_Return_%'] = ((1 + stock['Close'].pct_change()).cumprod() - 1) * 100
    
    # Calculate volatility (annualized)
    daily_vol = stock['Daily_Return_%'].std()
    annual_vol = daily_vol * np.sqrt(252)
    
    # Calculate Sharpe Ratio (assuming risk-free rate = 0)
    mean_daily_return = stock['Daily_Return_%'].mean()
    sharpe_ratio = (mean_daily_return * 252) / (daily_vol * np.sqrt(252))
    
    print("-"*80)
    print("RETURN METRICS:")
    print("-"*80)
    print(f"Average Daily Return:    {mean_daily_return:.3f}%")
    print(f"Total Return (Period):   {stock['Cumulative_Return_%'].iloc[-1]:.2f}%")
    print(f"Annualized Volatility:   {annual_vol:.2f}%")
    print(f"Sharpe Ratio:            {sharpe_ratio:.2f}")
    
    # Best and worst days
    print("\n" + "-"*80)
    print("TOP 5 BEST TRADING DAYS:")
    print("-"*80)
    best_days = stock.nlargest(5, 'Daily_Return_%')[['Close', 'Daily_Return_%']]
    for date, row in best_days.iterrows():
        print(f"{date.strftime('%Y-%m-%d')}: +{row['Daily_Return_%']:.2f}%  (Close: ${row['Close']:.2f})")
    
    print("\n" + "-"*80)
    print("TOP 5 WORST TRADING DAYS:")
    print("-"*80)
    worst_days = stock.nsmallest(5, 'Daily_Return_%')[['Close', 'Daily_Return_%']]
    for date, row in worst_days.iterrows():
        print(f"{date.strftime('%Y-%m-%d')}: {row['Daily_Return_%']:.2f}%  (Close: ${row['Close']:.2f})")
    
    # Monthly returns
    print("\n" + "-"*80)
    print("MONTHLY RETURNS:")
    print("-"*80)
    monthly_returns = stock['Close'].resample('M').last().pct_change() * 100
    print(monthly_returns.tail(12))
    
    # Maximum drawdown
    cumulative = (1 + stock['Close'].pct_change()).cumprod()
    running_max = cumulative.cummax()
    drawdown = ((cumulative - running_max) / running_max) * 100
    max_drawdown = drawdown.min()
    max_dd_date = drawdown.idxmin()
    
    print("\n" + "-"*80)
    print("RISK METRICS:")
    print("-"*80)
    print(f"Maximum Drawdown:        {max_drawdown:.2f}%")
    print(f"Max Drawdown Date:       {max_dd_date.strftime('%Y-%m-%d')}")
    
    # BONUS: Compare with S&P 500
    print("\n" + "-"*80)
    print("BONUS: COMPARISON WITH S&P 500:")
    print("-"*80)
    
    sp500 = yf.download('^GSPC', start=start_date, end=end_date, progress=False)
    sp500_return = ((sp500['Close'].iloc[-1] / sp500['Close'].iloc[0]) - 1) * 100
    stock_return = ((stock['Close'].iloc[-1] / stock['Close'].iloc[0]) - 1) * 100
    
    print(f"{ticker} Total Return:  {stock_return:.2f}%")
    print(f"S&P 500 Total Return:    {sp500_return:.2f}%")
    print(f"Outperformance:          {stock_return - sp500_return:+.2f}%")
    
    # Correlation
    combined = pd.DataFrame({
        ticker: stock['Close'].pct_change(),
        'SP500': sp500['Close'].pct_change()
    }).dropna()
    
    correlation = combined[ticker].corr(combined['SP500'])
    print(f"Correlation with S&P 500: {correlation:.3f}")
    
    return stock


# =============================================================================
# EXERCISE 4: Excel Model Integration
# =============================================================================

def exercise_4_excel_integration():
    """
    Build a complete 3-statement financial model and export to Excel.
    
    This demonstrates:
    - Multi-statement modeling
    - Financial metrics calculation
    - Excel integration with multiple sheets
    - Data verification
    """
    print("\n" + "="*80)
    print("EXERCISE 4: EXCEL MODEL INTEGRATION")
    print("="*80)
    
    years = ['2020', '2021', '2022', '2023', '2024']
    
    # INCOME STATEMENT
    print("\nBuilding Income Statement...")
    
    revenue = [1000, 1150, 1323, 1521, 1749]  # 15% growth
    cogs = [600, 690, 794, 913, 1049]  # 60% of revenue
    gross_profit = [r - c for r, c in zip(revenue, cogs)]
    opex = [200, 230, 265, 304, 350]  # 20% of revenue
    ebitda = [gp - op for gp, op in zip(gross_profit, opex)]
    
    income_statement = pd.DataFrame({
        '2020': [revenue[0], cogs[0], gross_profit[0], opex[0], ebitda[0]],
        '2021': [revenue[1], cogs[1], gross_profit[1], opex[1], ebitda[1]],
        '2022': [revenue[2], cogs[2], gross_profit[2], opex[2], ebitda[2]],
        '2023': [revenue[3], cogs[3], gross_profit[3], opex[3], ebitda[3]],
        '2024': [revenue[4], cogs[4], gross_profit[4], opex[4], ebitda[4]]
    }, index=['Revenue', 'COGS', 'Gross Profit', 'Operating Expenses', 'EBITDA'])
    
    print(income_statement)
    
    # BALANCE SHEET
    print("\nBuilding Balance Sheet...")
    
    balance_sheet = pd.DataFrame({
        '2020': [3000, 1800, 1200],
        '2021': [3450, 1950, 1500],
        '2022': [3968, 2100, 1868],
        '2023': [4563, 2250, 2313],
        '2024': [5247, 2400, 2847]
    }, index=['Total Assets', 'Total Liabilities', 'Total Equity'])
    
    print(balance_sheet)
    
    # CASH FLOW STATEMENT
    print("\nBuilding Cash Flow Statement...")
    
    operating_cf = [eb * 0.8 for eb in ebitda]  # 80% of EBITDA
    investing_cf = [-r * 0.1 for r in revenue]  # -10% of revenue (capex)
    financing_cf = [-50, -60, -70, -80, -90]  # Debt paydown
    
    cash_flow = pd.DataFrame({
        '2020': [operating_cf[0], investing_cf[0], financing_cf[0]],
        '2021': [operating_cf[1], investing_cf[1], financing_cf[1]],
        '2022': [operating_cf[2], investing_cf[2], financing_cf[2]],
        '2023': [operating_cf[3], investing_cf[3], financing_cf[3]],
        '2024': [operating_cf[4], investing_cf[4], financing_cf[4]]
    }, index=['Operating Cash Flow', 'Investing Cash Flow', 'Financing Cash Flow'])
    
    print(cash_flow)
    
    # KEY METRICS
    print("\nCalculating Key Metrics...")
    
    # Calculate metrics
    gross_margin = (income_statement.loc['Gross Profit'] / income_statement.loc['Revenue']) * 100
    ebitda_margin = (income_statement.loc['EBITDA'] / income_statement.loc['Revenue']) * 100
    
    # Simplified ROE (EBITDA / Equity as proxy)
    roe = (income_statement.loc['EBITDA'] / balance_sheet.loc['Total Equity']) * 100
    
    # Net Debt / EBITDA (assuming some debt)
    net_debt = [500, 450, 400, 350, 300]  # Declining debt
    net_debt_ebitda = [nd / eb for nd, eb in zip(net_debt, ebitda)]
    
    key_metrics = pd.DataFrame({
        '2020': [gross_margin['2020'], ebitda_margin['2020'], roe['2020'], net_debt_ebitda[0]],
        '2021': [gross_margin['2021'], ebitda_margin['2021'], roe['2021'], net_debt_ebitda[1]],
        '2022': [gross_margin['2022'], ebitda_margin['2022'], roe['2022'], net_debt_ebitda[2]],
        '2023': [gross_margin['2023'], ebitda_margin['2023'], roe['2023'], net_debt_ebitda[3]],
        '2024': [gross_margin['2024'], ebitda_margin['2024'], roe['2024'], net_debt_ebitda[4]]
    }, index=['Gross Margin %', 'EBITDA Margin %', 'ROE %', 'Net Debt / EBITDA'])
    
    print(key_metrics.round(2))
    
    # WRITE TO EXCEL
    output_file = 'complete_financial_model.xlsx'
    
    print(f"\n✍️  Writing to Excel: {output_file}")
    
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        income_statement.to_excel(writer, sheet_name='Income Statement')
        balance_sheet.to_excel(writer, sheet_name='Balance Sheet')
        cash_flow.to_excel(writer, sheet_name='Cash Flow')
        key_metrics.to_excel(writer, sheet_name='Key Metrics')
    
    print(f"✅ Successfully created {output_file}")
    
    # READ BACK AND VERIFY
    print(f"\n🔍 Reading back from Excel to verify...")
    
    df_income = pd.read_excel(output_file, sheet_name='Income Statement', index_col=0)
    df_balance = pd.read_excel(output_file, sheet_name='Balance Sheet', index_col=0)
    df_cashflow = pd.read_excel(output_file, sheet_name='Cash Flow', index_col=0)
    df_metrics = pd.read_excel(output_file, sheet_name='Key Metrics', index_col=0)
    
    print("\nVerification:")
    print(f"  Income Statement: {df_income.shape[0]} rows × {df_income.shape[1]} columns ✅")
    print(f"  Balance Sheet:    {df_balance.shape[0]} rows × {df_balance.shape[1]} columns ✅")
    print(f"  Cash Flow:        {df_cashflow.shape[0]} rows × {df_cashflow.shape[1]} columns ✅")
    print(f"  Key Metrics:      {df_metrics.shape[0]} rows × {df_metrics.shape[1]} columns ✅")
    
    print("\n✅ All sheets verified successfully!")
    print(f"\n📁 Open '{output_file}' in Excel to see your financial model!")
    
    return {
        'income_statement': income_statement,
        'balance_sheet': balance_sheet,
        'cash_flow': cash_flow,
        'key_metrics': key_metrics
    }


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "█"*80)
    print("MODULE 03 - SOLUTIONS TO PRACTICE EXERCISES")
    print("█"*80)
    print("\nThese are complete solutions to all Module 03 exercises.")
    print("Study the code and output to understand Pandas for financial analysis!\n")
    
    # Exercise 1
    df_revenue = exercise_1_revenue_analysis()
    
    # Exercise 2
    df_comps = exercise_2_comps_analysis()
    
    # Exercise 3
    df_stock = exercise_3_stock_analysis(ticker='AAPL')
    
    # Exercise 4
    financial_model = exercise_4_excel_integration()
    
    print("\n" + "█"*80)
    print("ALL EXERCISES COMPLETED!")
    print("█"*80)
    print("\n✅ Exercise 1: Revenue Analysis - DONE")
    print("✅ Exercise 2: Comps Table - DONE")
    print("✅ Exercise 3: Stock Analysis - DONE")
    print("✅ Exercise 4: Excel Integration - DONE")
    print("\n🎉 Congratulations! You've mastered Pandas for Financial Analysis!")
    print("\n📚 Next up: Module 04 - DCF Modeling")
    print("█"*80 + "\n")
