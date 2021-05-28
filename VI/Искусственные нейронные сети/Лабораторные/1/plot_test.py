import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 
import pandas as pd
import numpy as np
import tensorflow.keras
from tensorflow.keras import layers
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
from matplotlib import gridspec

df = pd.read_csv('iris.csv', header=None)
dataset = df.values
X = dataset[:,0:4].astype(float)
Y = dataset[:,4]

encoder = LabelEncoder() # sklearn
encoder.fit(Y) # sklearn
encoded_Y = encoder.transform(Y) # sklearn
dummy_y = to_categorical(encoded_Y) # keras

model = Sequential()
model.add(Dense(8, input_shape=(4,), activation='relu'))
model.add(Dense(24, activation='relu'))
model.add(Dense(24, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])
H = model.fit(X, dummy_y, epochs=150, batch_size=10, validation_split=0.1, verbose=2)

model2 = Sequential()
model2.add(Dense(8, input_shape=(4,), activation='relu'))
model2.add(Dense(96, activation='relu'))
model2.add(Dense(72, activation='relu'))
model2.add(Dense(3, activation='softmax'))
model2.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])
H2 = model2.fit(X, dummy_y, epochs=150, batch_size=10, validation_split=0.1, verbose=2)


loss = H.history['loss']
val_loss = H.history['val_loss']
acc = H.history['accuracy']
val_acc = H.history['val_accuracy']
loss2 = H2.history['loss']
val_loss2 = H2.history['val_loss']
acc2 = H2.history['accuracy']
val_acc2 = H2.history['val_accuracy']
epochs = range(1, len(loss) + 1)

fig = plt.figure(figsize=(12,6))
gs = gridspec.GridSpec(1, 2, width_ratios=[3, 3]) 
plt.subplot(gs[0])
plt.plot(epochs, loss, 'r*-', label='Training loss old')
plt.plot(epochs, val_loss, 'r--', label='Validation loss old')
plt.plot(epochs, loss2, 'b*-', label='Training loss new')
plt.plot(epochs, val_loss2, 'b--', label='Validation loss new')
plt.title('Training and validation loss old/new model')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.subplot(gs[1])
plt.plot(epochs, acc, 'r*-', label='Training acc old')
plt.plot(epochs, val_acc, 'r--', label='Validation acc old')
plt.plot(epochs, acc2, 'b*-', label='Training acc new')
plt.plot(epochs, val_acc2, 'b--', label='Validation acc new')
plt.title('Training and validation accuracy old/new model')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
plt.show()