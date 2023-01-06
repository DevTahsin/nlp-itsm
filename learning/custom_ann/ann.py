import json
import numpy as np
import tensorflow as tf


def load_and_prepare_data(data):
  # Get inputs and labels from data
  inputs = [datapoint['input'] for datapoint in data]
#   print(inputs)
#   inputs = [datapoint['score'] for datapoint in inputs]
  labels = [[datapoint['category'], datapoint['priority']] for datapoint in data]

  
  # Convert inputs and labels to numpy arrays
  inputs = np.array(inputs)
  labels = np.array(labels)
  # convert inputs to inputs score float

  # Normalize input values
  inputs = inputs / inputs.max()

  return inputs, labels

def build_and_compile_model(input_shape):
  # Build model
  model = tf.keras.models.Sequential()
  model.add(tf.keras.layers.Dense(64, input_shape=input_shape, activation='relu'))
  model.add(tf.keras.layers.Dense(32, activation='relu'))
  model.add(tf.keras.layers.Dense(16, activation='relu'))
  model.add(tf.keras.layers.Dense(2))

  # Compile model
  model.compile(optimizer='adam',
                loss=tf.losses.MeanSquaredError(),
                metrics=['accuracy'])

  return model

def train_model(model, inputs, labels):
  # Train model on inputs and labels
  model.fit(inputs, labels, epochs=10, batch_size=64)

def test_model(model, inputs, labels):
  # Evaluate model on test data
  loss, acc = model.evaluate(inputs, labels, batch_size=64)
  print('Test loss:', loss)
  print('Test accuracy:', acc)

if __name__ == '__main__':
  # Load and prepare data
  with open('/Users/tahsingul/Documents/nlp/nlp-itsm/learning/custom_ann/data.json') as f:
        data = json.load(f)

  inputs, labels = load_and_prepare_data(data)

  # Get input shape
  input_shape = inputs[0].shape

  # Build and compile model
  model = build_and_compile_model(input_shape)

  # Train model
  train_model(model, inputs, labels)

  # Test model
  test_model(model, inputs, labels)
