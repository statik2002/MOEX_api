from pprint import pprint

import pandas as pd
import requests


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

pprint(history)

dataframe = pd.DataFrame.from_dict(history['history']['data'], columns=history['history']['columns'], orient='index')

print(dataframe)

