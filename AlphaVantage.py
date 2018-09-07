

import requests
import pandas as pd
from datetime import datetime as dt

Ticker = 'IBM'
Time   = 1 # minutes (1/5/15/30)

Url  = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY' +\
       '&interval='+str(Time)+'min&symbol='+str(Ticker)+ '&apikey={}'
Api_Key=open('alpha.txt','r').read()
Json = requests.get(Url.format(Api_Key))
Json = Json.json()
Json = Json['Time Series (' + str(Time)+ 'min)']

Data = pd.DataFrame(columns=['Date','Open','High','Low','Close','Volume'])
for d,p in Json.items():
    date = dt.strptime(d, '%Y-%m-%d %H:%M:%S')
    data_row=[date,float(p['1. open']),float(p['2. high']),float(p['3. low']),float(p['4. close']),int(p['5. volume'])]
    Data.loc[-1,:]=data_row
    Data.index=Data.index+1
Data=Data.sort_values('Date')
Data.set_index('Date', inplace=True)






  

