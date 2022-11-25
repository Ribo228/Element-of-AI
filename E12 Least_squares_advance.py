import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100],
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100],
              [2000, -250, -100, 150, 250],
              [3000, -100, -150, 0, 150]])

def find_best(X, y, c):
    sse = []
    for i in range(len(c)):
        predicts = []
        predict_price = X * c[i]
        for i in range(len(predict_price)):
            predicts.append(sum(predict_price[i]))
        sse.append(float(sum((y-np.asarray(predicts))**2)))
    smallest_error = min(range(len(sse)),key=sse.__getitem__)
             # edit here: calculate the sum of squared error with coefficient set coeff and
                 # keep track of the one yielding the smallest squared error
    print("the best set is set %d" % smallest_error)


find_best(X, y, c)
