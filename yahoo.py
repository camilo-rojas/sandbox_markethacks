import yfinance as yf

slack = yf.Ticker("AAPL")
print(slack.financials)
print(slack.balance_sheet)
print(slack.options)
opt = slack.option_chain(slack.options[6])
print(opt.calls)
strikes = opt.calls.strike
print(strikes.values)
print(min(strikes.values, key=lambda x: abs(x-float(100))))
if float(100.0) in strikes.values:
    print(" in list")
