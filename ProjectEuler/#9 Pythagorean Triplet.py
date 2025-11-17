final_answer = 0 
n = 1000
for c in range(n//3, n//2):
    for b in range((n-c)//2,c):
        a = n - c - b
        if a*a + b*b == c*c:
            final_answer = a*b*c
        
print(final_answer)
            
# or

final_answer = 0 
n = 1000
for c in range(n):
    for b in range(n):
            a = n - c - b
            if a*a + b*b == c*c and a > 0 and b > 0 and c > 0:
                final_answer = a*b*c

print(final_answer)
            
        