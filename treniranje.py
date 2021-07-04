import pandas as pd
import tensorflow as tf

dataset = pd.read_csv('liver-train.csv')

dataset['Gender'] = dataset['Gender'].apply(lambda x: 1 if x == 'Male' else 0)
dataset['Albumin_and_Globulin_Ratio'] = dataset['Albumin_and_Globulin_Ratio'].fillna(dataset['Albumin_and_Globulin_Ratio'].mean())


train_dataset = dataset.sample(frac=0.875,random_state=0)
validation_dataset = dataset.drop(train_dataset.index)

train_labels = train_dataset.pop('Dataset')
validation_labels = validation_dataset.pop('Dataset')


model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu',),
    tf.keras.layers.Dense(14, kernel_initializer = 'uniform', activation='relu'),
    tf.keras.layers.Dense(128, kernel_initializer = 'uniform', activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(128, kernel_initializer = 'uniform', activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(2, activation='softmax'),
  ])
model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=['accuracy'],
)

EPOCHS = 50
history = model.fit(train_dataset, 
                    train_labels, 
                    validation_data=(validation_dataset, validation_labels),
                    batch_size = 128,
                    epochs=EPOCHS,
                    verbose=1 )
model.save("my_model14")
model.summary()

