import numpy as np

X = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100],
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])
c = np.array([3000, 200, -50, 5000, 100])  # coefficient values


def squared_error(X, y, c):
    predicts = []
    predicted_price = X * c
    for i in range(len(predicted_price)):
        predicts.append(sum(predicted_price[i]))
    sse = float(sum((y - np.asarray(predicts)) ** 2))
    print(sse)


squared_error(X, y, c)