
while True:
    try:
        a,n,m = map(int, input("Enter a value: ").split())
        if a >= 10^9 and n <= 1:
            print("Try again")
            continue
        else:
            k = min(a,n,m)
            print(k)
            break
    except ValueError:
        print("Try again")
        
    
    
