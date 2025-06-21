import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Generate dummy sequential data
# Let's say we have 100 samples, each with 10 time steps, and 1 feature per step
X_dummy = np.random.rand(100, 10, 1)
y_dummy = np.random.randint(0, 2, size=(100, 1))  # Binary targets

# Build a simple RNN model
model = Sequential([
    SimpleRNN(16, input_shape=(10, 1), activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Print model summary
model.summary()

# Train on dummy data
model.fit(X_dummy, y_dummy, epochs=3, batch_size=8)