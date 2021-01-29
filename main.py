import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
data = yf.download(tickers='pltr', period='1d', interval='1m')
print(data)