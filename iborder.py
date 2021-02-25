from ib_insync import *
import config

ib = IB()
ib.connect(config.IP, config.PORT, clientId=13)

stock = Stock('AAPL', 'SMART', 'USD')
order = LimitOrder("BUY", 5, 15)
# order=MarketOrder('BUY', 10)
trade = ib.placeOrder(stock, order)
print(trade)


def orderFilled():
    print("Order has been filled")


trade.fillEvent += orderFilled
ib.run()

# ib.trades() and ib.orders() save the trades and orders sent
