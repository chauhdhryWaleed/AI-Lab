import tensorflow as tf
from keras.datasets import mnist, fashion_mnist
from keras.models import Sequential
from keras.layers import Flatten, Dense
from keras.utils import to_categorical
import time

# Load MNIST and Fashion MNIST datasets
(X_train_mnist, y_train_mnist), (X_test_mnist, y_test_mnist) = mnist.load_data()
(X_train_fashion, y_train_fashion), (X_test_fashion, y_test_fashion) = fashion_mnist.load_data()

# Normalize pixel values
X_train_mnist, X_test_mnist = X_train_mnist / 255.0, X_test_mnist / 255.0
X_train_fashion, X_test_fashion = X_train_fashion / 255.0, X_test_fashion / 255.0

# One-hot encode the labels
y_train_mnist = to_categorical(y_train_mnist, num_classes=10)
y_test_mnist = to_categorical(y_test_mnist, num_classes=10)
y_train_fashion = to_categorical(y_train_fashion, num_classes=10)
y_test_fashion = to_categorical(y_test_fashion, num_classes=10)

def single_layer_nn(input_shape):
    model = Sequential([
        Flatten(input_shape=input_shape),
        Dense(10, activation='softmax')
    ])
    return model

def mlp(input_shape):
    model = Sequential([
        Flatten(input_shape=input_shape),
        Dense(256, activation='relu'),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])
    return model

def fc_dnn(input_shape):
    model = Sequential([
        Flatten(input_shape=input_shape),
        Dense(512, activation='relu'),
        Dense(256, activation='relu'),
        Dense(128, activation='relu'),
        Dense(10, activation='softmax')
    ])
    return model

def train_and_evaluate(model, X_train, y_train, X_test, y_test, epochs=5):
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    start_time = time.time()
    model.fit(X_train, y_train, epochs=epochs, verbose=1)
    end_time = time.time()
    print('Finished Training')
    print('Training time: {:.2f} seconds'.format(end_time - start_time))
    _, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print('Test accuracy:', accuracy)

print("Training and Evaluating Single Layer Neural Network on MNIST:")
single_layer_model_mnist = single_layer_nn(input_shape=(28, 28))
train_and_evaluate(single_layer_model_mnist, X_train_mnist, y_train_mnist, X_test_mnist, y_test_mnist)

print("\nTraining and Evaluating Multi-Layer Perceptron on MNIST:")
mlp_model_mnist = mlp(input_shape=(28, 28))
train_and_evaluate(mlp_model_mnist, X_train_mnist, y_train_mnist, X_test_mnist, y_test_mnist)

print("\nTraining and Evaluating Fully Connected Deep Neural Network on MNIST:")
fc_dnn_model_mnist = fc_dnn(input_shape=(28, 28))
train_and_evaluate(fc_dnn_model_mnist, X_train_mnist, y_train_mnist, X_test_mnist, y_test_mnist)

print("\nTraining and Evaluating Single Layer Neural Network on Fashion MNIST:")
single_layer_model_fashion = single_layer_nn(input_shape=(28, 28))
train_and_evaluate(single_layer_model_fashion, X_train_fashion, y_train_fashion, X_test_fashion, y_test_fashion)

print("\nTraining and Evaluating Multi-Layer Perceptron on Fashion MNIST:")
mlp_model_fashion = mlp(input_shape=(28, 28))
train_and_evaluate(mlp_model_fashion, X_train_fashion, y_train_fashion, X_test_fashion, y_test_fashion)

print("\nTraining and Evaluating Fully Connected Deep Neural Network on Fashion MNIST:")
fc_dnn_model_fashion = fc_dnn(input_shape=(28, 28))
train_and_evaluate(fc_dnn_model_fashion, X_train_fashion, y_train_fashion, X_test_fashion, y_test_fashion)
