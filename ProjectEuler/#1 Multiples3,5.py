sum_mult_3 = 0
sum_mult_5 = 0
intersection = 0
for i in range(1000):
    if i % 3 == 0:
        sum_mult_3 += i
    elif i % 5 == 0:
        sum_mult_5 += i
    elif i % 3 and i % 5 == 0:
        intersection += i
        
print(sum_mult_3+sum_mult_5-intersection)
