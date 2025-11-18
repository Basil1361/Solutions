import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:

	m, n = X.shape
	y = y.reshape(-1, 1) 	

	theta = np.zeros((n, 1))
	for _ in range(iterations):
		predictions = X @ theta
		errors = predictions - y
		updates = X.T @ errors / m
		theta -= alpha * updates

	return np.round(theta.flatten(), 4) 	# Rounded to 4 decimals