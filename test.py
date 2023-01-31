from pprint import pprint

import pandas as pd
import requests
import matplotlib.pyplot as plt


def get_ticket_history(ticker, from_date, till_date):
    url = f'https://iss.moex.com/iss/history/engines/stock/markets/shares/sessions/1/securities/{ticker}.json?'

    params = {
        'from': from_date,
        'till': till_date,
        'lang': 'en',
        'tradingsession': 3,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


history = get_ticket_history('MOEX', '2022-01-01', '2023-01-01')

columns = ['BOARDID', 'TRADEDATE', 'SHORTNAME', 'SECID', 'NUMTRADES', 'VALUE', 'OPEN', 'LOW', 'HIGH', 'LEGALCLOSEPRICE', 'WAPRICE', 'CLOSE', 'VOLUME', 'MARKETPRICE2', 'MARKETPRICE3', 'ADMITTEDQUOTE', 'MP2VALTRD','MARKETPRICE3TRADESVALUE', 'ADMITTEDVALUE', 'WAVAL', 'TRADINGSESSION']

dataframe = pd.DataFrame.from_dict(history['history']['data'])
dataframe.columns = columns

print(dataframe)

df2 = dataframe[['OPEN', 'LOW', 'HIGH', 'CLOSE']].copy()

df3 = dataframe.loc[((dataframe['BOARDID'] == 'TQBR') & (dataframe['CLOSE']))]

print(df3)

plt.plot(df3['CLOSE'])
plt.show()
