from pprint import pprint

import pandas as pd
import requests
import matplotlib.pyplot as plt


def get_ticket_history(ticker, from_date, till_date, interval):
    url = f'https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{ticker}/candles.json'

    page = 0

    response_data = []

    params = {
        'from': from_date,
        'till': till_date,
        'start': page,
        'interval': interval,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    for line in response.json()['candles']['data']:
        response_data.append(line)

    page += 500

    while response:
        params = {
            'from': from_date,
            'till': till_date,
            'start': page,
            'interval': interval,
        }
        response = requests.get(url, params=params)
        response.raise_for_status()

        if not response.json()['candles']['data']:
            break

        for line in response.json()['candles']['data']:
            response_data.append(line)
        page += 500

    return response_data


history = get_ticket_history('SBER', '2010-01-01', '2023-01-01', 24)

dataframe = pd.DataFrame(history, columns=['open', 'close', 'high', 'low', 'value', 'volume', 'begin', 'end'])

print(dataframe)

plt.plot(dataframe['close'])
plt.show()
