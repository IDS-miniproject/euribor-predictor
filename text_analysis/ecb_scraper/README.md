# ECB Press Conference scraper
This directory contains necessary files for scraping ECB press conferences regarding monetary policy staments on key ECB interest rates. Scraped data is located in the [outputs directory](ecb_scraper/outputs/).

Pre-processed text data is within `clean_text_exl_nums.csv` and `clean_text_incl_nums.csv` files. These are otherwise identical files, but the other one has all the numbers excluded from the text.

## Running the scraper
To run the scraper follow these steps:
1. run `python3 get_html.py` - get the page source for press conference list and monetary policy statement list
2. run `python3 get_links.py` - get the links to press conference transcripts from the press conference list
3. run `python3 get_transcripts.py` - get transcript text for each individual press conference
4. run `python3 text_processor.py` - process the text data into more ML friendly format