#%%
#Importing Modules 
import pandas as pd
import numpy as np 
import xlsxwriter 
import requests
import math
import os 

print (os.getcwd())

#%%
#Obtaining stock information 
stocks = pd.read_csv('sp_500_stocks.csv')


#%%
#API Token 
IEX_CLOUD_API_TOKEN = 'Tpk_059b97af715d417d9f49f50b51b1c448'

#%%
#Making first API Call
symbol = 'AMZN'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()

print(data)

#%%
#Parsing API data
price = data['latestPrice']
company_name = data['companyName']

company_name, price

#%% Adding our stocks data to a pandas dataframe 
my_columns = ['Ticker','Company Name', 'Stock Price', 'Number of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)
final_dataframe

#%%
final_dataframe.append(
    pd.Series(
    [
        symbol,
        company_name,
        price,
        'N/A'
    ], index = my_columns),ignore_index=True)
