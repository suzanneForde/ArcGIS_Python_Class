
# Converting occurence.txt into a .csv file for week 5 challenge


import pandas as pd
import os



try:
    df=pd.read_csv('occurence.text', sep='\t')
    df.to_csv('occurence.csv', index=False)
except Exception as e:
    print("Error", e)

if os.path.isfile('occurence.csv'):
    print("CSV file exists")
else:
    print("CSV file does note exist")


