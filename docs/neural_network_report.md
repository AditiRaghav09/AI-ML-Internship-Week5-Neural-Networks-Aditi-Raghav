# Neural Network Report

## Project Overview

This project demonstrates a simple Multi-Layer Perceptron (MLP) built using TensorFlow and Keras on the Iris dataset.

The goal was to classify Iris flowers into three different species using a neural network.

---

## Neural Network Architecture

The neural network consists of:

- Input Layer: 4 input features
- Hidden Layer 1: 8 neurons with ReLU activation
- Hidden Layer 2: 4 neurons with ReLU activation
- Output Layer: 3 neurons with Softmax activation

---

## Activation Functions

### ReLU (Rectified Linear Unit)

- Used in the hidden layers.
- Helps the network learn complex patterns.
- Faster and commonly used in deep learning.

### Softmax

- Used in the output layer.
- Converts outputs into probabilities.
- Suitable for multi-class classification problems.

---

## Backpropagation

Backpropagation is the learning process used by the neural network.

During training:

- The model makes predictions.
- The error is calculated.
- The weights are updated to reduce the error.
- This process repeats for multiple epochs.

---

## Optimizer

The Adam optimizer was used because:

- It updates weights efficiently.
- It converges faster.
- It is one of the most popular optimizers in deep learning.

---

## Training Results

- Dataset: Iris Dataset
- Epochs: 50
- Batch Size: 16
- Optimizer: Adam
- Loss Function: Categorical Crossentropy
- Metric: Accuracy

The model achieved high accuracy on the test dataset and successfully classified the three Iris flower species.

---

## Conclusion

The project successfully demonstrated the implementation of a simple neural network using TensorFlow and Keras.

The model learned the dataset effectively and achieved good classification performance.
