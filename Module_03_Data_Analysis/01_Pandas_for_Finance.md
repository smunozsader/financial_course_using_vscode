# Module 3: Financial Data Analysis with Pandas

## Working with Financial Data in Python

### Introduction

Pandas is the most powerful library for financial data analysis in Python. It provides DataFrame objects that work like Excel tables but with vastly more capabilities.

### Why Pandas for Finance?

- **Time Series**: Built-in support for dates and financial calendars
- **Data Import**: Read Excel, CSV, databases, APIs
- **Data Cleaning**: Handle missing data, outliers
- **Calculations**: Easy financial ratios, returns, aggregations
- **Grouping**: Analyze by sector, time period, etc.
- **Speed**: Handles millions of rows efficiently

### Getting Started with Pandas

```python
import pandas as pd
import numpy as np
from datetime import datetime

# Creating a DataFrame - Like an Excel table
data = {
    'Company': ['Apple', 'Microsoft', 'Google', 'Amazon'],
    'Ticker': ['AAPL', 'MSFT', 'GOOGL', 'AMZN'],
    'Revenue': [394, 211, 307, 514],
    'EBITDA': [130, 107, 100, 66],
    'Market_Cap': [3000, 2800, 1800, 1600]
}

df = pd.DataFrame(data)
print(df)
```

### Essential Pandas Operations for Finance

#### 1. Calculating Financial Ratios

```python
# Add calculated columns
df['EBITDA_Margin'] = df['EBITDA'] / df['Revenue']
df['EV/Revenue'] = df['Market_Cap'] / df['Revenue']
df['EV/EBITDA'] = df['Market_Cap'] / df['EBITDA']

print(df[['Company', 'EBITDA_Margin', 'EV/EBITDA']])
```

#### 2. Working with Financial Statements

```python
# Income Statement as DataFrame
income_statement = pd.DataFrame({
    '2022': [1000, 600, 400, 100, 300, 75, 225],
    '2023': [1150, 660, 490, 110, 380, 95, 285],
    '2024': [1320, 720, 600, 120, 480, 120, 360]
}, index=[
    'Revenue',
    'COGS',
    'Gross Profit',
    'SG&A',
    'EBITDA',
    'D&A',
    'EBIT'
])

# Transpose for time series analysis
income_statement_T = income_statement.T
print(income_statement_T)

# Calculate margins
income_statement_T['Gross_Margin'] = (
    income_statement_T['Gross Profit'] / income_statement_T['Revenue']
)
income_statement_T['EBITDA_Margin'] = (
    income_statement_T['EBITDA'] / income_statement_T['Revenue']
)

print(income_statement_T[['Revenue', 'Gross_Margin', 'EBITDA_Margin']])
```

#### 3. Time Series Data

```python
# Create date range for financial periods
dates = pd.date_range(start='2020-01-01', end='2024-12-31', freq='Q')

# Quarterly revenue data
quarterly_revenue = pd.DataFrame({
    'Date': dates,
    'Revenue': np.random.randint(200, 400, len(dates))
})
quarterly_revenue.set_index('Date', inplace=True)

# Calculate growth rates
quarterly_revenue['QoQ_Growth'] = quarterly_revenue['Revenue'].pct_change()
quarterly_revenue['YoY_Growth'] = quarterly_revenue['Revenue'].pct_change(periods=4)

print(quarterly_revenue.tail(8))
```

#### 4. Loading Real Market Data

```python
import yfinance as yf

# Download stock data
ticker = 'AAPL'
stock_data = yf.download(ticker, start='2023-01-01', end='2024-12-31')

# Calculate returns
stock_data['Daily_Return'] = stock_data['Close'].pct_change()
stock_data['Cumulative_Return'] = (1 + stock_data['Daily_Return']).cumprod() - 1

# Calculate volatility (annualized)
volatility = stock_data['Daily_Return'].std() * np.sqrt(252)
print(f"{ticker} Annual Volatility: {volatility:.2%}")

# Moving averages
stock_data['MA_50'] = stock_data['Close'].rolling(window=50).mean()
stock_data['MA_200'] = stock_data['Close'].rolling(window=200).mean()
```

#### 5. Financial Statement Analysis

