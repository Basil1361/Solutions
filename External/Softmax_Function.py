import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    value = np.exp(L)
    sum = np.sum(value)
    result = []
    for i in range(len(L)):
        result.append(value[i]/sum)
    
    return result
    
answer = softmax([1,2,3,4])
print(answer)

# checking probability adds to one
print(np.sum(answer))
    

