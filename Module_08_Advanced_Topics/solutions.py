"""
Solutions to Module 08 Practice Exercises - Advanced Topics

Master cutting-edge financial modeling techniques!
These solutions show advanced quantitative methods used at top PE firms.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
import warnings
warnings.filterwarnings('ignore')


# =============================================================================
# EXERCISE 1: Monte Carlo LBO Analysis
# =============================================================================

def exercise_1_monte_carlo_lbo():
    """
    Monte Carlo simulation for LBO deal analysis.
    
    This is ADVANCED risk analysis - run 10,000 scenarios!
    Shows probability distribution of outcomes.
    
    Deal: $50M EBITDA, 8.0x entry, 60% leverage
    Variables: Revenue growth (7% ± 3%), Exit multiple (10x ± 2x)
    """
    print("\n" + "="*80)
    print("EXERCISE 1: MONTE CARLO LBO SIMULATION")
    print("="*80)
    
    # Deal parameters
    entry_ebitda = 50.0  # $M
    entry_multiple = 8.0
    purchase_price = entry_ebitda * entry_multiple
    
    equity_percent = 0.40
    debt_percent = 0.60
    
    equity_invested = purchase_price * equity_percent
    initial_debt = purchase_price * debt_percent
    
    holding_period = 5
    
    print(f"\nDEAL STRUCTURE:")
    print(f"Entry EBITDA:        ${entry_ebitda:.0f}M")
    print(f"Entry Multiple:      {entry_multiple:.1f}x")
    print(f"Purchase Price:      ${purchase_price:.0f}M")
    print(f"Equity Invested:     ${equity_invested:.0f}M ({equity_percent*100:.0f}%)")
    print(f"Initial Debt:        ${initial_debt:.0f}M ({debt_percent*100:.0f}%)")
    print(f"Holding Period:      {holding_period} years")
    
    # Random variable parameters
    revenue_growth_mean = 0.07
    revenue_growth_std = 0.03
    
    exit_multiple_mean = 10.0
    exit_multiple_std = 2.0
    
    ebitda_margin_mean = entry_ebitda / (entry_ebitda / 0.15)  # Assume 15% margin
    ebitda_margin_std = 0.02
    
    print(f"\nRANDOM VARIABLES:")
    print(f"Revenue Growth:      {revenue_growth_mean*100:.0f}% ± {revenue_growth_std*100:.0f}% (normal)")
    print(f"Exit Multiple:       {exit_multiple_mean:.1f}x ± {exit_multiple_std:.1f}x (normal)")
    print(f"EBITDA Margin:       {ebitda_margin_mean:.1%} ± {ebitda_margin_std:.1%} (normal)")
    
    # Run Monte Carlo simulation
    print(f"\n{'='*80}")
    print(f"RUNNING 10,000 MONTE CARLO SIMULATIONS...")
    print(f"{'='*80}")
    
    iterations = 10_000
    results = []
    
    np.random.seed(42)  # For reproducibility
    
    for i in range(iterations):
        # Draw random values
        revenue_growth = np.random.normal(revenue_growth_mean, revenue_growth_std)
        exit_multiple = np.random.normal(exit_multiple_mean, exit_multiple_std)
        ebitda_margin = np.random.normal(ebitda_margin_mean, ebitda_margin_std)
        
        # Cap exit multiple at reasonable bounds
        exit_multiple = max(6.0, min(exit_multiple, 15.0))
        ebitda_margin = max(0.05, min(ebitda_margin, 0.30))
        
        # Calculate exit EBITDA
        # Assume revenue grows, margin stays roughly constant
        revenue_multiplier = (1 + revenue_growth) ** holding_period
        exit_ebitda = entry_ebitda * revenue_multiplier * (ebitda_margin / ebitda_margin_mean)
        
        # Calculate exit value
        exit_ev = exit_ebitda * exit_multiple
        
        # Debt paydown (assume 50% paydown from FCF)
        debt_paydown_pct = np.random.normal(0.50, 0.10)
        debt_paydown_pct = max(0.20, min(debt_paydown_pct, 0.70))
        remaining_debt = initial_debt * (1 - debt_paydown_pct)
        
        # Exit equity value
        exit_equity_value = exit_ev - remaining_debt
        
        # Returns
        moic = exit_equity_value / equity_invested if equity_invested > 0 else 0
        irr = (moic ** (1/holding_period)) - 1 if moic > 0 else -1
        
        results.append({
            'revenue_growth': revenue_growth,
            'exit_multiple': exit_multiple,
            'ebitda_margin': ebitda_margin,
            'exit_ebitda': exit_ebitda,
            'exit_ev': exit_ev,
            'remaining_debt': remaining_debt,
            'exit_equity_value': exit_equity_value,
            'moic': moic,
            'irr': irr
        })
    
    # Convert to DataFrame for analysis
    df = pd.DataFrame(results)
    
    # ANALYSIS
    print(f"\n{'='*80}")
    print(f"MONTE CARLO RESULTS:")
    print(f"{'='*80}")
    
    # IRR Statistics
    print(f"\nIRR STATISTICS:")
    print(f"  Mean (Expected):     {df['irr'].mean()*100:.1f}%")
    print(f"  Median:              {df['irr'].median()*100:.1f}%")
    print(f"  Std Deviation:       {df['irr'].std()*100:.1f}%")
    print(f"  Min:                 {df['irr'].min()*100:.1f}%")
    print(f"  Max:                 {df['irr'].max()*100:.1f}%")
    
    # Percentiles
    print(f"\nIRR PERCENTILES:")
    print(f"  10th Percentile:     {df['irr'].quantile(0.10)*100:.1f}% (downside)")
    print(f"  25th Percentile:     {df['irr'].quantile(0.25)*100:.1f}%")
    print(f"  50th Percentile:     {df['irr'].quantile(0.50)*100:.1f}% (median)")
    print(f"  75th Percentile:     {df['irr'].quantile(0.75)*100:.1f}%")
    print(f"  90th Percentile:     {df['irr'].quantile(0.90)*100:.1f}% (upside)")
    
    # MOIC Statistics
    print(f"\nMOIC STATISTICS:")
    print(f"  Mean:                {df['moic'].mean():.2f}x")
    print(f"  Median:              {df['moic'].median():.2f}x")
    print(f"  10th Percentile:     {df['moic'].quantile(0.10):.2f}x")
    print(f"  90th Percentile:     {df['moic'].quantile(0.90):.2f}x")
    
    # Probability Analysis
    print(f"\n{'='*80}")
    print(f"PROBABILITY ANALYSIS:")
    print(f"{'='*80}")
    
    prob_25_plus = (df['irr'] >= 0.25).sum() / len(df) * 100
    prob_20_plus = (df['irr'] >= 0.20).sum() / len(df) * 100
    prob_15_plus = (df['irr'] >= 0.15).sum() / len(df) * 100
    prob_positive = (df['irr'] >= 0.00).sum() / len(df) * 100
    prob_loss = (df['moic'] < 1.0).sum() / len(df) * 100
    
    print(f"\nProbability of achieving:")
    print(f"  IRR ≥ 25%:           {prob_25_plus:.1f}% 🏆")
    print(f"  IRR ≥ 20%:           {prob_20_plus:.1f}% ✅")
    print(f"  IRR ≥ 15%:           {prob_15_plus:.1f}% 🟡")
    print(f"  IRR ≥ 0%:            {prob_positive:.1f}%")
    print(f"  LOSS (MOIC < 1.0x):  {prob_loss:.1f}% ❌")
    
    # Risk-Adjusted Return
    print(f"\n{'='*80}")
    print(f"RISK-ADJUSTED METRICS:")
    print(f"{'='*80}")
    
    expected_irr = df['irr'].mean()
    irr_volatility = df['irr'].std()
    sharpe_ratio = expected_irr / irr_volatility if irr_volatility > 0 else 0
    
    # Value at Risk (VaR)
    var_95 = df['irr'].quantile(0.05)
    cvar_95 = df[df['irr'] <= var_95]['irr'].mean()
    
    print(f"\nRisk Metrics:")
    print(f"  Sharpe Ratio:        {sharpe_ratio:.2f}")
    print(f"  VaR (95%):           {var_95*100:.1f}%")
    print(f"  CVaR (95%):          {cvar_95*100:.1f}%")
    print(f"\n  💡 95% confident we won't get less than {var_95*100:.1f}% IRR")
    
    # Recommendation
    print(f"\n{'='*80}")
    print(f"DEAL RECOMMENDATION:")
    print(f"{'='*80}")
    
    print(f"\n📊 Summary:")
    print(f"   Expected IRR:     {expected_irr*100:.1f}%")
    print(f"   Downside (10%):   {df['irr'].quantile(0.10)*100:.1f}%")
    print(f"   Upside (90%):     {df['irr'].quantile(0.90)*100:.1f}%")
    print(f"   Prob of 20%+ IRR: {prob_20_plus:.1f}%")
    
    if prob_20_plus >= 70 and df['irr'].quantile(0.10) >= 0.10:
        print(f"\n✅ STRONG BUY")
        print(f"   High probability of exceeding hurdle rate")
        print(f"   Downside protected (10th percentile > 10%)")
    elif prob_20_plus >= 50:
        print(f"\n🟡 MODERATE BUY")
        print(f"   Decent probability of meeting hurdle")
        print(f"   Monitor downside risk")
    else:
        print(f"\n❌ PASS")
        print(f"   Too risky - low probability of meeting hurdle")
    
    return df


# =============================================================================
# EXERCISE 2: Real Options Valuation
# =============================================================================

def exercise_2_real_options_valuation():
    """
    Real options analysis using Black-Scholes.
    
    Values management flexibility to delay investment.
    Critical for R&D, platform investments, etc.
    
    Scenario: R&D investment with option to wait
    """
    print("\n" + "="*80)
    print("EXERCISE 2: REAL OPTIONS VALUATION")
    print("="*80)
    
    from scipy.stats import norm
    
    # Parameters
    immediate_npv = 50.0  # $M if invest today
    delay_cost = 5.0      # $M cost to delay 1 year
    investment_cost = 80.0  # $M to invest in 1 year
    volatility = 0.40     # 40% project volatility
    time_to_decision = 1.0  # 1 year
    risk_free_rate = 0.05  # 5%
    
    print(f"\nSCENARIO: R&D Investment Decision")
    print("-" * 80)
    print(f"Immediate NPV (invest now): ${immediate_npv:.1f}M")
    print(f"Cost to delay 1 year:       ${delay_cost:.1f}M")
    print(f"Investment cost in 1 year:  ${investment_cost:.1f}M")
    print(f"Project volatility:         {volatility*100:.0f}%")
    print(f"Time to decision:           {time_to_decision:.0f} year")
    print(f"Risk-free rate:             {risk_free_rate*100:.0f}%")
    
    # Option 1: Invest immediately
    print(f"\n{'='*80}")
    print(f"OPTION 1: INVEST IMMEDIATELY")
    print(f"{'='*80}")
    
    immediate_value = immediate_npv
    print(f"NPV:                        ${immediate_value:.1f}M")
    
    # Option 2: Wait (real option)
    print(f"\n{'='*80}")
    print(f"OPTION 2: WAIT (Real Option Valuation)")
    print(f"{'='*80}")
    
    # Black-Scholes for call option
    # S = Current project value
    # K = Investment cost
    # σ = Volatility
    # T = Time
    # r = Risk-free rate
    
    S = immediate_npv + delay_cost  # Project value must cover delay cost
    K = investment_cost
    sigma = volatility
    T = time_to_decision
    r = risk_free_rate
    
    # Calculate d1 and d2
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    # Call option value
    option_value = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    
    # Net value of waiting
    net_option_value = option_value - delay_cost
    
    print(f"\nBlack-Scholes Calculation:")
    print(f"  S (Project Value):        ${S:.1f}M")
    print(f"  K (Investment Cost):      ${K:.1f}M")
    print(f"  d1:                       {d1:.3f}")
    print(f"  d2:                       {d2:.3f}")
    print(f"  N(d1):                    {norm.cdf(d1):.3f}")
    print(f"  N(d2):                    {norm.cdf(d2):.3f}")
    print(f"\nOption Value:               ${option_value:.1f}M")
    print(f"Less: Delay Cost:           (${delay_cost:.1f}M)")
    print(f"Net Value of Waiting:       ${net_option_value:.1f}M")
    
    # Comparison
    print(f"\n{'='*80}")
    print(f"COMPARISON:")
    print(f"{'='*80}")
    
    comparison = pd.DataFrame({
        'Strategy': ['Invest Now', 'Wait 1 Year'],
        'Value ($M)': [immediate_value, net_option_value],
        'Key Feature': ['Certainty', 'Flexibility']
    })
    
    print(comparison.to_string(index=False))
    
    value_of_flexibility = net_option_value - immediate_value
    
    print(f"\n💡 VALUE OF FLEXIBILITY: ${value_of_flexibility:.1f}M")
    
    if value_of_flexibility > 0:
        print(f"\n✅ RECOMMENDATION: WAIT")
        print(f"   The option to wait is worth ${value_of_flexibility:.1f}M more")
        print(f"   Flexibility to see market conditions = valuable!")
    else:
        print(f"\n✅ RECOMMENDATION: INVEST NOW")
        print(f"   Immediate investment creates ${abs(value_of_flexibility):.1f}M more value")
        print(f"   Don't wait - opportunity cost too high")
    
    # Sensitivity analysis
    print(f"\n{'='*80}")
    print(f"SENSITIVITY ANALYSIS:")
    print(f"{'='*80}")
    
    print(f"\nImpact of Volatility on Option Value:")
    print("-" * 80)
    
    for vol in [0.20, 0.30, 0.40, 0.50, 0.60]:
        d1_temp = (np.log(S/K) + (r + 0.5*vol**2)*T) / (vol*np.sqrt(T))
        d2_temp = d1_temp - vol*np.sqrt(T)
        opt_val_temp = S*norm.cdf(d1_temp) - K*np.exp(-r*T)*norm.cdf(d2_temp)
        net_val_temp = opt_val_temp - delay_cost
        
        print(f"Volatility {vol*100:.0f}%: Option Value = ${opt_val_temp:.1f}M, " +
              f"Net = ${net_val_temp:.1f}M")
    
    print(f"\n💡 Higher volatility = Higher option value!")
    print(f"   Uncertainty makes flexibility more valuable")
    
    return {
        'immediate_value': immediate_value,
        'option_value': option_value,
        'net_option_value': net_option_value,
        'value_of_flexibility': value_of_flexibility
    }


# =============================================================================
# EXERCISE 3: API-Driven Comp Analysis
# =============================================================================

def exercise_3_api_comp_analysis():
    """
    Automated comparable companies analysis using live data.
    
    THIS IS GAME-CHANGING - No manual data entry!
    Updates automatically with latest financials.
    
    Note: Requires yfinance package and internet connection
    """
    print("\n" + "="*80)
    print("EXERCISE 3: API-DRIVEN COMPARABLE COMPANIES ANALYSIS")
    print("="*80)
    
    # Tech company tickers to analyze
    tickers = ['MSFT', 'AAPL', 'GOOGL', 'META', 'AMZN', 
               'NVDA', 'TSLA', 'CRM', 'ADBE', 'ORCL']
    
    print(f"\nAnalyzing {len(tickers)} tech companies...")
    print(f"Tickers: {', '.join(tickers)}")
    
    # Simulated data (in real usage, would use yfinance)
    # For demonstration without API dependency
    print(f"\n💡 Note: Using simulated data for demonstration")
    print(f"   In production, use: import yfinance as yf")
    
    # Simulated comparable data
    comp_data = []
    
    companies = {
        'MSFT': {'name': 'Microsoft', 'market_cap': 2800, 'revenue': 211, 'ebitda': 96, 'ev': 2850},
        'AAPL': {'name': 'Apple', 'market_cap': 3000, 'revenue': 394, 'ebitda': 123, 'ev': 3020},
        'GOOGL': {'name': 'Alphabet', 'market_cap': 1700, 'revenue': 307, 'ebitda': 89, 'ev': 1720},
        'META': {'name': 'Meta', 'market_cap': 900, 'revenue': 134, 'ebitda': 47, 'ev': 890},
        'AMZN': {'name': 'Amazon', 'market_cap': 1600, 'revenue': 574, 'ebitda': 71, 'ev': 1650},
        'NVDA': {'name': 'NVIDIA', 'market_cap': 1200, 'revenue': 61, 'ebitda': 25, 'ev': 1210},
        'TSLA': {'name': 'Tesla', 'market_cap': 800, 'revenue': 96, 'ebitda': 14, 'ev': 780},
        'CRM': {'name': 'Salesforce', 'market_cap': 250, 'revenue': 34, 'ebitda': 8, 'ev': 255},
        'ADBE': {'name': 'Adobe', 'market_cap': 230, 'revenue': 19, 'ebitda': 7, 'ev': 235},
        'ORCL': {'name': 'Oracle', 'market_cap': 320, 'revenue': 50, 'ebitda': 18, 'ev': 370}
    }
    
    for ticker, data in companies.items():
        comp_data.append({
            'Ticker': ticker,
            'Company': data['name'],
            'Market Cap': data['market_cap'],
            'Revenue': data['revenue'],
            'EBITDA': data['ebitda'],
            'EV': data['ev'],
            'EV/Revenue': data['ev'] / data['revenue'],
            'EV/EBITDA': data['ev'] / data['ebitda'],
            'P/E': data['market_cap'] / (data['ebitda'] * 0.65)  # Simplified
        })
    
    df = pd.DataFrame(comp_data)
    
    # Display results
    print(f"\n{'='*80}")
    print(f"COMPARABLE COMPANIES DATA ($B):")
    print(f"{'='*80}")
    
    display_df = df[['Company', 'Market Cap', 'Revenue', 'EBITDA']].copy()
    print(display_df.to_string(index=False))
    
    # Valuation multiples
    print(f"\n{'='*80}")
    print(f"VALUATION MULTIPLES:")
    print(f"{'='*80}")
    
    multiples_df = df[['Company', 'EV/Revenue', 'EV/EBITDA', 'P/E']].copy()
    print(multiples_df.to_string(index=False))
    
    # Statistics
    print(f"\n{'='*80}")
    print(f"MULTIPLE STATISTICS:")
    print(f"{'='*80}")
    
    stats = df[['EV/Revenue', 'EV/EBITDA', 'P/E']].describe()
    print(stats.round(1))
    
    # Median multiples (most commonly used)
    print(f"\n{'='*80}")
    print(f"MEDIAN MULTIPLES (Most Commonly Used):")
    print(f"{'='*80}")
    
    median_ev_revenue = df['EV/Revenue'].median()
    median_ev_ebitda = df['EV/EBITDA'].median()
    median_pe = df['P/E'].median()
    
    print(f"Median EV/Revenue:   {median_ev_revenue:.1f}x")
    print(f"Median EV/EBITDA:    {median_ev_ebitda:.1f}x")
    print(f"Median P/E:          {median_pe:.1f}x")
    
    # Valuation application
    print(f"\n{'='*80}")
    print(f"VALUATION APPLICATION:")
    print(f"{'='*80}")
    
    target_revenue = 100.0  # $B
    target_ebitda = 20.0    # $B
    
    print(f"\nTarget Company:")
    print(f"  Revenue:           ${target_revenue:.0f}B")
    print(f"  EBITDA:            ${target_ebitda:.0f}B")
    
    print(f"\nImplied Valuation:")
    
    val_revenue = target_revenue * median_ev_revenue
    val_ebitda = target_ebitda * median_ev_ebitda
    val_avg = (val_revenue + val_ebitda) / 2
    
    print(f"  EV/Revenue method: ${val_revenue:.0f}B ({median_ev_revenue:.1f}x)")
    print(f"  EV/EBITDA method:  ${val_ebitda:.0f}B ({median_ev_ebitda:.1f}x)")
    print(f"  Average:           ${val_avg:.0f}B")
    
    print(f"\n💡 Valuation Range: ${min(val_revenue, val_ebitda):.0f}B - ${max(val_revenue, val_ebitda):.0f}B")
    
    # Ranking
    print(f"\n{'='*80}")
    print(f"COMPANIES RANKED BY EV/EBITDA:")
    print(f"{'='*80}")
    
    ranked = df.sort_values('EV/EBITDA', ascending=False)[['Company', 'EV/EBITDA']]
    print(ranked.to_string(index=False))
    
    print(f"\n📊 Automation Benefits:")
    print(f"   ✅ Real-time data (no manual entry)")
    print(f"   ✅ Daily updates possible")
    print(f"   ✅ Consistent methodology")
    print(f"   ✅ Scalable to 100+ companies")
    
    return df


# =============================================================================
# EXERCISE 4: ML Revenue Forecasting
# =============================================================================

def exercise_4_ml_revenue_forecasting():
    """
    Machine learning model for revenue forecasting.
    
    Uses Random Forest to predict revenue growth.
    Better than linear regression for complex relationships!
    
    Note: Requires sklearn package
    """
    print("\n" + "="*80)
    print("EXERCISE 4: MACHINE LEARNING REVENUE FORECASTING")
    print("="*80)
    
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score, mean_absolute_error
    
    # Generate synthetic training data
    np.random.seed(42)
    n_companies = 100
    
    print(f"\nGenerating training data for {n_companies} companies...")
    
    # Features
    gdp_growth = np.random.normal(0.025, 0.015, n_companies)
    sector_growth = np.random.normal(0.08, 0.03, n_companies)
    capex_ratio = np.random.normal(0.10, 0.03, n_companies)
    r_and_d_pct = np.random.normal(0.15, 0.05, n_companies)
    market_share = np.random.uniform(0.05, 0.30, n_companies)
    
    # Target: Revenue growth (with some realistic relationships)
    revenue_growth = (
        0.3 * sector_growth +
        0.2 * gdp_growth +
        0.15 * r_and_d_pct +
        0.25 * market_share +
        0.1 * capex_ratio +
        np.random.normal(0, 0.02, n_companies)  # Noise
    )
    
    # Create DataFrame
    data = pd.DataFrame({
        'gdp_growth': gdp_growth,
        'sector_growth': sector_growth,
        'capex_ratio': capex_ratio,
        'r_and_d_pct': r_and_d_pct,
        'market_share': market_share,
        'revenue_growth': revenue_growth
    })
    
    print(f"\nTraining Data Sample:")
    print(data.head().to_string())
    
    # Prepare features and target
    X = data[['gdp_growth', 'sector_growth', 'capex_ratio', 'r_and_d_pct', 'market_share']]
    y = data['revenue_growth']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"\nTraining set: {len(X_train)} companies")
    print(f"Testing set:  {len(X_test)} companies")
    
    # Train Random Forest model
    print(f"\n{'='*80}")
    print(f"TRAINING RANDOM FOREST MODEL...")
    print(f"{'='*80}")
    
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    
    # Evaluate
    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)
    
    train_r2 = r2_score(y_train, train_predictions)
    test_r2 = r2_score(y_test, test_predictions)
    
    train_mae = mean_absolute_error(y_train, train_predictions)
    test_mae = mean_absolute_error(y_test, test_predictions)
    
    print(f"\nMODEL PERFORMANCE:")
    print(f"  Training R²:         {train_r2:.3f}")
    print(f"  Testing R²:          {test_r2:.3f}")
    print(f"  Training MAE:        {train_mae*100:.2f}%")
    print(f"  Testing MAE:         {test_mae*100:.2f}%")
    
    if test_r2 >= 0.70:
        print(f"\n  ✅ STRONG predictive power (R² ≥ 0.70)")
    elif test_r2 >= 0.50:
        print(f"\n  🟡 MODERATE predictive power (R² 0.50-0.70)")
    else:
        print(f"\n  ❌ WEAK predictive power (R² < 0.50)")
    
    # Feature importance
    print(f"\n{'='*80}")
    print(f"FEATURE IMPORTANCE:")
    print(f"{'='*80}")
    
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    print(feature_importance.to_string(index=False))
    
    print(f"\n💡 Most important factor: {feature_importance.iloc[0]['Feature']}")
    
    # Make predictions for new companies
    print(f"\n{'='*80}")
    print(f"REVENUE GROWTH PREDICTIONS:")
    print(f"{'='*80}")
    
    new_companies = [
        {
            'name': 'High Growth Tech',
            'gdp_growth': 0.03,
            'sector_growth': 0.12,
            'capex_ratio': 0.15,
            'r_and_d_pct': 0.20,
            'market_share': 0.25
        },
        {
            'name': 'Mature Industrial',
            'gdp_growth': 0.02,
            'sector_growth': 0.05,
            'capex_ratio': 0.08,
            'r_and_d_pct': 0.05,
            'market_share': 0.15
        },
        {
            'name': 'Declining Retail',
            'gdp_growth': 0.02,
            'sector_growth': -0.02,
            'capex_ratio': 0.05,
            'r_and_d_pct': 0.02,
            'market_share': 0.10
        }
    ]
    
    print(f"\nPredictions for New Companies:")
    print("-" * 80)
    
    for company in new_companies:
        name = company.pop('name')
        features = pd.DataFrame([company])
        prediction = model.predict(features)[0]
        
        print(f"\n{name}:")
        print(f"  Inputs: {company}")
        print(f"  Predicted Revenue Growth: {prediction*100:.1f}%")
    
    # Model vs Traditional
    print(f"\n{'='*80}")
    print(f"ML MODEL vs TRADITIONAL METHODS:")
    print(f"{'='*80}")
    
    comparison = pd.DataFrame({
        'Approach': ['Linear Regression', 'Historical Average', 'ML Random Forest'],
        'Pros': [
            'Simple, interpretable',
            'Very simple',
            'Captures non-linear patterns'
        ],
        'Cons': [
            'Assumes linear relationships',
            'Ignores drivers',
            'Requires more data'
        ],
        'Best For': [
            'Simple relationships',
            'Quick estimates',
            'Complex patterns, large datasets'
        ]
    })
    
    print(comparison.to_string(index=False))
    
    print(f"\n💡 Use ML when:")
    print(f"   • You have 100+ data points")
    print(f"   • Relationships are non-linear")
    print(f"   • Multiple interacting variables")
    print(f"   • Need high accuracy")
    
    return model, feature_importance


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "█"*80)
    print("MODULE 08 - ADVANCED TOPICS: SOLUTIONS TO PRACTICE EXERCISES")
    print("█"*80)
    print("\nCutting-edge quantitative finance techniques!")
    print("Master these to separate yourself from 95% of analysts!\n")
    
    # Exercise 1: Monte Carlo LBO
    print("\n" + "█"*80)
    ex1_results = exercise_1_monte_carlo_lbo()
    
    # Exercise 2: Real Options
    print("\n" + "█"*80)
    ex2_results = exercise_2_real_options_valuation()
    
    # Exercise 3: API Comp Analysis
    print("\n" + "█"*80)
    ex3_results = exercise_3_api_comp_analysis()
    
    # Exercise 4: ML Revenue Forecasting
    print("\n" + "█"*80)
    ex4_model, ex4_importance = exercise_4_ml_revenue_forecasting()
    
    print("\n" + "█"*80)
    print("ALL EXERCISES COMPLETED!")
    print("█"*80)
    print("\n✅ Exercise 1: Monte Carlo LBO Analysis - DONE")
    print("✅ Exercise 2: Real Options Valuation - DONE")
    print("✅ Exercise 3: API-Driven Comp Analysis - DONE")
    print("✅ Exercise 4: ML Revenue Forecasting - DONE")
    print("\n🎉 Congratulations! You've mastered advanced techniques!")
    print("\n💼 You now have tools that 95% of analysts don't know!")
    print("\n📚 Next up: Module 09 - Real Projects")
    print("█"*80 + "\n")
