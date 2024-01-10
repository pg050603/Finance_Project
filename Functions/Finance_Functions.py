import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import seaborn as sns

def distributions(df):
    uniform = {i: 1/9 for i in range(1,10)}
    benfords = {i: np.log10(1 + 1/i) for i in range(1, 10)}
    
    actual = df.set_index('Digit')['Probability'].to_dict()
    
    x = np.arange(1, 10)  # x-axis positions for each bar
    
    plt.figure(figsize=(10, 6))

    # plt.bar(x - 0.2, uniform.values(), width=0.2, label='Uniform', color='blue')
    plt.bar(x, benfords.values(), width=0.2, label='Benfords', color='orange')
    plt.bar(x + 0.2, actual.values(), width=0.2, label='Actual', color='green')
    
    plt.title('Histogram of Labels vs Count')
    plt.xlabel('Labels')
    plt.ylabel('Count')
    plt.legend()
    plt.show()
    return

def get_tickers(filepath):
    with open(filepath) as f:
        tickers_df = pd.read_csv(f).iloc[:, 0]
        tickers_df.to_csv('tickers.csv', index=False)
    return

def get_prices(tickers, end_date, start_date):
    symbols = tickers['Symbol'].tolist()
    close_prices = pd.concat([yf.download(symbol, start=start_date, end=end_date, progress=False)['Adj Close'] for symbol in symbols], axis=1)
    close_prices.columns = symbols
    return close_prices
    

def leading_digits(df):
    leading_digit_df = df.applymap(lambda x: str(x)[0])
    flat_series = leading_digit_df.stack()
    digit_counts = flat_series.value_counts().reset_index()
    digit_counts.columns = ['Digit', 'Count']
    
    # Remove digits that are not between 0 and 9
    digit_counts = digit_counts[digit_counts['Digit'].isin(['1', '2', '3', '4', '5', '6', '7', '8', '9'])]
    
    total_count = digit_counts['Count'].sum()
    digit_counts['Probability'] = digit_counts['Count'] / total_count
    
    return digit_counts


def sales_setup(ave, std_dev, num_reps):
    pct_to_target = np.random.normal(avg, std_dev, num_reps).round(2)
    target_values = [75_000, 100_000, 200_000, 300_000, 400_000, 500_000]
    likelihood = [.3, .3, .2, .1, .05, .05]
    sales_target = np.random.choice(target_values, num_reps, p=likelihood)
    df = pd.DataFrame(index=range(num_reps), data={'Pct_To_Target': pct_to_target,
                                                'Sales_Target': sales_target})
    df['Sales'] = df['Pct_To_Target'] * df['Sales_Target']
    return df

def calc_commission_rate(x):
    """ Return the commission rate based on the table:
    0-90% = 2%
    91-99% = 3%
    >= 100 = 4%
    """
    if x <= .90:
        return .02
    if x <= .99:
        return .03
    else:
        return .04

def apply_commission(df):
    df['Commission_Rate'] = df['Pct_To_Target'].apply(calc_commission_rate)
    df['Commission_Amount'] = df['Commission_Rate'] * df['Sales']
    return df

def MC_simulator(num_reps):
    # Define a dataframe to store the results from each simulation that we want to analyze
    all_stats = pd.DataFrame(columns=['Sales', 'Commission_Amount', 'Sales_Target'])

    # Loop through many simulations
    for i in range(num_simulations):
        df = sales_setup(avg, std_dev, num_reps)
        df = apply_commission(df)

        # We want to track sales, commission amounts, and sales targets over all the simulations
        all_stats.loc[i] = [df['Sales'].sum().round(0),
                            df['Commission_Amount'].sum().round(0),
                            df['Sales_Target'].sum().round(0)]

    return all_stats