```python
def analyze_financials(revenue, cogs, opex, tax_rate=0.25):
    """
    Analyze financial statements and calculate key metrics
    
    Parameters:
    -----------
    revenue : pandas Series
        Revenue over time
    cogs : pandas Series  
        Cost of goods sold
    opex : pandas Series
        Operating expenses
    tax_rate : float
        Tax rate
    
    Returns:
    --------
    pandas DataFrame with financial metrics
    """
    analysis = pd.DataFrame()
    
    analysis['Revenue'] = revenue
    analysis['COGS'] = cogs
    analysis['Gross_Profit'] = revenue - cogs
    analysis['Gross_Margin'] = analysis['Gross_Profit'] / revenue
    
    analysis['OpEx'] = opex
    analysis['EBITDA'] = analysis['Gross_Profit'] - opex
    analysis['EBITDA_Margin'] = analysis['EBITDA'] / revenue
    
    # Assume D&A is 5% of revenue
    analysis['D&A'] = revenue * 0.05
    analysis['EBIT'] = analysis['EBITDA'] - analysis['D&A']
    
    # Taxes
    analysis['Taxes'] = analysis['EBIT'].apply(
        lambda x: x * tax_rate if x > 0 else 0
    )
    analysis['Net_Income'] = analysis['EBIT'] - analysis['Taxes']
    analysis['Net_Margin'] = analysis['Net_Income'] / revenue
    
    return analysis

# Example usage
years = pd.date_range('2020', '2024', freq='Y')
revenue = pd.Series([1000, 1150, 1320, 1520, 1750], index=years)
cogs = pd.Series([600, 660, 720, 820, 910], index=years)
opex = pd.Series([200, 220, 240, 260, 280], index=years)

financials = analyze_financials(revenue, cogs, opex)
print(financials)
```

#### 6. Comparable Company Analysis

```python
# Create comps table
comps = pd.DataFrame({
    'Company': ['Company A', 'Company B', 'Company C', 'Company D', 'Target'],
    'Revenue': [1500, 2200, 1800, 3000, 1600],
    'EBITDA': [300, 440, 360, 600, 320],
    'Market_Cap': [3000, 4800, 3800, 7200, np.nan]
})

# Calculate multiples
comps['EV/Revenue'] = comps['Market_Cap'] / comps['Revenue']
comps['EV/EBITDA'] = comps['Market_Cap'] / comps['EBITDA']

# Statistics (excluding target)
comp_stats = comps[comps['Company'] != 'Target'][['EV/Revenue', 'EV/EBITDA']].describe()
print("\nComparable Company Statistics:")
print(comp_stats)

# Value target company using median multiples
median_ev_revenue = comps[comps['Company'] != 'Target']['EV/Revenue'].median()
median_ev_ebitda = comps[comps['Company'] != 'Target']['EV/EBITDA'].median()

target_revenue = comps[comps['Company'] == 'Target']['Revenue'].values[0]
target_ebitda = comps[comps['Company'] == 'Target']['EBITDA'].values[0]

valuation_revenue = target_revenue * median_ev_revenue
valuation_ebitda = target_ebitda * median_ev_ebitda

print(f"\nTarget Valuation:")
print(f"  Using Revenue multiple: ${valuation_revenue:,.0f}M")
print(f"  Using EBITDA multiple: ${valuation_ebitda:,.0f}M")
print(f"  Average: ${(valuation_revenue + valuation_ebitda)/2:,.0f}M")
```

### Excel Integration

```python
# Read Excel file
df = pd.read_excel('financial_model.xlsx', sheet_name='Income Statement')

# Write to Excel
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    income_statement.to_excel(writer, sheet_name='Income Statement')
    balance_sheet.to_excel(writer, sheet_name='Balance Sheet')
    cash_flow.to_excel(writer, sheet_name='Cash Flow')
```

### Practice Exercises

#### Exercise 1: Historical Analysis
Download 5 years of financial data for a public company and:
1. Calculate revenue CAGR
2. Plot revenue and EBITDA trends
3. Calculate average margins
4. Identify trends

#### Exercise 2: Comps Analysis
Build a comparable company analysis:
1. Find 5-10 comparable companies
2. Calculate trading multiples
3. Create summary statistics
4. Value your target company

#### Exercise 3: Returns Analysis
Analyze stock returns:
1. Download historical prices
2. Calculate daily, monthly, annual returns
3. Calculate volatility and Sharpe ratio
4. Plot cumulative returns

### Solutions

See `Module_03_Data_Analysis/solutions.py`

### Key Takeaways

✅ **DataFrames**: The foundation of financial analysis in Python
✅ **Time Series**: Built-in support for dates and periods
✅ **Calculations**: Easy to calculate ratios, growth rates, returns
✅ **Grouping**: Analyze by categories (sector, region, etc.)
✅ **Excel Integration**: Read and write Excel files
✅ **Real Data**: Access market data via APIs (yfinance, etc.)

### Next Steps

Continue to: `Module_04_DCF_Modeling/01_DCF_Overview.md`

---

**Estimated Time**: 3-4 hours
**Prerequisites**: Module 2 (Python Fundamentals)
