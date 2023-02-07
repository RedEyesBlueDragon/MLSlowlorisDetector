import numpy as np
import pandas as pd

import tensorflow as tf

from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
import logging
import absl.logging
absl.logging.set_verbosity(absl.logging.ERROR)

logging.getLogger('tensorflow').setLevel(logging.ERROR)

dataframe = pd.read_csv("dataset/dataset4.csv")



dataframe = dataframe.drop(columns=["Source", "Destination", "Info"])


train, test = train_test_split(dataframe, test_size=0.2)
train, val = train_test_split(train, test_size=0.2)
print(len(train), 'train examples')
print(len(val), 'validation examples')
print(len(test), 'test examples')


def df_to_dataset(dataframe, shuffle=True, batch_size=32):
	dataframe = dataframe.copy()
	labels = dataframe.pop("Label")
	ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
	if shuffle:
		ds = ds.shuffle(buffer_size=len(dataframe))
	ds = ds.batch(batch_size)
	return ds


batch_size = 32 
train_ds = df_to_dataset(train, batch_size=batch_size)
val_ds = df_to_dataset(val, shuffle=False, batch_size=batch_size)
test_ds = df_to_dataset(test, shuffle=False, batch_size=batch_size)	

feature_columns = []

time = feature_column.categorical_column_with_vocabulary_list(
      'Time', dataframe.Time.unique())
time_embedding = feature_column.embedding_column(time, dimension=8)
feature_columns.append(time_embedding)

protocol = feature_column.categorical_column_with_vocabulary_list(
      'Protocol', dataframe.Protocol.unique())
protocol_embedding = feature_column.embedding_column(protocol, dimension=8)
feature_columns.append(protocol_embedding)

length = feature_column.categorical_column_with_vocabulary_list(
      'Length', dataframe.Length.unique())
length_embedding = feature_column.embedding_column(length, dimension=8)
feature_columns.append(length_embedding)








feature_layer = tf.keras.layers.DenseFeatures(feature_columns)

print("Training:")

model = tf.keras.Sequential([
	feature_layer,
	layers.Dense(128, activation='relu'),
	layers.Dense(128, activation='relu'),
	layers.Dense(128, activation='relu'),
	layers.Dense(128, activation='relu'),
	layers.Dropout(.1),
	layers.Dense(1)
])

model.compile(optimizer='adam',
	loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), metrics=['accuracy'])

model.fit(train_ds,
	validation_data=val_ds,epochs=5)
print("Testdataset Evaluation:")

model.save('saved_model/my_model')

loss, accuracy = model.evaluate(test_ds)


