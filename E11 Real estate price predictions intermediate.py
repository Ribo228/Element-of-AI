X = [[66, 5, 15, 2, 500],
     [21, 3, 50, 1, 100],
     [120, 15, 5, 2, 1200]]

# coefficient values
c = [3000, 200, -50, 5000, 100]


def predict(X, c):
    # write a loop that goes over the cabin data and for each cabin prints out
    # the predicted price of the cabin you can assume that the number of inputs
    # and the number of coefficients are the same
    for i in range(len(X)):
        prices = [X[i][j]*c[j] for j in range(len(c))]
        price = sum(prices)

        print(price)

predict(X, c)