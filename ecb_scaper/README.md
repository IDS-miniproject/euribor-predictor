# ECB Press Conference scraper
This directory contains necessary files for scraping ECB press conferences regarding monetary policy staments on key ECB interest rates.  
Scraped data is located in the [outputs directory](ecb_scaper/outputs/).

## Running the scraper
To run the scraper follow these steps:
1. run `python3 get_html.py` - get the page source for press conference list and monetary policy statement list
2. run `python3 get_links.py` - get the links to press conference transcripts from the press conference list
3. run `python3 get_transcripts.py` - get transcript text for each individual press conference
4. run `python3 text_processor.py` - process the text data into more ML friendly format

## TO-DO:
- **Improvement**: Fit all functions into one notebook file for better documentation and avoiding running multiple files
- **Improvement**: Decide what to do with data mismatches; not all monetary policy statements have corresponding press conference and vice versa
- **Next step**: append the ecb key interest rate change numerical data to the dataframe and fit into a ML model. 

  
