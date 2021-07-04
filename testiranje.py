import pandas as pd
import seaborn as sns
from tensorflow.keras.layers import Dense
import tensorflow as tf
from tensorflow.keras.optimizers import SGD


dataset = pd.read_csv('liver-test.csv')
print(dataset.shape)
print(dataset['Dataset'].value_counts())

dataset['Gender'] = dataset['Gender'].apply(lambda x: 1 if x == 'Male' else 0)
test_dataset = dataset
test_labels = test_dataset.pop('Dataset')


model  = tf.keras.models.load_model("modeli/my_model9")


model.evaluate(test_dataset, test_labels, verbose=1)