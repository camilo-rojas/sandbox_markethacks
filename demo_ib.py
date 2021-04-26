# Demo for Interactive Brokers

from ib_insync import *
import config

ib = IB()
ib.connect(config.IP, config.PORT, clientId=12)

contract = Stock('AAPL', 'SMART', 'USD')
bars = ib.reqHistoricalData(contract, endDateTime='', durationStr='30 D',
                            barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

df = util.df(bars)
print(df)

ib.sleep(2)
market_data = ib.reqMktData(contract, '', False, False)
# variables in stock, out price, %change, %Volume

print(market_data)


def onPendingTickers(tickers):
    print("Pending ticker event received")
    print(tickers)


ib.pendingTickersEvent += onPendingTickers
ib.run()

#        df = df.append({'stock': self.symbol, 'price': stock.TickerFundament().get('Price'),
#                        '%Change': float(stock.TickerFundament().get('Change').strip('%'))/100,
#                        '%Volume':
#                        float(stock.TickerFundament().get('Rel Volume'))}, ignore_index=True)
