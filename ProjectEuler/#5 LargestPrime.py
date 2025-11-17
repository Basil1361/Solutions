def largest_prime_factor(n):
    # Remove all factors of 2
    while n % 2 == 0:
        largest = 2
        n = n // 2
        
    # now n is an odd number
    i = 3
    # Complexity is n^1/2 = i, so i^2 = n
    while i * i <= n:
        while n % i == 0:
            largest = i
            n = n // i
        i += 2  
        
    if n > 2:
        largest = n
    
    return largest

number = 600851475143
result = largest_prime_factor(number)
print(f"Largest prime factor of {number} is: {result}")