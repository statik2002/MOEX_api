import datetime
from pprint import pprint
from progress.bar import Bar
import pandas as pd
import matplotlib.pyplot as plt
from functional.classes import ResistLine


from functional.api import get_ticket_history, get_securities, get_security, get_index, get_engines, \
    get_engine_description, get_engine_markets, get_market_fields_description, get_trades_modes, get_all_securities, \
    get_security_candles, get_spec_security

current_date = datetime.date.today()
ticker = 'SBER'

print('downloading...')
history = get_ticket_history(ticker, '2024-01-01', current_date.__str__(), 10)
print(f'downloading finished. Downloaded {len(history)} bars')
print('start analyzing...')
bar = Bar('Analyzing', max=len(history), fill='#', suffix='%(percent)d%%')
for candle in history:
    bar_counter = 0
    for analyze_bar in history:
        if candle[0] == analyze_bar[0] or candle[0] == analyze_bar[1]:
            bar_counter += 1

    if bar_counter > 3:
        ResistLine(candle[0], bar_counter)

    bar.next()

print(f'Found {len(ResistLine.resist_lines)} resists.')
for line in ResistLine.resist_lines:
    print(line)

#pprint(history)


#dataframe = pd.DataFrame(history, columns=['open', 'close', 'high', 'low', 'value', 'volume', 'begin', 'end'])

#print(dataframe)



#plt.xlabel('Дни')
#plt.ylabel('Цена')
#plt.suptitle(ticker)
#plt.plot(dataframe['close'])
#plt.show()


#data = get_securities('SBER')
#data = get_security('SBER')
#data = get_index()
#data = get_engines()
#data = get_engine_description('stock')
#data = get_engine_markets('stock')
#data = get_market_fields_description('stock', 'shares')
#data = get_trades_modes('stock', 'shares')
#data = get_all_securities('stock', 'shares', securities=['SBER', 'VTBR'])
#data = get_spec_security('stock', 'shares', security='SBER')
#data = get_security_candles('stock', 'shares', 'SBER')

#pprint(data)
