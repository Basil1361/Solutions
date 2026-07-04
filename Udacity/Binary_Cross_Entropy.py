import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    listing = []
    for i in range(len(Y)):
        if Y[i] == 0:
            new_prob = 1-P[i]
            new_log = -np.log(new_prob)
            listing.append(new_log)
        elif Y[i] == 1:
            log = -np.log(P[i])
            listing.append(log)
    return np.sum(listing)
            
# faster way:

# def cross_entropy(Y, P):
#     loss = 0
#     for y,p in zip(Y,P):
#         if y == 0:
#             loss += np.log(1-p)
#         elif y ==1:
#             loss += np.log(p)
#     return -loss

# How Zip works:
# Y = [1, 0, 1]
# P = [0.9, 0.2, 0.8]

# for y, p in zip(Y, P):

# y = 1, p = 0.9
# y = 0, p = 0.2
# y = 1, p = 0.8

# how enum works:
# Y = [1, 0, 1]

# for i, y in enumerate(Y):
#     print(i, y)

# 0 1
# 1 0
# 2 1