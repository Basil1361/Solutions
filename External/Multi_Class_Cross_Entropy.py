import numpy as np

def multi_cross_entropy(Y, p):
    loss_total = 0
    for i in range(len(Y)):
        # solve for down row
        for j in range(len(Y[i])):
            # solve for across row
            loss_total += Y[i][j]*np.log(p[i][j])
    return -loss_total

# Loop:
# choose a row first
# then move across that row

# i = 0
# j = 0, 1, 2

# i = 1
# j = 0, 1, 2

# i = 2
# j = 0, 1, 2


example = [
    [0, 1, 0],   # Duck: Door 2 is correct
    [1, 0, 0],   # Beaver: Door 1 is correct
    [0, 0, 1]    # Seal: Door 3 is correct
]

probability = [
    [0.1, 0.8, 0.1],
    [0.6, 0.3, 0.1],
    [0.2, 0.2, 0.6]
]            

answer = multi_cross_entropy(example, probability)
print(answer)
