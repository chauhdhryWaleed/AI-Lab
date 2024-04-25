import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Load the cleaned CSV dataset
data = np.genfromtxt('dataset.csv', delimiter=',', skip_header=1, dtype=float)

# Split data into features and labels
X = data[:, 2:-1]  # Excluding race_id, horse_id, and calc_position
y = data[:, -1]  # Target variable (calc_position)

# Normalize the features
X = (X - np.min(X, axis=0)) / (np.max(X, axis=0) - np.min(X, axis=0))

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Define the derivative of the sigmoid activation function
def sigmoid_derivative(x):
    return x * (1 - x)


# Define the number of neurons in each layer
input_neurons = X_train.shape[1]
hidden_neurons = 4
output_neurons = 1

# Define learning rate and number of iterations
learning_rate = 0.1
epochs = 1000

# Initialize weights randomly
np.random.seed(1)
hidden_weights = np.random.uniform(size=(input_neurons, hidden_neurons))
output_weights = np.random.uniform(size=(hidden_neurons, output_neurons))

# Training the MLP
for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(X_train, hidden_weights)
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, output_weights)
    output_layer_output = sigmoid(output_layer_input)

    # Backpropagation
    error = y_train.reshape(-1, 1) - output_layer_output
    d_output = error * sigmoid_derivative(output_layer_output)

    error_hidden_layer = d_output.dot(output_weights.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Update weights
    output_weights += hidden_layer_output.T.dot(d_output) * learning_rate
    hidden_weights += X_train.T.dot(d_hidden_layer) * learning_rate

# Predictions on training set
predicted_train = np.round(output_layer_output)
accuracy_train = np.mean(predicted_train == y_train.reshape(-1, 1))
print("Training Accuracy:", accuracy_train)

# Predictions on testing set
hidden_layer_input_test = np.dot(X_test, hidden_weights)
hidden_layer_output_test = sigmoid(hidden_layer_input_test)
output_layer_input_test = np.dot(hidden_layer_output_test, output_weights)
output_layer_output_test = sigmoid(output_layer_input_test)
predicted_test = np.round(output_layer_output_test)
accuracy_test = np.mean(predicted_test == y_test.reshape(-1, 1))
print("Testing Accuracy:", accuracy_test)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, predicted_test)
print("\nConfusion Matrix:")
print(conf_matrix)

# Classification Report
class_report = classification_report(y_test, predicted_test)
print("\nClassification Report:")
print(class_report)

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, output_layer_output_test)  # Incorrect: Use raw predictions
roc_auc = roc_auc_score(y_test, output_layer_output_test)  # Incorrect: Use raw predictions

# Adjusted ROC Curve and AUC calculation
fpr, tpr, thresholds = roc_curve(y_test, output_layer_output_test)
roc_auc = roc_auc_score(y_test, output_layer_output_test)
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.show()
