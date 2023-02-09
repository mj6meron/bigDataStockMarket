import yfinance as yf

# Retrieve the TSLA data from Yahoo Finance
tsla = yf.download('TSLA', start='2010-01-01', end='2023-02-08')

# Print the head of the data
print(tsla.head())