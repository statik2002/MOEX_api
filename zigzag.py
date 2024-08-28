from progress.bar import Bar
import pandas as pd
import matplotlib.pyplot as plt
import datetime

from functional.api import get_ticket_history

current_date = datetime.date.today()
ticker = 'AFLT'

print('downloading...')
history = get_ticket_history(ticker, '2024-01-01', current_date.__str__(), 24)
print(f'downloading finished. Downloaded {len(history)} bars')

print('start analyzing...')
bar = Bar('Analyzing', max=len(history), fill='#', suffix='%(percent)d%%')
max_bar, min_bar = history[0][2], history[0][3]
max_change, min_change = False, False
for candle in history:
    # in candle [O, C, H, L]
    #print(candle)
    if candle[2] > max_bar:
        max_bar = candle[2]
        max_change = True
    else:
        max_change = False

    if candle[3] < min_bar:
        min_bar = candle[3]
        min_change = True
    else:
        min_change = False

    if not max_change and min_change:
        print('Up POINT')
        print(candle)
        print(f'Max: {max_bar}, Max_change: {max_change}, Min: {min_bar}, Min_change: {min_change}')
    if not min_change and max_change:
        print('Down POINT')
        print(candle)
        print(f'Max: {max_bar}, Max_change: {max_change}, Min: {min_bar}, Min_change: {min_change}')



#print(f'Max: {max_bar}, Max_change: {max_change}, Min: {min_bar}, Min_change: {min_change}')

