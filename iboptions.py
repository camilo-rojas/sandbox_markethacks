from ib_insync import *
import config

ib = IB()
ib.connect(config.IP, config.PORT, clientId=13)

stock = Stock('AAPL', 'SMART', 'USD')
ib.qualifyContracts(stock)

print(stock)
ib.sleep(2)
chains = ib.reqSecDefOptParams(
    stock.symbol, '', stock.secType, stock.conId)
print(chains)
