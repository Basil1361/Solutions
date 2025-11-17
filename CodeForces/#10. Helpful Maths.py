x = input()

values = list(map(int, x.split('+')))

sorted_list = sorted(values)
result = '+'.join(map(str, sorted_list))
print(result)