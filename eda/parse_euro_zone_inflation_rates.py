import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.rateinflation.com/inflation-rate/germany-historical-inflation-rate/"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table')

rows = table.find_all('tr')
data = []
for row in rows[1:]:
    cells = row.find_all(['td', 'th'])
    row_data = [cell.text for cell in cells]
    data.append(row_data)

df = pd.DataFrame(data, columns=['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Annual'])

df.drop('Annual', axis=1, inplace=True)

for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col].str.rstrip('%'), errors='coerce') / 100.0

df_melted = pd.melt(df, id_vars=['Year'], var_name='Month', value_name='Interest_Rate')

month_to_number = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
df_melted['Month'] = df_melted['Month'].map(month_to_number)

df_melted.sort_values(['Year', 'Month'], ascending=[False, False], inplace=True)
df_melted.reset_index(drop=True, inplace=True)

df_melted.to_csv('germany_historical_inflation.csv', index=False)
