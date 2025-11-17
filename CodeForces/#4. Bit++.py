def function(n):
    value = n
    change = str(input("Enter the change: "))
    if change == "++x" or change == "x++":
        value += 1
    elif change == "--x" or change == 'x--':
        value -= 1 
    else:
        raise ValueError
    print(value)
    
function(50)