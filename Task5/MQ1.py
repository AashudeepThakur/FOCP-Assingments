int = input("Enter your name")
if int.split()[0] == "lord" or int.split()[0] == "lady":
    try:
        print(f"It shall be so, Lord {int.split()[1]}")
    except IndexError:
        print("Enter your full name")
else:
    print(f"You may not be known by that name!")

