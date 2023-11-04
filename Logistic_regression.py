import numpy as np

def sigmoid(z):
  """
  Computes the sigmoid function.

  Args:
    z: A numpy array of any shape.

  Returns:
    A numpy array of the same shape as z, containing the sigmoid values of the elements of z.
  """

  return 1 / (1 + np.exp(-z))

def logistic_regression(X, y, learning_rate=0.01, num_iterations=1000):
  """
  Performs logistic regression on the given data.

  Args:
    X: A numpy array of shape (m, n), where m is the number of training examples
      and n is the number of features.
    y: A numpy array of shape (m, 1), where m is the number of training examples
      and 1 is the number of labels.
    learning_rate: The learning rate.
    num_iterations: The number of iterations to train the model for.

  Returns:
    A numpy array of shape (n, 1), where n is the number of features and 1 is
    the number of labels.
  """

  # Initialize the weights.
  theta = np.zeros((X.shape[1], 1))

  # Train the model.
  for i in range(num_iterations):
    # Calculate the predictions.
    h = sigmoid(np.dot(X, theta))

    # Calculate the error.
    error = y - h

    # Update the weights.
    theta += learning_rate * np.dot(X.T, error)

  return theta

# Load the data.
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([[1], [0], [1]])

# Train the model.
theta = logistic_regression(X, y)

# Make predictions.
predictions = sigmoid(np.dot(X, theta))

# Print the predictions.
print(predictions)
