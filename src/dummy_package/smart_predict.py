from sklearn.linear_model import LinearRegression
import numpy as np

def predict_next(numbers):
    X = np.arange(len(numbers)).reshape(-1, 1)
    y = np.array(numbers)

    model = LinearRegression()
    model.fit(X, y)

    next_position = np.array([[len(numbers)]])
    return model.predict(next_position)[0]