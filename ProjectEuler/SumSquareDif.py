value = 0 
for i in range(100):
    value += (i+1)
    
squared_value = value**2


value2 = 0 
for i in range(100):
    value2 += (i+1)**2

difference = squared_value - value2
print(difference)
