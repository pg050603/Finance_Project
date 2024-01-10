import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def distributions():
    uniform = {i: 1/9 for i in range(1,10)}
    benfords = {i: np.log10(1 + 1/i) for i in range(1, 10)}


    labels = list(uniform.keys())
    uniform_values = list(uniform.values())
    benfords_values = list(benfords.values())

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x + width/2, benfords_values, width, label='Benfords')
    rects2 = ax.bar(x - width/2, uniform_values, width, label='Uniform')


    ax.set_xlabel('Digits')
    ax.set_ylabel('Distribution')
    ax.set_title('Uniform vs Benfords Distribution')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    fig.tight_layout()
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
    