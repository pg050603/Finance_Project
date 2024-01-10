from Functions.Finance_Functions import *

filepath = r'data\SP500.csv'
# get_tickers(filepath)

# # Set up tickers and dates parameters
tickers_df = pd.read_csv(r'data\tickers.csv')
end_date = datetime.today()
start_date = end_date - timedelta(days=365*5)

# # Get 5 year prices for all stocks s&p500 last 5 years
# prices = get_prices(tickers_df, end_date, start_date)
# prices.to_csv('SP500_5yr_prices.csv')

hist_prices = pd.read_csv(r'data\SP500_5yr_prices.csv', index_col=0)

digit_occurs = leading_digits(hist_prices)

distributions(digit_occurs)


# a = MC_simulator(num_reps)

# a['Away_From_Target'] = a['Sales_Target'] - a['Sales']

# # Create a histogram of the away from target values
# plt.figure(figsize=(10, 6))
# sns.histplot(data=a, x='Away_From_Target', bins=30)
# plt.title('Histogram of Away From Target')
# plt.xlabel('Away From Target')
# plt.ylabel('Frequency')
# plt.show()

# sns.set_style('whitegrid')

# avg = 1
# std_dev = .1
# num_reps = 500

# num_simulations = 1000

# row_1 = hist_prices.iloc[0]

# get_tickers()


# a = MC_simulator(num_reps)

# a['Away_From_Target'] = a['Sales_Target'] - a['Sales']

# # Create a histogram of the away from target values
# plt.figure(figsize=(10, 6))
# sns.histplot(data=a, x='Away_From_Target', bins=30)
# plt.title('Histogram of Away From Target')
# plt.xlabel('Away From Target')
# plt.ylabel('Frequency')
# plt.show()

# sns.set_style('whitegrid')

# avg = 1
# std_dev = .1
# num_reps = 500

# num_simulations = 1000
