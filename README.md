# Twitter-Sentiment
Convolutional neural network model for finding sentiment of the given tweet.

The model is built using [this dataset from Kaggle](https://www.kaggle.com/kazanova/sentiment140). It has 1.6 Million tweets with equal distribution among Positive and negative sentiments.

After building the model, a utility program (Find_Sentiment.py) is created. When the program is run, it uses the extract_tweet.py to extract the text content from given tweet URL. The text is then preprocessed, vectorized using the trained vector. Then vector is finally given to the model to get the result.
