import Benford_Functions as bf

# Set up initial distribution
# bf.distributions()

# Get tickers
# filepath = r'C:\Users\pgile\Downloads\VSCode\CondaTest\SP500.csv'
# bf.get_tickers(filepath)

# Set up tickers and dates parameters
# tickers_df = bf.pd.read_csv(r'C:\Users\pgile\Downloads\VSCode\CondaTest\tickers.csv')
# end_date = bf.datetime.today()
# start_date = end_date - bf.timedelta(days=365*5)

# Get 5 year prices for all stocks s&p500 last 5 years
# prices = bf.get_prices(tickers_df, end_date, start_date)
# prices.to_csv('SP500_5yr_prices.csv')

hist_prices = bf.pd.read_csv(r'C:\Users\pgile\Downloads\VSCode\CondaTest\SP500_5yr_prices.csv', index_col=0)

row_1 = hist_prices.iloc[0]

leading_digits = [int(str(data)[0]) for data in row_1]

print(leading_digits)


# hist_prices['Symbols'].apply(lambda x: int(str(x)[0]))
# leading_digit_counts = {}

# for digit in range(1, 10):
#     count = hist_prices[hist_prices['Leading Digit'] == digit].shape[0]
#     leading_digit_counts[digit] = count


# print(leading_digit_counts)
