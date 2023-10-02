from bs4 import BeautifulSoup
import pandas as pd

# Extract dates of monetary policy statements
mopo_soup = BeautifulSoup(open('outputs/mopo.html'), "html.parser")
divs = mopo_soup.find_all("div", class_='lazy-load loaded')

policy_dates = []
for div in divs:
    dt_elements = div.find_all("dt", recursive=False)
    for dt in dt_elements:
        policy_dates.append(dt['isodate'])


# Extract date and link of each conference
conf_soup = BeautifulSoup(open('outputs/conf.html'), "html.parser")

dt_list = conf_soup.find_all("dt") # term elements contain the date
dd_list = conf_soup.find_all("dd") # description elements contain the link

if(len(dt_list) != len(dd_list)):
    raise Exception(f"Mismatch in dt ({len(dt_list)}) and dd ({len(dd_list)}) count. Check the conf.html file.")

conf_hrefs = []
conf_dates =[]

# Extract the date and link from each term and description
for (dt, dd) in dict(zip(dt_list, dd_list)).items():
    date = dt['isodate']

    anchor = dd.find_next('div', class_='title').find('a')
    text = anchor.get_text().lower().replace(' ', '')

    # The page source includes also some entries that are not conferences related to monetary policy decisions.
    # We filter out these entries by checking if the text contains both 'q&a' and 'statement'
    if 'q&a' in text and 'statement' in text:
        conf_hrefs.append(anchor['href'])
        conf_dates.append(date)

print(f'Total amount of conference transciptions: {len(conf_hrefs)}\n')

# Compare the dates of monetary policy statements and conference transcripts and find mismatches
missing_conf_dates = []
missing_policy_dates = []

for date in policy_dates:
    if date not in conf_dates:
        missing_conf_dates.append(date)

for date in conf_dates:
    if date not in policy_dates:
        missing_policy_dates.append(date)

if len(missing_conf_dates) > 0:
    text = f'Monetary policy statements without corresponding conference transcipt ({len(missing_conf_dates)}):\n' + '\n'.join(missing_conf_dates)
    with open('outputs/missing_conf_dates.txt', 'w') as f:
        f.write(text)

if len(missing_policy_dates) > 0:
    text = f'Conference transcipts without corresponding monetary policy statement ({len(missing_policy_dates)}):\n' + '\n'.join(missing_policy_dates)
    with open('outputs/missing_policy_dates.txt', 'w') as f:
        f.write(text)

if (len(missing_conf_dates) > 0 or len(missing_policy_dates) > 0):
    print('Mismatch in policy statements and conference transcripts. Check the outputs for details.')

# Output conference dates and links into a csv file
date_link_df = pd.DataFrame(list(zip(conf_dates, conf_hrefs)), columns=['date', 'link'])
date_link_df.to_csv('outputs/date_link.csv', index=False)


