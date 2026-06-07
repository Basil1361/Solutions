import numpy as np
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def stepFunction(t):
    if t >= 0:
        return 1
    return 0

def prediction(X, W, b):
    return stepFunction((np.matmul(X,W)+b)[0])
    # use [0] for one value

# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate = 0.01):
    # We use len(X) because it looks like this:
#     # X = [
#     [0.78051, -0.063669],
#     [0.28774,  0.29139],
#     [0.40714,  0.17878],
#     [0.29230,  0.42170],
#     ...
# ]
    for i in range(len(X)):
        y_hat = prediction(X[i], W, b)
        # for positive values in negative area:
        # y hat only can return 1 and 0
        # a) If the point is at the negative region, but it has a positive value, add αp,αq,αp,αq, and αα to w1,w2,w1,w2, and bb respectively.
        # b) If the point is positive region, but it has a negative value, subtract αp,αq,αp,αq, and αα from w1,w2,w1,w2, and bb respectively.
        if y[i] - y_hat == 1:
        # means a)
        # Weight change:
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate
        # else b:
        elif y[i]-y_hat == -1:
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
        
    return W, b
    
# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
    return boundary_lines
