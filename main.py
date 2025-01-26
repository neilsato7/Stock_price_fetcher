import yfinance as yf
import time as t
import requests

# Raw GitHub URL
all_stocks_url = 'https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/all/all_tickers.txt'
nyse_url = 'https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nyse/nyse_tickers.txt'
amex_url = 'https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nyse/nyse_tickers.txt'
nasdaq_url = 'https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/nyse/nyse_tickers.txt'


# Fetch the content of the text file, change the url to be what exchange listing you want.
response = requests.get(nyse_url)
if response.status_code == 200:
    # Split the content by newlines and load it into a set
    tickers = set(response.text.splitlines())
else:
    print(f"Failed to fetch the file: HTTP {response.status_code}")

def fetch_stock_data(ticker, timeperiod):
    # Download data from Yahoo Finance
    # example: yf.download(['MSFT', 'AAPL', 'GOOG'], period='1mo')
    stock = yf.download(ticker, period=f"{timeperiod}", interval="1d")

    # Extract relevant columns
    stock = stock[['Open', 'High', 'Low', 'Close', 'Volume']]
    stock.reset_index(inplace=True)
    return stock

    t.sleep(20)  # Add delay to avoid hitting rate limits

#YFinance valid periods ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']")
timeperiod = '1d'

# Example: initialize variable for all the stock tickers
stocklist = tickers  # Replace with your desired stock tickers

#call the function to get stock data
data = fetch_stock_data(stocklist, timeperiod)

# Display the data for testing
#print(data)

# Optionally, save to a CSV
data.to_csv(f"nyse_last_{timeperiod}.csv", index=False)
