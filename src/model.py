# Neural Network Model Definition

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create the model
model = Sequential([
    Dense(8, activation='relu', input_shape=(4,)),
    Dense(4, activation='relu'),
    Dense(3, activation='softmax')
])

# Display model summary
model.summary()
