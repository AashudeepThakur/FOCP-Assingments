name = input("Enter your name: ")
phone = input("Enter your phone: ")

f = open("contacts.txt", "w")

for i in range(3):
    name = input("Enter your name: ")
    phone = input("Enter your phone: ")
    name_newformat = f"{name.split()[1].upper()} ,{name.split()[0]} : {phone}"

    f.write(name_newformat)

f.close()
