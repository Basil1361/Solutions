x = str(input("Enter a username: "))
lists = []
while True:
    try:
        if len(x) >= 100:
            print("Try again")
            continue
        else:
            break
    except ValueError:
            print("ValueError!")

r = [char for char in x]
unique_list = list(set(r))
if len(unique_list) % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
    