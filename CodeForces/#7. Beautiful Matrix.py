matrix = []
n = 5

for i in range(n):
    matrix.append([]) 

print(matrix)

for i in range(n):
    row = list(map(int, input("Enter a row: ").rstrip().split()))
    matrix[i] = row

location = []
for i in range(n): 
    for j in range(n):
        if matrix[i][j] == 1:
            location = [i+1, j+1]
            break 

# Check distance from middle
center_x = ((n+1)/2)
center_y = ((n+1)/2)

# check location
move = abs(location[0] - center_x + location[1] - center_y)
print(move)