import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])
def linear(x,c):
    sum = 0
    for index in range(0,len(c)):
        sum += c[index] * x[index]
    return sum
def sigmoid(z):
    sigmoid = 1 / (1 +math.exp(-z))
    return sigmoid
s = sigmoid(linear(x, c1))
print(s)
s = sigmoid(linear(x, c2))
print(s)
s = sigmoid(linear(x, c3))
print(s)
    # add your implementation of the sigmoid function here


# calculate the output of the sigmoid for x with all three coefficients