# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:38:35 2018

@author: farai.ndawana
"""
import requests
import numpy as np
import pandas as pd
import xmltodict
from pandas import *

# read xml data structure and write to json

from urllib.request import urlopen
file = urlopen('https://df-alpha.bk.rw/interview01/customers')


c_url = file.read()
file.close()
custUrl = xmltodict.parse(c_url)

#read  url  API

transUrl = requests.get('https://df-alpha.bk.rw/interview01/transactions').json()



#load dataframes
transactions_df = pd.DataFrame(transUrl)
customers_df = pd.DataFrame(custUrl)

#print(customers_df)


#rename columns
transactions_df.rename(columns={'customerId' :'Customer_Id','amount':'Amount'})




#add id and beginning of df

transactions_df['Transaction_ID'] = np.random.randint(1, 50000, transactions_df.shape[0])



#convert date type

pd.to_datetime(transactions_df['timestamp']).apply(lambda x: x.date())

#drop extra columns

transactions_df.drop(['latitude','longitude'], axis=1 ,inplace=True)


# drop duplicates to make sure this is unqiue
# it should be unique
customers_df.drop_duplicates()

#join data frames


df = pd.merge(transactions_df, customers_df,
                       how='left', on=['id'])



#group by City 

city_totals_df =transactions_df.groupby('City_Name').apply(lambda x :pd.Series(dict(transactions_df=xshape[0],
                                       
    Total_Amount=x.Amount.sum(),
    
    Unique_Customer =x,
    
    Total_transactions =x
    
    ))).reset_index()


#order columns

transactions_ds[('Transactions_ID','DateTime','Customer_Id','Customer_Name','Amount','City_Name')]

#write output

transactions_df.to_csv('transactions.csv')

city_totals_df.to_csv('city_totals.csv')
