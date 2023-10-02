from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = 'https://www.ecb.europa.eu'

date_link_df = pd.read_csv('outputs/date_link.csv')

driver = webdriver.Chrome()
data = []

# Console output for progression
def update_progress(i, total):
    msg = f'Progress: {i} of {total}'
    print(msg, end='\r')
    print(end='', flush=True)

# Scrape the press conference transcripts
for i, row in date_link_df.iterrows():
    update_progress(i+1, len(date_link_df))

    (date, href) = row
    url = BASE_URL + href

    driver.get(url)
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    sections = soup.find_all('div', class_='section')

    texts = []
    for s in sections:
        for p in s.find_all('p'):
            texts.append(p.get_text())

    text = ' '.join(texts)

    data.append([date, text])

# Output dates and conference transcripts into a csv file
df = pd.DataFrame(data, columns=['date', 'text'])
df.to_csv('outputs/raw_text_data.csv', index=False)