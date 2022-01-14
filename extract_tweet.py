import os
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize


lemmatizer = WordNetLemmatizer() # Lemmatizer to get the root word of any given word
stemmer = PorterStemmer() # Stemmer for normalizing similar words
stop_list = stopwords.words('english')


def preprocess_text(text):
  tokens = word_tokenize(text) # Tokenizing given text
  nw_removed = [word for word in tokens if word not in stop_list]
  ls = []
  for w in nw_removed: # For each word in the token
    ls.append(lemmatizer.lemmatize(stemmer.stem(w))) # First we are stemming the word and finding its root word using lemmatizing
    # It is then appended to the list

  return ' '.join(ls) # returning the preprocessed words as a string

def extract_text(tweet):
  t1 = re.sub(r'@\S+',' ',tweet) # Removing any user mentions
  t1 = re.sub(r'http\S+',' ',t1) # Removing any URLs
  return preprocess_text(re.sub(r'[^0-9a-zA-Z]+',' ',t1).strip().lower())
    # Removing extra spaces and sending only lowercase alphanumeric characters


def getTweet(tweet_link):
    tweet_id = getTweetId(tweet_link).strip()
    os.system(f"snscrape --jsonl twitter-tweet {tweet_id} >tweet-content.json")
    content = pd.read_json("./tweet-content.json",lines = True,orient="records")
    return extract_text(content["renderedContent"][0])

def getTweetId(tweet_link):
    tweet_link = re.sub(r'https\S+s/',"",tweet_link)
    tweet_id = re.sub(r'[^0-9]+',' ',tweet_link).strip()
    return tweet_id
