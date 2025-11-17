a, b = 1,2
n = 4 * 10**6
sum_even = 2

while b < n:
    c = a + b
    a = b
    b = c
    
    if c % 2 == 0 and c < n:
        sum_even += c

print(sum_even)