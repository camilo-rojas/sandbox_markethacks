import pandas as pd
from finvizfinance.quote import finvizfinance

stock = finvizfinance('tsla')

stock_fundament = stock.TickerFundament()
print(stock_fundament)
