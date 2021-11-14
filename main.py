import pandas as pd

from data import order_book
import pickle
from Functions import *


exchanges = ["kraken", "ftx", "coinmate", "currencycom"]
btc= 'BTC/USD'
eth = 'ETH/USD'
bnb = 'BNB/USD'

data_BTC = order_book(symbol=btc, exchanges=exchanges, output='inplace', stop=None, verbose=True)
data_ETH = order_book(symbol=eth, exchanges=exchanges, output='inplace', stop=None, verbose=True)
data_BNB = order_book(symbol=bnb, exchanges=exchanges, output='inplace', stop=None, verbose=True)

# Diccionarios
dic_BTC = crypto(data_BTC, exchanges)
dic_ETH = crypto(data_ETH, exchanges)
dic_BNB = crypto(data_ETH, exchanges)

dic_FINAL_BTC = open("dic_BTC.pkl", "wb")
dic_FINAL_ETH = open("dic_ETH.pkl", "wb")
dic_FINAL_BNB = open("dic_BNB.pkl", "wb")

pickle.dump(dic_BTC, dic_FINAL_BTC)
pickle.dump(dic_ETH, dic_FINAL_ETH)
pickle.dump(dic_BNB, dic_FINAL_BNB)

dic_FINAL_BTC.close()
dic_FINAL_ETH.close()
dic_FINAL_BNB.close()

df_BTC = pd.DataFrame(dic_BTC)
df_ETH = pd.DataFrame(dic_ETH)
df_BNB = pd.DataFrame(dic_BNB)

print(df_BTC)
print(df_ETH)
print(df_BNB)

df_BTC.to_pickle("df_BTC.pkl")
df_ETH.to_pickle("df_ETH.pkl")
df_BNB.to_pickle("df_BNB.pkl")
