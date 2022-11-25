import numpy as np

x_train = np.random.rand(10, 2)  # generate 10 random vectors of dimension 2
x_test = np.random.rand(2)  # generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi) ** 2
    return np.sqrt(sum)

def nearest(x_train, x_test):
    distances = []
    for i in x_train:
        d = dist(i, x_test)
        distances.append(d)
    nearest_index = min(range(len(distances)), key=distances.__getitem__)
    # add a loop here that goes through all the vectors in x_train and finds the one that
    # is nearest to x_test. return the index (between 0, ..., len(x_train)-1) of the nearest
    # neighbor
    print(nearest_index)
    print(x_train)
    print(x_test)

nearest(x_train, x_test)