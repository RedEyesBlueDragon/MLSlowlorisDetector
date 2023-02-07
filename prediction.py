import numpy as np
import pandas as pd
import csv

import tensorflow as tf

from tensorflow import feature_column
from tensorflow.keras import layers


# A utility method to create a tf.data dataset from a Pandas Dataframe
def df_to_dataset(dataframe, shuffle=True, batch_size=32):
    dataframe = dataframe.copy()
    ds = tf.data.Dataset.from_tensor_slices((dict(dataframe)))
    if shuffle:
        ds = ds.shuffle(buffer_size=len(dataframe))
    ds = ds.batch(batch_size)
    return ds

model = tf.keras.models.load_model('saved_model/my_model')

dataframe = pd.read_csv("dataset/pred.csv")


dataframe = dataframe.drop(columns=["Source", "Destination", "Info"])

new_ds = df_to_dataset(dataframe, shuffle=False, batch_size=32)

predictions = model.predict(new_ds)
if predictions[0] > 0.5:
    print("Attack")
else:
    print("Regular Traffic")    
