import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'AX1NT5IY9LZUHZOJ'
ts= TimeSeries(api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol= 'MSFT', interval= '1min',outputsize = 'full')
print(data)

#i= 1
#while i==1:
#    data, meta_data = ts.get_intraday(symbol= 'MSFT', interval= '1min',outputsize = 'full')
#    open with ("data",)
#    time.sleep(60)

close_data = data['4. close']
precentage_change= close_data.pct_change()
print(precentage_change)

last_change = precentage_change[-1]

if abs(last_change)>0.0004:
   print("MSFT ALERT: " + str(last_change))
