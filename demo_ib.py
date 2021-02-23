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

print(market_data)


def onPendingTickers(tickers):
    print("Pending ticker event received")
    print(tickers)


ib.pendingTickersEvent += onPendingTickers
ib.run()
