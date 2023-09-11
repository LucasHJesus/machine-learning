import numpy as np
import itertools

class Perceptron:
    def _init_(self, input_size, learning_rate=0.01, epochs=100):
        self.weights = np.zeros(input_size + 1)  # +1 for the bias weight
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activate(self, x):
        return 1 if x >= 0 else -1

    def train(self, X, y):
        for _ in range(self.epochs):
            for inputs, target in zip(X, y):
                inputs = np.insert(inputs, 0, 1)  # Adding bias input
                prediction = self.activate(np.dot(self.weights, inputs))
                error = target - prediction
                self.weights += self.learning_rate * error * inputs

    def predict(self, X):
        predictions = []
        for inputs in X:
            inputs = np.insert(inputs, 0, 1)
            prediction = self.activate(np.dot(self.weights, inputs))
            predictions.append(prediction)
        return predictions


# # Example usage
# X = np.array([[1 if i == j else -1 for j in range(25)] for i in range(25)])
# target_pattern = np.array([1 if i == 0 else -1 for i in range(25)])
#
# perceptron = Perceptron(input_size=25)
# perceptron.train(X, target_pattern)
#
# # Testing the trained perceptron
# test_data = np.array([[1 if i == j else -1 for j in range(25)] for i in range(25)])
# predictions = perceptron.predict(test_data)
# print(test_data)
# print("----------------------------------------------------------------------")
# print(predictions)
# print("----------------------------------------------------------------------")
# print(target_pattern)


def generate_test_cases():
    test_cases = []
    for x1, x2, x3, x4, x5, x6, x7, x8, x9 in itertools.product([-1, 1], repeat=9):
        temp = []
        temp.append(x1)
        temp.append(x2)
        temp.append(x3)
        temp.append(x4)
        temp.append(x5)
        temp.append(x6)
        temp.append(x7)
        temp.append(x8)
        temp.append(x9)
        test_cases.append(temp)
    return test_cases


X = generate_test_cases()

grid_x = [1, -1, 1, -1, 1, -1, 1, -1, 1]

target_pattern = np.array([1 if i == X.index(grid_x) else -1 for i in range(512)])

perceptron = Perceptron(input_size=9)
perceptron.train(X, target_pattern)

test_data = X
predictions = perceptron.predict(test_data)

print(predictions.count(1))

print()

print(target_pattern)

print()

print(predictions.count(1))