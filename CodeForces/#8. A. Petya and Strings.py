x = str(input("Enter a string 1: ").lower())
y = str(input("Enter a string 2: ").lower())

list = [x,y]
# test values

count = 0
sorted_words = sorted(list)

if x == y:
    count = 0 
elif sorted_words[0] == x and sorted_words[1] == y:
    count -= 1
elif sorted_words[0] == y and sorted_words[1] == x:
    count += 1

print(count)
