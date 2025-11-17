n = 664000
sum_count = 0
for i in range(n):
    if (i+1) % 2 == 1:
        sum_count += (i+1)**2
    elif (i+1) % 2 == 0:
        pass

print(sum_count)
    