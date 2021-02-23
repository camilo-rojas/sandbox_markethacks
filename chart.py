import plotly.graph_objects as go
import pandas

df = pandas.read_csv('stock.csv')

figure = go.Figure(data=[go.Candlestick(
    x=df['date'], open=df['open'], high=df['high'], low=df['low'], close=df['close'])])
figure.layout.xaxis.type = "category"  # take out the weekend
figure.show()
