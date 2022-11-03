# %%
#Importing Modules 
import pandas as pd
import numpy as np 
import xlsxwriter 
import requests
import math

#Obtaining Stock Information 
stocks = pd.read_csv('sp_500_stocks.csv')
stocks.head()

#Acquiring an API Token 
IEX_CLOUD_API_TOKEN = 'Tpk_059b97af715d417d9f49f50b51b1c448'

#Making a first API Call 
symbol = 'AMZN'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()

print(data)

#%% 
#Parsing the Data of API Call 
price = data['latestPrice']
company_name = data['companyName']
company_name, price

#%%
#Adding stocks data to a pandas dataframe
my_columns = ['Ticker', 'Company Name' 'Stock Price', 'Number of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)
final_dataframe.append(pd.Series([symbol,company_name, price,'N/A'], index = my_columns), ignore_index=True )

#%%
#Looping Through the tickers in our list of stocks 
final_dataframe = pd.DataFrame(columns = my_columns)
'''
for stock in stocks['Ticker']:    
    api_url = f'https://sandbox.iexapis.com/stable/stock/{stock}/quote?token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(api_url).json()
    final_dataframe = final_dataframe.append(
    pd.Series(
    [
        stock,
        data['latestPrice'],
        'N/A'
    ],
    index = my_columns),
    ignore_index = True)
    
    final_dataframe.head()
'''


#%% 
#Using Batch API Calls to improve performance
#1.Split the list of tickers in sublists.

#2. Using chuncks function
#2.1. Source: https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks

#3. See batch requests in IEX API documentation

def chunks(lst,n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]

#%%
symbol_groups = list(chunks(stocks['Ticker'],100))
symbol_strings = []
for i in range(0, len(symbol_groups)):
    
    symbol_strings.append(','.join(symbol_groups[i]))
    #print (symbol_strings[i])
    
final_dataframe = pd.DataFrame(columns = my_columns)

for symbol_string in symbol_strings[:1]: 
    batch_api_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol_string}&types=quote&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_api_call_url).json()
    
    for symbol in symbol_string.split(','):
        final_dataframe = final_dataframe.append(
        pd.Series(
        [
            symbol,
            data[symbol]['quote']['latestPrice'],
            'N/A'
        ],
        index = my_columns
        ),
        ignore_index = True
        )


final_dataframe        
# %%
#Calculating the number of shares to buy to reach portifolio size
portifolio_size = 100000
val = float(portifolio_size)

position_size = val/len(final_dataframe.index)

for i in range(0, len(final_dataframe.index)):
    final_dataframe.loc[i, 'Number of Shares to Buy'] = math.floor(position_size/final_dataframe.loc[i,'Stock Price'])

print (final_dataframe)