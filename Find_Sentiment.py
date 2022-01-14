from typing import final
from tensorflow.keras.layers import TextVectorization
import tensorflow as tf
import keras
import pickle
import numpy as np
import extract_tweet

tweet_link = input("Enter the Tweet link: ")
cleaned_text = extract_tweet.getTweet(tweet_link)

model = keras.models.load_model("model.h5") # Loading Saved model
temp = pickle.load(open('vectorizer.pkl','rb')) # Loading Text Vectorizer layer
vectorizer = TextVectorization(max_tokens = temp['config']['max_tokens'],output_mode = 'int',
                                output_sequence_length = temp['config']['output_sequence_length']) # Changing the parameters
vectorizer.adapt(tf.data.Dataset.from_tensor_slices(["xyz"])) # Forming Tensor for dummy variable to set original weights
vectorizer.set_weights(temp['weights']) # Setting Original Weights

string_input = keras.Input(shape=(1,), dtype="string")
x = vectorizer(string_input)
preds = model(x)
final_model = keras.Model(string_input, preds) # pipelining the vectorizing and predicting part

probabilities = final_model.predict([[cleaned_text]])
sentiment = ["Negative","Positive"]
print("*"*10)
print(f"The given Tweet has {sentiment[np.argmax(probabilities[0])]} sentiment.")