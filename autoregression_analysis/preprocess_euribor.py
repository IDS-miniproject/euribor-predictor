import pandas as pd
import datetime as dt

# import csv files
eur1mo = pd.read_csv('euribor1mo.csv', header=0, names=('date', 'period', '1mo euribor'))
eur3mo = pd.read_csv('euribor3mo.csv', header=0, names=('date', 'period', '3mo euribor'))
eur6mo = pd.read_csv('euribor6mo.csv', header=0, names=('date', 'period', '6mo euribor'))
eur12mo = pd.read_csv('euribor12mo.csv', header=0, names=('date', 'period', '12mo euribor'))

# merge rates into one data frame
df = eur1mo
df['3mo euribor'] = eur3mo['3mo euribor']
df['6mo euribor'] = eur6mo['6mo euribor']
df['12mo euribor'] = eur12mo['12mo euribor']

# remove day from datetime and set as index
#df = df.reset_index()
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m')
#df.set_index('date', inplace=True)

# store into a csv
df.to_csv("historical_euribor.csv")
