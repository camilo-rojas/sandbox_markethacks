# Demo for Interactive Brokers

from ib_insync import *

ib=IB()
ib.connect('127.0.0.1',7497,clientId=1)

contract = Stock('AAPL', 'SMART', 'USD')
bars = ibm.reqHistorialData(contract, endDateTime='', durationStr'30 D', barsizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

df?util.df(bars)
print(df)
