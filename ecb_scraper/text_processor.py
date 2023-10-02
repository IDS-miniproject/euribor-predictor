import pandas as pd
from nltk.stem.porter import *

# With numbers in the data we may risk overfitting it
# as the transcipts may contain direct values on rate changes
remove_numbers = "y" in input('Remove numbers? (y/n): ').lower()

df = pd.read_csv('outputs/raw_text_data.csv')

# make text lowercase
df['text'] = df['text'].str.lower()

# remove punctuation
pattern = r'[^\w\s]+|\d' if remove_numbers else r'[^\w\s]+'
df['text'] = df['text'].str.replace(pattern, '', regex=True)

# remove stopwords
with open("stopwords-en.txt") as f:
    stopwords = set(f.read().split("\n"))
    
df["text"] = df['text'].apply(lambda x: ' '.join([word for word in str(x).split() if word not in (stopwords)]))

# stem words
ps = PorterStemmer()
df["text"] = df["text"].apply(lambda x: ' '.join([ps.stem(word) for word in str(x).split()]))

output_name = 'clean_text_excl_nums.csv' if remove_numbers else 'clean_text_incl_nums.csv'
df.to_csv('outputs/'+output_name, index=False)
